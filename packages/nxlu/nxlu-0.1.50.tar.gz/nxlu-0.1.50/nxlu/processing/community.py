import logging
from dataclasses import dataclass
from enum import Enum

import networkx as nx
import numpy as np
from sentence_transformers import SentenceTransformer

from nxlu.utils.misc import cosine_similarity

logger = logging.getLogger("nxlu")


class CommunityMethod(str, Enum):
    """Supported community detection methods."""

    LOUVAIN = "louvain"
    GIRVAN_NEWMAN = "girvan_newman"
    LABEL_PROPAGATION = "label_propagation"
    GREEDY_MODULARITY = "greedy_modularity"
    FLUID = "fluid"


@dataclass
class CommunityResolution:
    """Community detection results at a specific resolution."""

    resolution: float
    communities: list[set[str]]
    modularity: float
    method: CommunityMethod


@dataclass
class ConsensusResult:
    """Consensus community detection results."""

    communities: list[set[str]]
    modularity: float
    methods: list[CommunityMethod]
    stability: float
    hierarchical_levels: list[list[set[str]]]


class MultiResolutionDetector:
    """
    Multi-resolution community detection using NetworkX's native algorithms.

    This class combines multiple NetworkX community detection approaches:
    - Louvain for resolution-parameterized modularity optimization
    - Girvan-Newman for hierarchical community structure
    - Label propagation for fast detection at different scales
    - Greedy modularity maximization as a baseline
    - Fluid communities for variable-size community detection

    The consensus approach combines results across methods and resolutions
    to find stable community structures.

    Parameters
    ----------
    graph : nx.Graph
        Input graph for community detection
    min_resolution : float, optional
        Minimum resolution parameter for modularity-based methods, by default 0.1
    max_resolution : float, optional
        Maximum resolution parameter for modularity-based methods, by default 2.0
    n_resolutions : int, optional
        Number of resolution steps to use, by default 10
    methods : List[CommunityMethod], optional
        Community detection methods to use, by default all methods
    random_state : Optional[int], optional
        Random seed for reproducibility, by default None

    Attributes
    ----------
    resolutions : List[CommunityResolution]
        Results from each method/resolution combination
    consensus : Optional[ConsensusResult]
        Consensus clustering results if computed
    """

    def __init__(
        self,
        graph: nx.Graph,
        min_resolution: float = 0.1,
        max_resolution: float = 2.0,
        n_resolutions: int = 10,
        methods: list[CommunityMethod] | None = None,
        random_state: int | None = None,
    ):
        self.graph = graph.copy()
        self.min_resolution = min_resolution
        self.max_resolution = max_resolution
        self.n_resolutions = n_resolutions
        self.methods = methods or list(CommunityMethod)
        self.random_state = random_state

        self.resolutions: list[CommunityResolution] = []
        self.consensus: ConsensusResult | None = None

        self.rng = np.random.RandomState(random_state)

    def detect_communities(self) -> ConsensusResult:
        """
        Perform multi-resolution community detection.

        Returns
        -------
        ConsensusResult
            Consensus communities across methods and resolutions
        """
        logger.info("Starting multi-resolution community detection")

        resolutions = np.linspace(
            self.min_resolution, self.max_resolution, self.n_resolutions
        )

        # detect communities using each method at each resolution
        for method in self.methods:
            for resolution in resolutions:
                communities = self._detect_with_method(method, resolution)

                if communities:  # some methods may fail to find communities
                    modularity = nx.community.modularity(
                        self.graph, communities, resolution=resolution
                    )

                    self.resolutions.append(
                        CommunityResolution(
                            resolution=resolution,
                            communities=communities,
                            modularity=modularity,
                            method=method,
                        )
                    )

        # generate consensus communities
        self.consensus = self._generate_consensus()

        logger.info("Completed multi-resolution community detection")
        return self.consensus

    def _detect_with_method(
        self, method: CommunityMethod, resolution: int
    ) -> list[set[str]]:
        """
        Detect communities using specified method and resolution.

        Parameters
        ----------
        method : CommunityMethod
            Community detection method to use
        resolution : int
            Resolution parameter value

        Returns
        -------
        List[Set[str]]
            Detected communities as lists of node sets
        """
        try:
            if method == CommunityMethod.LOUVAIN:
                communities = nx.community.louvain_communities(
                    self.graph, resolution=resolution, seed=self.random_state
                )

            elif method == CommunityMethod.GIRVAN_NEWMAN:
                # use n_communities proportional to resolution
                n_communities = max(2, int(self.graph.number_of_nodes() * resolution))
                gn_communities = nx.community.girvan_newman(self.graph)
                for _ in range(n_communities - 1):
                    communities = next(gn_communities)

            elif method == CommunityMethod.LABEL_PROPAGATION:
                communities = nx.community.label_propagation_communities(self.graph)

            elif method == CommunityMethod.GREEDY_MODULARITY:
                communities = nx.community.greedy_modularity_communities(
                    self.graph, resolution=resolution
                )

            elif method == CommunityMethod.FLUID:
                # number of communities varies with resolution
                k = max(2, int(self.graph.number_of_nodes() * resolution))
                communities = nx.community.asyn_fluidc(
                    self.graph, k, seed=self.random_state
                )

            else:
                self._raise_unsupported_method_error(method)

            # convert node IDs to strings for consistency
            return [{str(n) for n in c} for c in communities]

        except Exception as e:
            logger.warning(
                f"Failed to detect communities with method {method} at resolution "
                f"{resolution}: {e!s}"
            )
            return []

    @staticmethod
    def _raise_unsupported_method_error(method: CommunityMethod):
        raise ValueError(f"Unsupported community detection method: {method}")

    def _generate_consensus(self) -> ConsensusResult:
        """
        Generate consensus communities from all methods/resolutions.

        Returns
        -------
        ConsensusResult
            Consensus communities and related metrics
        """
        if not self.resolutions:
            raise ValueError("No community detection results available")

        # build co-occurrence matrix
        n_nodes = self.graph.number_of_nodes()
        co_matrix = np.zeros((n_nodes, n_nodes))

        node_list = list(self.graph.nodes())
        node_to_idx = {str(node): i for i, node in enumerate(node_list)}

        # count node co-occurrences
        for result in self.resolutions:
            for community in result.communities:
                for node1 in community:
                    for node2 in community:
                        i, j = node_to_idx[node1], node_to_idx[node2]
                        co_matrix[i, j] += 1
                        co_matrix[j, i] += 1

        # normalize
        co_matrix /= len(self.resolutions)

        # convert co-occurrence matrix to graph
        consensus_graph = nx.Graph()
        for i in range(n_nodes):
            for j in range(i + 1, n_nodes):
                if (
                    co_matrix[i, j] > 0.5
                ):  # add edge if nodes co-occur in >50% of results
                    consensus_graph.add_edge(
                        node_list[i], node_list[j], weight=co_matrix[i, j]
                    )

        # get consensus communities using connected components
        consensus_communities = [
            {str(n) for n in c} for c in nx.connected_components(consensus_graph)
        ]

        # calculate consensus modularity
        consensus_modularity = nx.community.modularity(
            self.graph, consensus_communities
        )

        # calculate stability score
        stability = self._calculate_stability(consensus_communities)

        # generate hierarchical levels using Girvan-Newman
        hierarchical_levels = self._generate_hierarchy(consensus_communities)

        return ConsensusResult(
            communities=consensus_communities,
            modularity=consensus_modularity,
            methods=[r.method for r in self.resolutions],
            stability=stability,
            hierarchical_levels=hierarchical_levels,
        )

    def _calculate_stability(self, consensus: list[set[str]]) -> float:
        """
        Calculate stability score for consensus communities.

        Parameters
        ----------
        consensus : List[Set[str]]
            Consensus community assignments

        Returns
        -------
        float
            Stability score between 0 and 1
        """
        overlap_scores = []
        for result in self.resolutions:
            max_overlaps = []
            for cons_comm in consensus:
                # find best matching community
                max_overlap = max(
                    len(cons_comm.intersection(comm)) / len(cons_comm.union(comm))
                    for comm in result.communities
                )
                max_overlaps.append(max_overlap)
            overlap_scores.append(np.mean(max_overlaps))

        return float(np.mean(overlap_scores))

    def _generate_hierarchy(
        self, base_communities: list[set[str]]
    ) -> list[list[set[str]]]:
        """
        Generate hierarchical community levels using Girvan-Newman.

        Parameters
        ----------
        base_communities : List[Set[str]]
            Base level communities to subdivide

        Returns
        -------
        List[List[Set[str]]]
            List of community levels from coarsest to finest
        """
        hierarchy = [base_communities]

        # for each base community
        for community in base_communities:
            if len(community) <= 3:  # don't subdivide very small communities
                continue

            # create subgraph for this community
            subgraph = self.graph.subgraph(community)

            try:
                # Girvan-Newman
                gn_communities = nx.community.girvan_newman(subgraph)

                # add each level to hierarchy
                max_levels = min(len(community) - 1, 3)  # limit number of levels
                sub_levels = []
                for _ in range(max_levels):
                    level = next(gn_communities)
                    sub_levels.append([{str(n) for n in c} for c in level])

                if sub_levels:
                    hierarchy.extend(sub_levels)

            except Exception:
                logger.warning("Failed to generate hierarchy for community")
                continue

        return hierarchy

    def get_hierarchical_relationships(
        self,
    ) -> dict[tuple[int, str], list[tuple[int, str]]]:
        """
        Get hierarchical relationships between communities.

        Returns
        -------
        Dict[Tuple[int, str], List[Tuple[int, str]]]
            Mapping from (level, community_id) to child communities
        """
        if not self.consensus or not self.consensus.hierarchical_levels:
            return {}

        relationships = {}
        levels = self.consensus.hierarchical_levels

        for level_idx in range(len(levels) - 1):
            parent_level = levels[level_idx]
            child_level = levels[level_idx + 1]

            for parent_idx, parent in enumerate(parent_level):
                parent_key = (level_idx, f"community_{parent_idx}")
                children = []

                for child_idx, child in enumerate(child_level):
                    # Calculate overlap
                    overlap = len(parent.intersection(child)) / len(child)
                    if overlap > 0.5:  # Child belongs to parent if >50% overlap
                        children.append((level_idx + 1, f"community_{child_idx}"))

                if children:
                    relationships[parent_key] = children

        return relationships


