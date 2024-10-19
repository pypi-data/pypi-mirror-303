import inspect
import logging
import random
import threading
import types
import warnings
from collections.abc import Callable
from typing import Any

import networkx as nx
import numpy as np
from sentence_transformers import SentenceTransformer

from nxlu.constants import CUSTOM_ALGORITHMS, GENERATORS_TO_DICT
from nxlu.getters import get_available_algorithms
from nxlu.utils.misc import cosine_similarity

warnings.filterwarnings("ignore")

random.seed(42)
rng = np.random.default_rng(seed=42)
logger = logging.getLogger("nxlu")

AVAILABLE_ALGORITHMS = get_available_algorithms(nxlu_only=False)

__all__ = [
    "get_algorithm_function",
    "map_algorithm_result",
    "apply_algorithm",
    "register_custom_algorithm",
    "GraphProperties",
    "filter_relevant_nodes",
]

_hits_lock = threading.Lock()


def get_algorithm_function(
    algorithm_name: str, algorithm_dict: dict = AVAILABLE_ALGORITHMS
) -> Callable:
    """Retrieve the appropriate algorithm function by name.

    Parameters
    ----------
    algorithm_name : str
        The name of the algorithm to retrieve.
    algorithm_dict : Dict[str, Callable]
        Dictionary of available algorithms.

    Returns
    -------
    Callable
        The function corresponding to the algorithm.

    Raises
    ------
    ValueError
        If the algorithm is not found in NetworkX or custom algorithms.
    """
    if algorithm_name in CUSTOM_ALGORITHMS:
        return CUSTOM_ALGORITHMS[algorithm_name]

    if algorithm_name in algorithm_dict:
        return algorithm_dict[algorithm_name]

    raise ValueError(f"Algorithm '{algorithm_name}' not found.")


def map_algorithm_result(graph: nx.Graph, algorithm: str, result: Any) -> None:
    """
    Map the result of an algorithm to the graph's nodes, edges, or attributes.

    Parameters
    ----------
    graph : nx.Graph
        The NetworkX graph to map the results onto.
    algorithm : str
        The name of the algorithm.
    result : Any
        The result returned by the algorithm.
    """
    if isinstance(result, dict):
        if all(graph.has_node(node) for node in result):
            for node, value in result.items():
                graph.nodes[node].setdefault("algorithm_results", {})[algorithm] = value
            logger.info(f"Mapped node attributes for algorithm '{algorithm}'.")
            return

        if all(isinstance(key, tuple) and graph.has_edge(*key) for key in result):
            for edge, value in result.items():
                if graph.has_edge(*edge):
                    if isinstance(graph, nx.MultiGraph):
                        for key in graph[edge[0]][edge[1]]:
                            graph.edges[edge[0], edge[1], key].setdefault(
                                "algorithm_results", {}
                            )[algorithm] = value
                    else:
                        graph.edges[edge[0], edge[1]].setdefault(
                            "algorithm_results", {}
                        )[algorithm] = value
            logger.info(f"Mapped edge attributes for algorithm '{algorithm}'.")
            return

        graph.graph.setdefault("algorithm_results", {})[algorithm] = result
        logger.info(f"Mapped graph-level attribute for algorithm '{algorithm}'.")
        return

    if isinstance(result, list):
        if all(isinstance(item, tuple) and len(item) == 2 for item in result):
            for edge in result:
                if graph.has_edge(*edge):
                    if isinstance(graph, nx.MultiGraph):
                        for key in graph[edge[0]][edge[1]]:
                            graph.edges[edge[0], edge[1], key].setdefault(
                                "algorithm_results", {}
                            )[algorithm] = True
                    else:
                        graph.edges[edge[0], edge[1]].setdefault(
                            "algorithm_results", {}
                        )[algorithm] = True
            logger.info(f"Mapped edge presence for algorithm '{algorithm}'.")
            return

        graph.graph.setdefault("algorithm_results", {})[algorithm] = result
        logger.info(
            f"Mapped list as graph-level attribute for algorithm '{algorithm}'."
        )
        return

    if isinstance(result, (int, float, str)):
        graph.graph.setdefault("algorithm_results", {})[algorithm] = result
        logger.info(f"Mapped scalar graph-level attribute for algorithm '{algorithm}'.")
        return

    logger.warning(
        f"Unhandled result type for algorithm '{algorithm}'. No mapping performed."
    )


