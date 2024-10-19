import logging
import math
import statistics
import warnings
from collections import defaultdict
from typing import Any

import networkx as nx
from sentence_transformers import SentenceTransformer

from nxlu.explanation.classify import classify_domain
from nxlu.processing.analyze import GraphProperties, filter_relevant_nodes
from nxlu.processing.preprocess import assign_default_weights

warnings.filterwarnings("ignore")


logger = logging.getLogger("nxlu")


__all__ = ["characterize_graph", "format_numeric_value", "format_algorithm_results"]


def characterize_graph(
    graph: nx.Graph,
    graph_props: GraphProperties,
    user_query: str | None = None,
    detect_domain: bool = False,
    max_nodes_for_embedding: int = 100,
) -> str:
    """Generate a comprehensive summary of the graph, including representational and
    structural information based on node labels, edge types, and graph metrics.

    Parameters
    ----------
    graph : nx.Graph
        The graph to summarize.
    graph_props : GraphProperties
        Precomputed graph properties.
    user_query : Optional[str], optional
        The user's query to determine relevant hubs and authorities.
    detect_domain : bool
        Classify the data domain of the graph based on its node attributes.
    max_nodes_for_embedding : int, optional
        Maximum number of nodes to consider for embedding (default is 100).

    Returns
    -------
    str
        A comprehensive summary of the graph.
    """
    if not isinstance(graph, nx.Graph):
        raise TypeError(
            "Invalid graph input: 'graph' must be an instance of networkx.Graph."
        )

    if not isinstance(graph_props, GraphProperties):
        raise TypeError(
            "Invalid graph properties: 'graph_props' must be an instance of "
            "GraphProperties."
        )

    assign_default_weights(graph)

    summary_parts = [
        f"The graph has {graph_props.num_nodes} nodes and {graph_props.num_edges} "
        f"edges."
    ]

    node_labels = nx.get_node_attributes(graph, "label")
    edge_labels = nx.get_edge_attributes(graph, "relationship")

    if node_labels:
        unique_node_labels = set(node_labels.values())
        summary_parts.append(f"Nodes represent: {', '.join(unique_node_labels)}.")

    if edge_labels:
        unique_edge_labels = set(edge_labels.values())
        summary_parts.append(
            f"Edges represent: {', '.join(unique_edge_labels)} relationships."
        )

    properties = (
        f"Directed: {graph_props.is_directed}, "
        f"Multigraph: {graph_props.is_multigraph}, "
        f"Bipartite: {graph_props.is_bipartite}, "
        f"Weighted: {graph_props.is_weighted}, "
        f"Tree: {graph_props.is_tree}, "
        f"Planar: {graph_props.is_planar}, "
        f"Strongly Connected: {graph_props.is_strongly_connected}, "
        f"Connected: {graph_props.is_connected} (if disconnected, preprocessing may "
        "force connectedness in some cases, depending on the algorithms applied "
        f"during analysis)."
    )
    summary_parts.append(f"The graph has the following properties: {properties}")

    if graph_props.num_nodes > 0:
        summary_parts.append(
            f"It has an average clustering coefficient of "
            f"{graph_props.average_clustering:.2f}."
        )
        summary_parts.append(f"The graph density is {graph_props.density:.3f}.")

    if graph_props.degree_hist:
        peak_degree = graph_props.peak_degree
        peak_count = graph_props.degree_hist[peak_degree]
        summary_parts.append(
            f"It has a degree distribution that peaks at index {peak_degree} on the "
            f"degree histogram with a degree of {peak_count}."
        )
        summary_parts.append(
            f"The maximum degree is: {graph_props.max_degree}, "
            f"the minimum degree is: {graph_props.min_degree}, "
            f"and the average degree is: {graph_props.avg_degree}"
        )

    truncated_nodes = list(graph.nodes(data=True))[:max_nodes_for_embedding]
    truncated_node_set = {node[0] for node in truncated_nodes}

    truncated_edges = [
        (u, v, d)
        for u, v, d in graph.edges(data=True)
        if u in truncated_node_set and v in truncated_node_set
    ]
    truncated_edge_labels = [
        edge_labels.get((u, v), "unknown") for u, v, _ in truncated_edges
    ]

    if detect_domain:
        domain = classify_domain(
            {
                "nodes": truncated_nodes,
                "edges": truncated_edge_labels,
                "query": user_query,
            }
        )
        summary_parts.append(
            f"The graph likely represents data in the domain of: {domain}."
        )

    if (graph_props.hubs or graph_props.authorities) and user_query:
        stmodel = SentenceTransformer("all-MiniLM-L6-v2")
        relevant_hubs = filter_relevant_nodes(graph_props.hubs, user_query, stmodel)
        relevant_authorities = filter_relevant_nodes(
            graph_props.authorities, user_query, stmodel
        )

        if relevant_hubs:
            summary_parts.append(
                f"Identified Network Hubs: {', '.join(relevant_hubs)}."
            )

        if relevant_authorities:
            summary_parts.append(
                f"Identified Network Authorities: {', '.join(relevant_authorities)}."
            )

    return " ".join(summary_parts)


def format_numeric_value(value: float) -> Any:
    """Format numeric values by rounding, capping, or zeroing based on magnitude.

    Parameters
    ----------
    value : float
        The numeric value to format.

    Returns
    -------
    Any
        The formatted value.
    """
    if isinstance(value, (int, float)):
        if abs(value) >= 1e10:
            return float("inf")
        if abs(value) <= 1e-4:
            return 0.0
        return round(value, 4)
    return value