class CommunityQueryMatcher:
    """Match queries to detected graph communities using semantic similarity.

    This class performs multi-resolution community detection on a graph and
    identifies the most semantically similar communities to a given query.

    Parameters
    ----------
    embedding_model_name : str
        Name of the sentence transformer model to use for embeddings
    min_resolution : float
        Minimum resolution parameter for community detection
    max_resolution : float
        Maximum resolution parameter for community detection
    n_resolutions : int
        Number of resolution steps
    methods : List[CommunityMethod]
        Community detection methods to use
    random_state : Optional[int]
        Random seed for reproducibility

    Attributes
    ----------
    model : SentenceTransformer
        Model for computing text embeddings
    detector : MultiResolutionDetector
        Multi-resolution community detector
    community_embeddings : Dict[Tuple[int, str], np.ndarray]
        Cached embeddings for each community
    """

    def __init__(
        self,
        embedding_model_name: str = "all-MiniLM-L6-v2",
        min_resolution: float = 0.1,
        max_resolution: float = 2.0,
        n_resolutions: int = 10,
        methods: list[CommunityMethod] | None = None,
        random_state: int | None = None,
    ):
        self.model = SentenceTransformer(embedding_model_name)
        self.min_resolution = min_resolution
        self.max_resolution = max_resolution
        self.n_resolutions = n_resolutions
        self.methods = methods
        self.random_state = random_state

        self.detector = None
        self.community_embeddings = {}

    def fit(self, graph: nx.Graph) -> None:
        """Detect communities and compute their embeddings.

        Parameters
        ----------
        graph : nx.Graph
            Input graph to analyze
        """
        self.detector = MultiResolutionDetector(
            graph,
            min_resolution=self.min_resolution,
            max_resolution=self.max_resolution,
            n_resolutions=self.n_resolutions,
            methods=self.methods,
            random_state=self.random_state,
        )
        consensus = self.detector.detect_communities()

        hierarchy = self.detector.get_hierarchical_relationships()

        for level, comm_id in hierarchy:
            # get community nodes
            community = consensus.hierarchical_levels[level][int(comm_id.split("_")[1])]

            # create community description from node attr
            desc = self._get_community_description(graph, community)

            self.community_embeddings[(level, comm_id)] = self.model.encode(desc)

    def _get_community_description(self, graph: nx.Graph, nodes: set[str]) -> str:
        """Generate a text description of a community from node attributes.

        Parameters
        ----------
        graph : nx.Graph
            The input graph
        nodes : Set[str]
            Set of node IDs in the community

        Returns
        -------
        str
            Text description of the community
        """
        descriptions = []
        for node in nodes:
            node_data = graph.nodes[node]
            desc_parts = []

            if "label" in node_data:
                desc_parts.append(str(node_data["label"]))
            if "description" in node_data:
                desc_parts.append(str(node_data["description"]))
            if "type" in node_data:
                desc_parts.append(f"Type: {node_data['type']}")

            if desc_parts:
                descriptions.append(" ".join(desc_parts))

        if descriptions:
            return " ".join(descriptions)
        return " ".join(nodes)  # fallback to node IDs

    def find_similar_communities(
        self, query: str, n_communities: int = 5, min_similarity: float = 0.5
    ) -> list[tuple[tuple[int, str], float]]:
        """Find the most semantically similar communities to a query.

        Parameters
        ----------
        query : str
            Input query text
        n_communities : int
            Maximum number of communities to return
        min_similarity : float
            Minimum cosine similarity threshold

        Returns
        -------
        List[Tuple[Tuple[int, str], float]]
            List of (community_id, similarity_score) pairs, sorted by similarity
        """
        if not self.detector:
            raise ValueError("Must call fit() before finding similar communities")

        query_embedding = self.model.encode(query, convert_to_numpy=True)

        # compute similarities with all communities
        similarities = []
        for comm_id, comm_embedding in self.community_embeddings.items():
            sim = cosine_similarity(
                query_embedding.reshape(1, -1), comm_embedding.reshape(1, -1)
            )[0][0]
            if sim >= min_similarity:
                similarities.append((comm_id, sim))

        similarities.sort(key=lambda x: x[1], reverse=True)

        return similarities[:n_communities]

    def get_community_nodes(self, community_id: tuple[int, str]) -> set[str]:
        """Get the nodes belonging to a community.

        Parameters
        ----------
        community_id : Tuple[int, str]
            The (level, community_id) identifier

        Returns
        -------
        Set[str]
            Set of node IDs in the community
        """
        if not self.detector:
            raise ValueError("Must call fit() before getting community nodes")

        level, comm_id = community_id
        community_idx = int(comm_id.split("_")[1])
        return self.detector.consensus.hierarchical_levels[level][community_idx]