def analyze_relationships(graph: nx.Graph) -> str:
    """Generate a summary of all relationships within the graph, including edge weights.

    Parameters
    ----------
    graph : nx.Graph
        The NetworkX graph to analyze.

    Returns
    -------
    str
        A summary string of all relationships in the graph.
    """
    relationship_summary = "Graph Relationships:\n"
    for u, v, data in graph.edges(data=True):
        relation = data.get("relation", "EDGE")
        weight = data.get("weight", "N/A")
        relationship_summary += f"{u} -- {relation} (Weight: {weight}) --> {v}\n"
    return relationship_summary


def apply_algorithm(
    algorithm_encyclopedia: dict[str, dict[str, Any]],
    graph: nx.Graph,
    algorithm_name: str,
    **kwargs,
) -> Any:
    """Apply a NetworkX algorithm or a custom algorithm to the graph.

    Parameters
    ----------
    algorithm_encyclopedia : dict
        An encyclopedia of supported algorithms and their metadata.
    graph : nx.Graph
        The input graph.
    algorithm_name : str
        The name of the algorithm to apply.
    **kwargs : Additional keyword arguments for the algorithm.

    Returns
    -------
    Any
        The result of the algorithm.

    Raises
    ------
    ValueError
        If the algorithm is not found or an error occurs during application.
    """
    logger.info(f"Applying algorithm: {algorithm_name}")

    try:
        algorithm = get_algorithm_function(algorithm_name)
    except ValueError:
        logger.exception("Error getting algorithm function")
        raise

    graph_to_use = graph.copy()
    if graph_to_use.number_of_nodes() == 0:
        error_msg = f"Algorithm '{algorithm_name}' cannot be applied to an empty graph."
        logger.error(error_msg)
        raise ValueError(error_msg)
    algorithm_metadata = algorithm_encyclopedia.get(algorithm_name)

    if algorithm_metadata:
        # Handle Directedness
        requires_directed = algorithm_metadata.get("directed", None)
        if requires_directed is True and not graph_to_use.is_directed():
            graph_to_use = graph_to_use.to_directed()
            logger.info(f"Converted graph to directed for algorithm '{algorithm_name}'")
        elif requires_directed is False and graph_to_use.is_directed():
            graph_to_use = graph_to_use.to_undirected()
            logger.info(
                f"Converted graph to undirected for algorithm '{algorithm_name}'"
            )

        # Check for minimum number of nodes
        min_nodes = algorithm_metadata.get("min_nodes", None)
        if min_nodes is not None and graph_to_use.number_of_nodes() < min_nodes:
            error_msg = (
                f"Algorithm '{algorithm_name}' requires at least {min_nodes} nodes, "
                f"but graph has {graph_to_use.number_of_nodes()} nodes."
            )
            logger.error(error_msg)
            raise ValueError(error_msg)

        # Check if the algorithm requires a DAG
        requires_dag = algorithm_metadata.get("requires_dag", False)
        if requires_dag:
            if not graph_to_use.is_directed():
                error_msg = f"Algorithm '{algorithm_name}' requires a directed acyclic "
                "graph (DAG)."
                logger.error(error_msg)
                raise ValueError(error_msg)
            if not nx.is_directed_acyclic_graph(graph_to_use):
                error_msg = f"Algorithm '{algorithm_name}' requires a directed acyclic "
                "graph (DAG)."
                logger.error(error_msg)
                raise ValueError(error_msg)

        # Check if the algorithm requires a tree
        requires_tree = algorithm_metadata.get("requires_tree", False)
        if requires_tree:
            if graph_to_use.is_directed():
                if not nx.is_arborescence(graph_to_use):
                    error_msg = f"Algorithm '{algorithm_name}' requires the graph to "
                    "be a directed tree (arborescence)."
                    logger.error(error_msg)
                    raise ValueError(error_msg)
            elif not nx.is_tree(graph_to_use):
                error_msg = (
                    f"Algorithm '{algorithm_name}' requires the graph to be a tree."
                )
                logger.error(error_msg)
                raise ValueError(error_msg)

        # Check if the algorithm requires connectedness
        requires_connectedness = algorithm_metadata.get("requires_connectedness", False)
        if requires_connectedness:
            if graph_to_use.is_directed():
                is_connected = nx.is_weakly_connected(graph_to_use)
            else:
                is_connected = nx.is_connected(graph_to_use)
            if not is_connected:
                # Use the largest connected component
                if graph_to_use.is_directed():
                    connected_components = nx.weakly_connected_components(graph_to_use)
                else:
                    connected_components = nx.connected_components(graph_to_use)
                largest_cc = max(connected_components, key=len)
                graph_to_use = graph_to_use.subgraph(largest_cc).copy()
                logger.info(f"Using LCC for algorithm '{algorithm_name}'")

        # Check if the algorithm requires weighted edges
        requires_weighted = algorithm_metadata.get("weighted", False)
        if requires_weighted and not nx.is_weighted(graph_to_use):
            # Assign default weight to edges
            for _u, _v, data in graph_to_use.edges(data=True):
                data["weight"] = 1.0
            logger.info(
                f"Assigned default weight to edges for algorithm '{algorithm_name}'"
            )
            # Ensure 'weight' parameter is set
            if (
                "weight" in inspect.signature(algorithm).parameters
                and "weight" not in kwargs
            ):
                kwargs["weight"] = "weight"

        # Check if the algorithm requires symmetry (undirected graph)
        requires_symmetry = algorithm_metadata.get("requires_symmetry", False)
        if requires_symmetry and graph_to_use.is_directed():
            graph_to_use = graph_to_use.to_undirected()
            logger.info(
                f"Converted graph to undirected for algorithm '{algorithm_name}'"
            )

        # Handle self_loops if necessary
        self_loops = algorithm_metadata.get("self_loops", None)
        if self_loops is not None and not self_loops:
            graph_to_use.remove_edges_from(nx.selfloop_edges(graph_to_use))
            logger.info(f"Removed self-loops for algorithm '{algorithm_name}'")

    try:
        sig = inspect.signature(algorithm)
        # Set default for 'k' parameter
        if "k" in sig.parameters and "k" not in kwargs:
            if algorithm_name == "all_node_cuts":
                default_k = 2
            else:
                default_k = min(100, graph_to_use.number_of_nodes())
            kwargs["k"] = default_k
            logger.info(f"Parameter 'k' set to {default_k} by default.")

        # Check and set default for 'weight' parameter
        if "weight" in sig.parameters and "weight" not in kwargs:
            if nx.is_weighted(graph_to_use):
                kwargs["weight"] = "weight"
                logger.info("Parameter 'weight' set to 'weight'.")
            else:
                for _u, _v, data in graph_to_use.edges(data=True):
                    data["weight"] = 1.0
                kwargs["weight"] = "weight"
                logger.info("Assigned default weight of 1.0 to edges.")

        # Set 'normalized' parameter for 'rich_club_coefficient'
        if algorithm_name == "rich_club_coefficient":
            if "normalized" in sig.parameters and "normalized" not in kwargs:
                kwargs["normalized"] = False
                logger.info(
                    "Parameter 'normalized' set to False for 'rich_club_coefficient'."
                )

    except (ValueError, TypeError) as e:
        logger.warning(
            f"Could not inspect signature of '{algorithm_name}': {e}. Proceeding "
            f"without setting 'k' or 'weight'."
        )

    try:
        result = algorithm(graph_to_use, **kwargs)
        logger.info(f"Algorithm '{algorithm_name}' applied successfully.")
    except Exception as e:
        error_msg = f"Error applying algorithm '{algorithm_name}': {e!s}"
        logger.exception(error_msg)
        raise ValueError(error_msg)

    if algorithm_name in GENERATORS_TO_DICT:
        try:
            result = dict(result)
            logger.debug(f"Converted generator result of '{algorithm_name}' to dict.")
        except Exception as e:
            error_msg = f"Failed to convert generator result of '{algorithm_name}' "
            f"to dict: {e!s}"
            logger.exception(error_msg)
            raise ValueError(error_msg)
    elif isinstance(result, types.GeneratorType):
        result = list(result)
        logger.debug(f"Converted generator result of '{algorithm_name}' to list.")

    return result


