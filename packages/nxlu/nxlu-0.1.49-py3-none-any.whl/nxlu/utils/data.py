import logging
import warnings
from typing import Any

import networkx as nx

warnings.filterwarnings("ignore")


logger = logging.getLogger("nxlu")


__all__ = [
    "create_graph_from_data",
    "inspect_data",
    "filter_graph_by_relation",
    "construct_graph",
]


def create_graph_from_data(data: dict[str, Any]) -> nx.Graph:
    """Create a NetworkX graph from general-purpose data.

    Parameters
    ----------
    data : Dict[str, Any]
        Dictionary containing 'nodes' and 'edges' with their attributes.

    Returns
    -------
    nx.Graph
        The constructed NetworkX graph.
    """
    graph = nx.Graph()

    for node in data.get("nodes", []):
        node_id = node.get("id")
        if node_id is None:
            logger.warning("A node without an 'id' was found and skipped.")
            continue
        attributes = node.get("attributes", {})
        graph.add_node(node_id, **attributes)

    for edge in data.get("edges", []):
        source = edge.get("source")
        target = edge.get("target")
        if source is None or target is None:
            logger.warning(f"Incomplete edge data {edge} found and skipped.")
            continue
        attributes = edge.get("attributes", {})
        graph.add_edge(source, target, **attributes)

    return graph


def validate_graph(G: nx.Graph) -> bool:
    for u, v in G.edges():
        if not G.has_node(u) or not G.has_node(v):
            logger.error(f"Invalid edge detected between {u} and {v}.")
            return False
    logger.info("Graph validation successful.")
    return True


def inspect_data(dataset: dict[str, Any]) -> tuple[Any, Any]:
    """Inspect and print the types and samples of 'nodes' and 'links' in the dataset.

    Parameters
    ----------
    dataset : Dict[str, Any]
        The dataset containing 'nodes' and 'links'.

    Returns
    -------
    Tuple[Any, Any]
        The 'nodes' and 'links' extracted from the dataset.
    """
    nodes = dataset.get("nodes")
    links = dataset.get("links")

    if isinstance(nodes, list):
        for _node in nodes[:5]:
            pass
    elif isinstance(nodes, dict):
        for _key, _value in list(nodes.items())[:5]:
            pass
    else:
        pass

    if isinstance(links, list):
        for _link in links[:5]:
            pass
    elif isinstance(links, dict):
        for _key, _value in list(links.items())[:5]:
            pass
    else:
        pass

    return nodes, links


def filter_graph_by_relation(
    graph: nx.MultiDiGraph, desired_relation: str = "phenotype_phenotype"
) -> nx.Graph:
    """Filter the graph to include only edges with the specified 'relation' attribute.

    Parameters
    ----------
    graph : nx.MultiDiGraph
        The original graph.
    desired_relation : str, optional
        The relation attribute to filter edges by, by default "phenotype_phenotype".

    Returns
    -------
    nx.Graph
        The filtered graph containing only the desired edges.
    """
    filtered_graph = nx.Graph()
    filtered_graph.graph.update(graph.graph)

    for u, v, key, data in graph.edges(keys=True, data=True):
        if data.get("relation") == desired_relation:
            filtered_graph.add_edge(u, v, key=key, **data)

    return filtered_graph


def construct_graph(nodes: Any, links: Any) -> nx.Graph:
    """Construct a NetworkX graph from nodes and links.

    Parameters
    ----------
    nodes : Any
        List or dict of nodes with optional attributes.
    links : Any
        List or dict of links with optional attributes.

    Returns
    -------
    nx.Graph
        The constructed NetworkX graph.
    """
    graph = nx.Graph()

    if isinstance(nodes, list):
        if not nodes:
            logger.warning("'nodes' list is empty.")
        elif isinstance(nodes[0], dict):
            for node in nodes:
                node_id = node.get("id")
                weight = node.get("weight", 1)
                if node_id:
                    graph.add_node(node_id, weight=weight)
                else:
                    logger.warning("A node without an 'id' was found and skipped.")
        else:
            graph.add_nodes_from((node, {"weight": 1}) for node in nodes)
    elif isinstance(nodes, dict):
        graph.add_nodes_from(
            (node_id, {"weight": weight}) for node_id, weight in nodes.items()
        )
    else:
        logger.warning("Unrecognized 'nodes' structure. Nodes may not have weights.")
        try:
            graph.add_nodes_from((node, {"weight": 1}) for node in nodes)
        except Exception:
            logger.exception("Error adding nodes")

    if isinstance(links, list):
        if not links:
            logger.warning("'links' list is empty.")
        else:
            first_link = links[0]
            if isinstance(first_link, tuple):
                for link in links:
                    if isinstance(link, tuple):
                        if len(link) == 3:
                            source, target, weight = link
                            graph.add_edge(source, target, weight=weight)
                        elif len(link) == 2:
                            source, target = link
                            graph.add_edge(source, target, weight=1)
                        else:
                            logger.warning(
                                f"Unexpected link tuple size {len(link)}: {link}"
                            )
                    else:
                        logger.warning(f"Link is not a tuple: {link}")
            elif isinstance(first_link, dict):
                for link in links:
                    if isinstance(link, dict):
                        source = link.get("source")
                        target = link.get("target")
                        weight = link.get("weight", 1)
                        if source and target:
                            graph.add_edge(source, target, weight=weight)
                        else:
                            logger.warning(f"Incomplete link data {link}")
                    else:
                        logger.warning(f"Link is not a dict: {link}")
            else:
                logger.warning(f"Unexpected link type: {type(first_link)}")
    elif isinstance(links, dict):
        first_key = next(iter(links), None)
        if isinstance(first_key, tuple):
            for edge, attrs in links.items():
                if isinstance(edge, tuple) and len(edge) >= 2:
                    source, target = edge[:2]
                    weight = attrs.get("weight", 1) if isinstance(attrs, dict) else 1
                    graph.add_edge(source, target, weight=weight)
                else:
                    logger.warning(
                        f"Invalid edge format {edge} with attributes {attrs}"
                    )
        else:
            for source, targets in links.items():
                for target in targets:
                    graph.add_edge(source, target, weight=1)
    else:
        logger.warning("Unrecognized 'links' structure. No edges added.")

    return graph