def format_algorithm_results(results):
    """Consolidate and format the results of multiple graph algorithms.

    Parameters
    ----------
    results : List[Tuple[str, Any]]
        List of tuples containing algorithm names and their result data.

    Returns
    -------
    str
        A formatted and consolidated summary of all algorithm results.
    """
    if not isinstance(results, list):
        raise TypeError("`results` should be a list of tuples")
    for item in results:
        if not isinstance(item, tuple) or len(item) != 2:
            raise TypeError(
                "Each item in `results` should be a tuple of "
                "(algorithm_name, result_data)."
            )

    def format_numeric_value(val):
        if isinstance(val, float):
            if math.isinf(val):
                return "inf" if val > 0 else "-inf"
            if math.isnan(val):
                return "NaN"

            formatted_val = (
                f"{val:.4f}".rstrip("0").rstrip(".")
                if "." in f"{val:.4f}"
                else f"{val:.4f}"
            )
            if formatted_val == "":
                formatted_val = "0"
            return formatted_val

        if isinstance(val, int):
            return str(val)

        return str(val)

    def should_exclude(vals):
        return all(v in (0.0, 1.0) for v in vals)

    graph_results = {}
    node_results = defaultdict(list)
    edge_results = defaultdict(list)

    for alg, result in results:
        if isinstance(result, dict):
            if all(isinstance(k, str) and "-" in k for k in result):
                edge_results[alg] = list(result.values())
            else:
                node_results[alg] = list(result.values())
        elif isinstance(result, list):
            edge_results[alg] = result
        else:
            graph_results[alg] = result

    formatted_output = ""

    if graph_results:
        formatted_output += "**Graph-Level Results:**\n"
        for alg, val in graph_results.items():
            formatted_val = format_numeric_value(val)
            formatted_output += (
                f"- **{alg.replace('_', ' ').title()}**: {formatted_val}\n"
            )
        formatted_output += "\n"

    node_specific_output = ""
    for alg, vals in node_results.items():
        finite_vals = [
            v
            for v in vals
            if isinstance(v, (int, float)) and not (math.isinf(v) or math.isnan(v))
        ]
        if not finite_vals:
            logger.info(f"Excluding algorithm '{alg}' as all values are non-finite.")
            continue

        if should_exclude(finite_vals):
            logger.info(f"Excluding algorithm '{alg}' as all values are 0.0 or 1.0.")
            continue

        formatted_vals = [format_numeric_value(v) for v in finite_vals]

        node_specific_output += f"- **{alg.replace('_', ' ').title()}**:\n"
        if all(isinstance(v, (int, float)) for v in finite_vals):
            try:
                average = format_numeric_value(statistics.mean(finite_vals))
                median = format_numeric_value(statistics.median(finite_vals))
                try:
                    mode_val = format_numeric_value(statistics.mode(finite_vals))
                except statistics.StatisticsError:
                    mode_val = "N/A"
                std_dev = (
                    format_numeric_value(statistics.stdev(finite_vals))
                    if len(finite_vals) > 1
                    else "0.0"
                )
                node_specific_output += (
                    f"  - Average: {average}\n"
                    f"  - Median: {median}\n"
                    f"  - Mode: {mode_val}\n"
                    f"  - Std Dev: {std_dev}\n"
                )
            except OverflowError:
                node_specific_output += "  - Statistics: OverflowError\n"
        else:
            node_specific_output += f"  - Total: {len(finite_vals)} nodes\n"

    if node_specific_output:
        formatted_output += "**Node-Specific Results:**\n"
        formatted_output += node_specific_output
        formatted_output += "\n"

    edge_specific_output = ""
    for alg, vals in edge_results.items():
        if isinstance(vals, list) and all(isinstance(v, (int, float)) for v in vals):
            finite_vals = [
                v
                for v in vals
                if isinstance(v, (int, float)) and not (math.isinf(v) or math.isnan(v))
            ]
            if not finite_vals:
                logger.info(
                    f"Excluding algorithm '{alg}' as all values are non-finite."
                )
                continue

            if should_exclude(finite_vals):
                logger.info(
                    f"Excluding algorithm '{alg}' as all values are 0.0 or 1.0."
                )
                continue

            formatted_vals = [format_numeric_value(v) for v in finite_vals]

            edge_specific_output += f"- **{alg.replace('_', ' ').title()}**:\n"
            if all(isinstance(v, (int, float)) for v in finite_vals):
                try:
                    average = format_numeric_value(statistics.mean(finite_vals))
                    median = format_numeric_value(statistics.median(finite_vals))
                    try:
                        mode_val = format_numeric_value(statistics.mode(finite_vals))
                    except statistics.StatisticsError:
                        mode_val = "N/A"
                    std_dev = (
                        format_numeric_value(statistics.stdev(finite_vals))
                        if len(finite_vals) > 1
                        else "0.0"
                    )
                    edge_specific_output += (
                        f"  - Average: {average}\n"
                        f"  - Median: {median}\n"
                        f"  - Mode: {mode_val}\n"
                        f"  - Std Dev: {std_dev}\n"
                    )
                except OverflowError:
                    edge_specific_output += "  - Statistics: OverflowError\n"
            else:
                edge_specific_output += f"  - Total: {len(finite_vals)} edges\n"
        elif isinstance(vals, list):
            formatted_vals = []
            for v in vals:
                if isinstance(v, set):
                    formatted_vals.append(str(sorted(v)))
                else:
                    formatted_vals.append(str(v))
            edge_specific_output += (
                f"- **{alg.replace('_', ' ').title()}**: {formatted_vals}\n"
            )

    if edge_specific_output:
        formatted_output += "**Edge-Specific Results:**\n"
        formatted_output += edge_specific_output
        formatted_output += "\n"

    return formatted_output.strip()