def register_custom_algorithm(name: str, func: Callable) -> None:
    """Register a custom algorithm.

    Parameters
    ----------
    name : str
        The name of the custom algorithm.
    func : Callable
        The function implementing the custom algorithm.
    """
    CUSTOM_ALGORITHMS[name] = func


class GraphProperties:
    """A class to compute and store various properties of a NetworkX graph.

    This class provides a range of attributes describing the structural properties
    of a graph, such as whether it's connected, bipartite, weighted, or planar.
    It also includes methods for identifying hubs and authorities using the HITS
    algorithm.

    Attributes
    ----------
    graph : nx.Graph
        The input NetworkX graph.
    is_directed : bool
        Whether the graph is directed.
    num_nodes : int
        The number of nodes in the graph.
    num_edges : int
        The number of edges in the graph.
    density : float
        The density of the graph.
    is_strongly_connected : bool
        Whether the graph is strongly connected (only relevant for directed graphs).
    is_connected : bool
        Whether the graph is connected (weakly connected for directed graphs).
    is_bipartite : bool
        Whether the graph is bipartite.
    is_planar : bool
        Whether the graph is planar.
    is_tree : bool
        Whether the graph is a tree.
    has_edge_data : bool
        Whether the edges of the graph contain additional data.
    has_node_data : bool
        Whether the nodes of the graph contain additional data.
    is_multigraph : bool
        Whether the graph is a multigraph.
    is_weighted : bool
        Whether the graph is weighted.
    average_clustering : float
        The average clustering coefficient of the graph.
    degree_hist : list[int]
        The degree histogram of the graph.
    peak_degree : int or None
        The degree with the highest frequency in the graph, or None if no peak exists.
    hubs : list[str]
        List of influential hubs in the graph based on the HITS algorithm.
    authorities : list[str]
        List of influential authorities in the graph based on the HITS algorithm.

    Methods
    -------
    _identify_hits(G: nx.Graph, z_threshold: float = 1.5) -> tuple[list[str], list[str]]
    :
        Identify influential hubs and authorities in the graph using the HITS
        algorithm.
    _compute_peak_degree() -> int or None:
        Compute the peak degree of the graph based on the degree histogram.
    """

    def __init__(
        self,
        graph: nx.Graph,
        compute_peak_degree: bool = True,
        identify_hits: bool = True,
        z_threshold: float = 2.0,
    ):
        """Initialize the GraphProperties object and computes various properties of the
        graph.

        Parameters
        ----------
        graph : nx.Graph
            The input NetworkX graph.
        compute_peak_degree : bool
            Compute the peak degree of the graph based on the degree histogram. Default
            is True
        identify_hits : bool
            Identify influential hubs and authorities in the graph using the HITS
            algorithm. Default is True.
        z_threshold : float
            The z-score threshold for qualifying a node as a hub or authority.
        """
        self.graph = graph
        self.is_directed = graph.is_directed()
        self.num_nodes = graph.number_of_nodes()
        self.num_edges = graph.number_of_edges()
        self.density = nx.density(graph)
        self.is_strongly_connected = (
            nx.is_strongly_connected(graph) if self.is_directed else False
        )
        self.is_connected = (
            nx.is_connected(graph)
            if not self.is_directed
            else nx.is_weakly_connected(graph)
        )
        self.is_bipartite = (
            nx.is_bipartite(graph) if "bipartite" in graph.graph else False
        )
        self.is_planar = (
            nx.check_planarity(graph)[0] if "planar" in graph.graph else False
        )
        self.is_tree = nx.is_tree(graph) if "is_tree" in graph.graph else False
        self.has_edge_data = (
            any(graph.edges[edge] for edge in graph.edges())
            if "has_edge_data" in graph.graph
            else False
        )
        self.has_node_data = (
            any(graph.nodes[node] for node in graph.nodes())
            if "has_node_data" in graph.graph
            else False
        )
        self.is_multigraph = graph.is_multigraph()
        self.is_weighted = nx.is_weighted(graph)
        self.degree_hist = nx.degree_histogram(graph) if self.num_nodes > 0 else []
        degrees = [d for n, d in graph.degree()]
        self.min_degree = min(degrees)
        self.max_degree = max(degrees)
        self.avg_degree = sum(degrees) / len(degrees)
        if compute_peak_degree:
            self.peak_degree = self._compute_peak_degree()
        if identify_hits:
            self.hubs, self.authorities = self._identify_hits(
                graph, z_threshold=z_threshold
            )

    @staticmethod
    def _identify_hits(
        G: nx.Graph, z_threshold: float = 1.5
    ) -> tuple[list[str], list[str]]:
        """Identify influential hubs and authorities in a graph using the HITS algorithm
        and dynamic z-score thresholding.

        Parameters
        ----------
        G : nx.Graph
            The input graph.
        z_threshold : float, optional
            Z-score threshold to identify outliers based on hub and authority scores,
            by default 1.5

        Returns
        -------
        Tuple[List[str], List[str]]
            A tuple containing two lists:
            - Hubs: List of nodes with hub scores beyond the z-score threshold.
            - Authorities: List of nodes with authority scores beyond the z-score
            threshold.
        """
        with _hits_lock:
            hits_hub_scores, hits_authority_scores = nx.hits(
                G, max_iter=50, normalized=True
            )

        hub_scores = np.array(list(hits_hub_scores.values()))
        authority_scores = np.array(list(hits_authority_scores.values()))

        mean_hub = np.mean(hub_scores)
        std_hub = np.std(hub_scores)

        mean_authority = np.mean(authority_scores)
        std_authority = np.std(authority_scores)

        hubs = [
            node
            for node, score in hits_hub_scores.items()
            if (score - mean_hub) / std_hub > z_threshold
        ]
        authorities = [
            node
            for node, score in hits_authority_scores.items()
            if (score - mean_authority) / std_authority > z_threshold
        ]

        logger.info(f"Hubs identified: {hubs}")
        logger.info(f"Authorities identified: {authorities}")

        return hubs, authorities

    def _compute_peak_degree(self):
        """Compute the peak degree in the graph based on the degree histogram.

        Returns
        -------
        int or None
            The degree with the highest frequency in the graph, or None if no peak
            exists.
        """
        if self.degree_hist:
            max_degree = max(self.degree_hist)
            return self.degree_hist.index(max_degree)
        return None


def filter_relevant_nodes(
    nodes: list[str], query: str, model: SentenceTransformer, z_threshold: float = 1.0
) -> list[str]:
    """Filter nodes based on their semantic relevance to the user's query using
    embeddings and z-score thresholding.

    Parameters
    ----------
    nodes : List[str]
        The list of node labels (hubs or authorities) to filter.
    query : str
        The user's query string.
    model : SentenceTransformer
        The sentence-transformer model used to generate embeddings.
    z_threshold : float, optional
        The z-score threshold for determining relevance, by default 2.0.

    Returns
    -------
    List[str]
        A list of nodes that are semantically relevant to the user's query.
    """
    if not nodes:
        return []

    query_embedding = model.encode([query])
    node_embeddings = model.encode(nodes)

    similarities = cosine_similarity(node_embeddings, query_embedding).flatten()

    mean_sim = np.mean(similarities)
    std_sim = np.std(similarities)
    if std_sim == 0:
        std_sim = 1e-10

    # dynamic threshold based on z-scores
    threshold = mean_sim + z_threshold * std_sim
    relevant_nodes = [
        node for node, sim in zip(nodes, similarities) if sim >= threshold
    ]

    logger.info(f"{len(relevant_nodes)} nodes relevant to the query.")

    return relevant_nodes
