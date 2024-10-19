import statistics
from collections import defaultdict
from unittest.mock import Mock, create_autospec, patch

import networkx as nx
import pytest

from nxlu.processing.analyze import GraphProperties
from nxlu.processing.summarize import characterize_graph, format_algorithm_results


@pytest.fixture
def fully_connected_graph():
    G = nx.complete_graph(5)
    nx.set_node_attributes(G, {n: f"Label_{n}" for n in G.nodes()}, "label")
    nx.set_edge_attributes(
        G, {edge: "relationship_type" for edge in G.edges()}, "relationship"
    )
    return G


@pytest.fixture
def partially_connected_graph():
    G = nx.Graph()
    edges = [(0, 1), (1, 2), (3, 4)]
    G.add_edges_from(edges)
    nx.set_node_attributes(G, {n: f"Label_{n}" for n in G.nodes()}, "label")
    nx.set_edge_attributes(
        G, {edge: "relationship_type" for edge in G.edges()}, "relationship"
    )
    return G


@pytest.fixture
def disconnected_graph():
    G = nx.Graph()
    G.add_nodes_from([0, 1, 2, 3, 4])
    nx.set_node_attributes(G, {n: f"Label_{n}" for n in G.nodes()}, "label")
    return G


@pytest.fixture
def weighted_graph():
    G = nx.Graph()
    edges = [(0, 1, 0.5), (1, 2, 0.7), (2, 3, 0.2)]
    G.add_weighted_edges_from(edges)
    nx.set_node_attributes(G, {n: f"Label_{n}" for n in G.nodes()}, "label")
    nx.set_edge_attributes(
        G,
        {edge[:2]: "weighted_relationship" for edge in G.edges(data=True)},
        "relationship",
    )
    return G


@pytest.fixture
def binary_graph():
    G = nx.Graph()
    edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
    G.add_edges_from(edges)
    nx.set_node_attributes(G, {n: f"Label_{n}" for n in G.nodes()}, "label")
    nx.set_edge_attributes(
        G, {edge: "binary_relationship" for edge in G.edges()}, "relationship"
    )
    return G


@pytest.fixture(
    params=[
        "fully_connected_graph",
        "partially_connected_graph",
        "disconnected_graph",
        "weighted_graph",
        "binary_graph",
    ]
)
def varied_graph(
    request,
    fully_connected_graph,
    partially_connected_graph,
    disconnected_graph,
    weighted_graph,
    binary_graph,
):
    graph = request.getfixturevalue(request.param)
    graph.graph["name"] = request.param
    return graph


@pytest.fixture
def graph_properties(varied_graph):
    """Create a mock of GraphProperties using create_autospec."""
    num_nodes = varied_graph.number_of_nodes()
    num_edges = varied_graph.number_of_edges()
    is_directed = varied_graph.is_directed()
    is_multigraph = isinstance(varied_graph, nx.MultiGraph)
    is_bipartite = nx.is_bipartite(varied_graph)
    is_weighted = nx.is_weighted(varied_graph)
    is_tree = nx.is_tree(varied_graph)
    is_planar = nx.check_planarity(varied_graph)[0]
    is_strongly_connected = (
        nx.is_strongly_connected(varied_graph) if is_directed else False
    )
    is_connected = nx.is_connected(varied_graph) if not is_directed else False
    average_clustering = nx.average_clustering(varied_graph) if num_nodes > 0 else 0.0
    density = nx.density(varied_graph)

    degree_hist = defaultdict(int)
    degrees = dict(varied_graph.degree()).values()
    for degree in degrees:
        degree_hist[degree] += 1

    if degree_hist:
        peak_degree = max(degree_hist, key=lambda k: degree_hist[k])
        max_degree = max(degree_hist.keys())
        min_degree = min(degree_hist.keys())
        avg_degree = (
            sum(k * v for k, v in degree_hist.items()) / num_nodes
            if num_nodes > 0
            else 0.0
        )
    else:
        peak_degree = 0
        max_degree = 0
        min_degree = 0
        avg_degree = 0.0

    hubs = ["Hub1", "Hub2"]
    authorities = ["Authority1"]

    # Create a mock with spec set to GraphProperties
    mock = create_autospec(GraphProperties, instance=True)
    mock.num_nodes = num_nodes
    mock.num_edges = num_edges
    mock.is_directed = is_directed
    mock.is_multigraph = is_multigraph
    mock.is_bipartite = is_bipartite
    mock.is_weighted = is_weighted
    mock.is_tree = is_tree
    mock.is_planar = is_planar
    mock.is_strongly_connected = is_strongly_connected
    mock.is_connected = is_connected
    mock.average_clustering = average_clustering
    mock.density = density
    mock.degree_hist = degree_hist
    mock.peak_degree = peak_degree
    mock.max_degree = max_degree
    mock.min_degree = min_degree
    mock.avg_degree = avg_degree
    mock.hubs = hubs
    mock.authorities = authorities

    return mock


@pytest.fixture
def mock_logger():
    with patch("nxlu.processing.summarize.logger") as mock_logger:
        yield mock_logger


class TestCharacterizeGraph:
    @pytest.mark.parametrize("detect_domain", [True, False])
    @pytest.mark.parametrize("user_query", [None, "test query"])
    @pytest.mark.parametrize("max_nodes_for_embedding", [0, 1, 50, 100, 150])
    def test_characterize_graph_valid_inputs(
        self,
        varied_graph,
        graph_properties,
        user_query,
        detect_domain,
        max_nodes_for_embedding,
    ):
        with (
            patch("nxlu.processing.summarize.assign_default_weights"),
            patch("nxlu.processing.summarize.classify_domain") as mock_classify_domain,
            patch(
                "nxlu.processing.summarize.filter_relevant_nodes"
            ) as mock_filter_relevant_nodes,
            patch(
                "nxlu.processing.summarize.SentenceTransformer"
            ) as mock_sentence_transformer,
        ):
            # Mock SentenceTransformer instance and its behavior
            mock_st_instance = Mock()
            mock_sentence_transformer.return_value = mock_st_instance

            mock_classify_domain.return_value = "Test Domain"
            mock_filter_relevant_nodes.side_effect = lambda nodes, query, model: (
                nodes if query else []
            )

            summary = characterize_graph(
                graph=varied_graph,
                graph_props=graph_properties,  # Pass valid graph_props
                user_query=user_query,
                detect_domain=detect_domain,
                max_nodes_for_embedding=max_nodes_for_embedding,
            )

            assert isinstance(summary, str)
            assert (
                f"The graph has {graph_properties.num_nodes} nodes and "
                f"{graph_properties.num_edges} edges." in summary
            )

            # Check for node labels
            if varied_graph.nodes:
                unique_node_labels = {
                    attr["label"] for _, attr in varied_graph.nodes(data=True)
                }
                labels_str = ", ".join(unique_node_labels)
                assert f"Nodes represent: {labels_str}." in summary

            # Check for edge labels
            if varied_graph.edges:
                unique_edge_labels = {
                    attr["relationship"] for _, _, attr in varied_graph.edges(data=True)
                }
                edge_labels_str = ", ".join(unique_edge_labels)
                assert f"Edges represent: {edge_labels_str} relationships." in summary

            # Check graph properties
            properties = (
                f"Directed: {graph_properties.is_directed}, "
                f"Multigraph: {graph_properties.is_multigraph}, "
                f"Bipartite: {graph_properties.is_bipartite}, "
                f"Weighted: {graph_properties.is_weighted}, "
                f"Tree: {graph_properties.is_tree}, "
                f"Planar: {graph_properties.is_planar}, "
                f"Strongly Connected: {graph_properties.is_strongly_connected}, "
                f"Connected: {graph_properties.is_connected} (if disconnected, "
                f"preprocessing may force connectedness in some cases, depending on "
                f"the algorithms applied during analysis)."
            )
            assert f"The graph has the following properties: {properties}" in summary

            # Check average clustering and density
            if graph_properties.num_nodes > 0:
                assert (
                    f"It has an average clustering coefficient of "
                    f"{graph_properties.average_clustering:.2f}." in summary
                )
                assert (
                    f"The graph density is {graph_properties.density:.3f}." in summary
                )

            # Check degree distribution
            if graph_properties.degree_hist:
                peak_degree = graph_properties.peak_degree
                peak_count = graph_properties.degree_hist[peak_degree]
                assert (
                    f"It has a degree distribution that peaks at index {peak_degree} "
                    f"on the degree histogram with a degree of {peak_count}." in summary
                )

            truncated_nodes = list(varied_graph.nodes(data=True))[
                :max_nodes_for_embedding
            ]
            truncated_node_set = {n for n, _ in truncated_nodes}

            truncated_edges = [
                (u, v, d)
                for u, v, d in varied_graph.edges(data=True)
                if u in truncated_node_set and v in truncated_node_set
            ]
            edge_labels = nx.get_edge_attributes(varied_graph, "relationship")
            truncated_edge_labels = [
                edge_labels.get((u, v), "unknown") for u, v, _ in truncated_edges
            ]

            expected_input = {
                "nodes": truncated_nodes,
                "edges": truncated_edge_labels,
                "query": user_query,
            }

            if detect_domain:
                mock_classify_domain.assert_called_with(expected_input)
                assert (
                    "The graph likely represents data in the domain of: Test Domain."
                    in summary
                )
            else:
                mock_classify_domain.assert_not_called()
                assert (
                    "The graph likely represents data in the domain of:" not in summary
                )

            # Check relevant hubs and authorities
            if (graph_properties.hubs or graph_properties.authorities) and user_query:
                mock_filter_relevant_nodes.assert_any_call(
                    graph_properties.hubs, user_query, mock_st_instance
                )
                mock_filter_relevant_nodes.assert_any_call(
                    graph_properties.authorities,
                    user_query,
                    mock_st_instance,
                )
                if graph_properties.hubs:
                    hubs_str = ", ".join(graph_properties.hubs)
                    assert f"Identified Network Hubs: {hubs_str}." in summary
                if graph_properties.authorities:
                    authorities_str = ", ".join(graph_properties.authorities)
                    assert (
                        f"Identified Network Authorities: {authorities_str}." in summary
                    )
            else:
                # If no user_query, or no hubs/authorities, no relevant nodes
                mock_filter_relevant_nodes.assert_not_called()

    def test_characterize_graph_empty_graph(self, mock_logger):
        empty_graph = nx.Graph()
        empty_graph.graph["name"] = "empty_graph"

        # Create a mock for graph_properties with spec set to GraphProperties
        mock_graph_properties = create_autospec(GraphProperties, instance=True)
        mock_graph_properties.num_nodes = 0
        mock_graph_properties.num_edges = 0
        mock_graph_properties.is_directed = False
        mock_graph_properties.is_multigraph = False
        mock_graph_properties.is_bipartite = False
        mock_graph_properties.is_weighted = False
        mock_graph_properties.is_tree = False
        mock_graph_properties.is_planar = True  # An empty graph is planar
        mock_graph_properties.is_strongly_connected = False
        mock_graph_properties.is_connected = False  # Empty graph is not connected
        mock_graph_properties.average_clustering = 0.0
        mock_graph_properties.density = 0.0
        mock_graph_properties.degree_hist = {}
        mock_graph_properties.peak_degree = 0
        mock_graph_properties.hubs = []
        mock_graph_properties.authorities = []

        with (
            patch("nxlu.processing.summarize.assign_default_weights"),
            patch("nxlu.processing.summarize.classify_domain") as mock_classify_domain,
            patch(
                "nxlu.processing.summarize.filter_relevant_nodes"
            ) as mock_filter_relevant_nodes,
            patch("nxlu.processing.summarize.SentenceTransformer"),
        ):
            summary = characterize_graph(
                graph=empty_graph,
                graph_props=mock_graph_properties,
                user_query=None,
                detect_domain=False,
                max_nodes_for_embedding=100,
            )

            assert isinstance(summary, str)
            assert "The graph has 0 nodes and 0 edges." in summary
            assert "The graph has the following properties:" in summary
            assert "It has an average clustering coefficient of" not in summary
            assert "The graph density is" not in summary
            assert "It has a degree distribution that peaks at index" not in summary

            mock_classify_domain.assert_not_called()
            mock_filter_relevant_nodes.assert_not_called()

    @pytest.mark.parametrize("invalid_graph", [None, 123, "not_a_graph", {}, []])
    def test_characterize_graph_invalid_graph_input(
        self, invalid_graph, graph_properties
    ):
        with pytest.raises(
            TypeError,
            match="Invalid graph input: 'graph' must be an instance of networkx.Graph.",
        ):
            characterize_graph(graph=invalid_graph, graph_props=graph_properties)

    @pytest.mark.parametrize(
        "invalid_graph_props", [None, "not_graph_props", 123, {}, []]
    )
    def test_characterize_graph_invalid_graph_props(
        self, varied_graph, invalid_graph_props
    ):
        with pytest.raises(
            TypeError,
            match="Invalid graph properties: 'graph_props' must be an instance of "
            "GraphProperties.",
        ):
            characterize_graph(graph=varied_graph, graph_props=invalid_graph_props)

    @pytest.mark.parametrize("detect_domain", [True, False])
    @pytest.mark.parametrize("user_query", [None, "test query"])
    @pytest.mark.parametrize("max_nodes_for_embedding", [0, 1, 50, 100, 150])
    def test_characterize_graph_max_nodes_for_embedding_boundary(
        self,
        varied_graph,
        graph_properties,
        user_query,
        detect_domain,
        max_nodes_for_embedding,
    ):
        with (
            patch("nxlu.processing.summarize.assign_default_weights"),
            patch("nxlu.processing.summarize.classify_domain") as mock_classify_domain,
            patch(
                "nxlu.processing.summarize.filter_relevant_nodes"
            ) as mock_filter_relevant_nodes,
            patch(
                "nxlu.processing.summarize.SentenceTransformer"
            ) as mock_sentence_transformer,
        ):
            # Mock SentenceTransformer instance and its behavior
            mock_st_instance = Mock()
            mock_sentence_transformer.return_value = mock_st_instance

            mock_classify_domain.return_value = "Test Domain"
            mock_filter_relevant_nodes.side_effect = lambda nodes, query, model: (
                nodes if query else []
            )

            summary = characterize_graph(
                graph=varied_graph,
                graph_props=graph_properties,
                user_query=user_query,
                detect_domain=detect_domain,
                max_nodes_for_embedding=max_nodes_for_embedding,
            )

            truncated_nodes = list(varied_graph.nodes(data=True))[
                :max_nodes_for_embedding
            ]
            truncated_node_set = {n for n, _ in truncated_nodes}

            truncated_edges = [
                (u, v, d)
                for u, v, d in varied_graph.edges(data=True)
                if u in truncated_node_set and v in truncated_node_set
            ]
            edge_labels = nx.get_edge_attributes(varied_graph, "relationship")
            truncated_edge_labels = [
                edge_labels.get((u, v), "unknown") for u, v, _ in truncated_edges
            ]

            expected_input = {
                "nodes": truncated_nodes,
                "edges": truncated_edge_labels,
                "query": user_query,
            }

            if detect_domain:
                mock_classify_domain.assert_called_with(expected_input)
                assert (
                    "The graph likely represents data in the domain of: Test Domain."
                    in summary
                )
            else:
                mock_classify_domain.assert_not_called()
                assert (
                    "The graph likely represents data in the domain of:" not in summary
                )


class TestFormatAlgorithmResults:
    @pytest.fixture
    def valid_results(self):
        return [
            ("algorithm_one", {"node1": 0.5, "node2": 0.7}),
            ("algorithm_two", {"edge1-edge2": 1.0, "edge3-edge4": 0.0}),
            ("algorithm_three", 123.456),
            ("algorithm_four", [("node1", "node2"), ("node3", "node4")]),
            ("algorithm_five", {"metric1": 1e11, "metric2": 1e-5}),
        ]

    def test_format_algorithm_results_valid(self, valid_results, mock_logger):
        formatted = format_algorithm_results(valid_results)
        assert isinstance(formatted, str)
        assert "**Graph-Level Results:**" in formatted
        assert "- **Algorithm Three**: 123.456" in formatted
        # '0.0' should not be present as algorithm_two is excluded
        assert "0.0" not in formatted
        assert "**Node-Specific Results:**" in formatted
        assert "- **Algorithm One**:" in formatted
        assert "- **Algorithm Five**:" in formatted
        # Edge-Specific Results should include algorithm_four
        assert "**Edge-Specific Results:**" in formatted
        assert "- **Algorithm Four**:" in formatted

    def test_format_algorithm_results_empty(self):
        formatted = format_algorithm_results([])
        assert isinstance(formatted, str)
        assert formatted == ""

    @pytest.mark.parametrize(
        "invalid_results",
        [
            None,
            "not_a_list",
            123,
            {"algorithm": "result"},
            [("only_one_element",)],
            [("too", "many", "elements")],
            [("valid", "result"), "invalid_item"],
        ],
    )
    def test_format_algorithm_results_invalid_inputs(
        self, invalid_results, mock_logger
    ):
        if not isinstance(invalid_results, list):
            with pytest.raises(TypeError, match="`results` should be a list of tuples"):
                format_algorithm_results(invalid_results)
        else:
            with pytest.raises(
                TypeError,
                match=(
                    r"Each item in `results` should be a tuple of \(algorithm_name, "
                    r"result_data\)."
                ),
            ):
                format_algorithm_results(invalid_results)

    def test_format_algorithm_results_exclude_algorithms(self, mock_logger):
        results = [
            ("alg_one", {"node1": 0.0, "node2": 1.0}),
            ("alg_two", {"edge1-edge2": 0.0, "edge3-edge4": 1.0}),
            ("alg_three", {"metric1": 0.0, "metric2": 1.0}),
        ]
        formatted = format_algorithm_results(results)
        assert formatted.strip() == ""
        mock_logger.info.assert_any_call(
            "Excluding algorithm 'alg_one' as all values are 0.0 or 1.0."
        )
        mock_logger.info.assert_any_call(
            "Excluding algorithm 'alg_two' as all values are 0.0 or 1.0."
        )
        mock_logger.info.assert_any_call(
            "Excluding algorithm 'alg_three' as all values are 0.0 or 1.0."
        )

    def test_format_algorithm_results_mode_error(self, mock_logger):
        # Mode is not unique
        results = [
            ("alg_numeric", {"node1": 1.0, "node2": 2.0, "node3": 2.0, "node4": 1.0}),
        ]
        with patch("statistics.mode", side_effect=statistics.StatisticsError):
            formatted = format_algorithm_results(results)
            assert "Mode: N/A" in formatted

    def test_format_algorithm_results_non_numeric_values(self):
        results = [
            ("alg_strings", {"node1": "A", "node2": "B", "node3": "A"}),
            ("alg_sets", [{"a", "b"}, {"c", "d"}]),
        ]
        formatted = format_algorithm_results(results)
        assert "**Graph-Level Results:**" not in formatted
        assert "**Node-Specific Results:**" not in formatted
        assert "**Edge-Specific Results:**" in formatted
        assert "- **Alg Sets**:" in formatted
        # Check for both possible orders
        assert "['a', 'b']" in formatted or "['b', 'a']" in formatted
        assert "['c', 'd']" in formatted or "['d', 'c']" in formatted

    def test_format_algorithm_results_large_small_numbers(self):
        results = [
            ("alg_large", 1e12),
            ("alg_small", 1e-6),
            ("alg_normal", 123.456789),
        ]
        formatted = format_algorithm_results(results)
        assert "**Graph-Level Results:**" in formatted
        assert "- **Alg Large**: 1000000000000" in formatted
        assert "- **Alg Small**: 0" in formatted
        assert "- **Alg Normal**: 123.4568" in formatted

    def test_format_algorithm_results_mixed_results(self):
        results = [
            ("alg_graph", 42),
            ("alg_nodes", {"node1": 1.0, "node2": 2.0, "node3": 3.0}),
            ("alg_edges", {"edge1-edge2": 0.5, "edge3-edge4": 1.5}),
            ("alg_list", [("node1", "node2"), ("node3", "node4")]),
        ]
        formatted = format_algorithm_results(results)
        assert "**Graph-Level Results:**" in formatted
        assert "- **Alg Graph**: 42" in formatted
        assert "**Node-Specific Results:**" in formatted
        assert "- **Alg Nodes**:" in formatted
        # Accept both '2' and '2.0'
        assert "  - Average: 2" in formatted or "  - Average: 2.0" in formatted
        assert (
            "  - Median: 2" in formatted or "  - Median: 2.0" in formatted
        )  # Adjust assertion
        assert "  - Mode: 1" in formatted
        assert "  - Std Dev: 1" in formatted
        assert "**Edge-Specific Results:**" in formatted
        assert "- **Alg Edges**:" in formatted
        assert "  - Average: 1" in formatted
        assert "  - Median: 1" in formatted
        assert "  - Mode: 0.5" in formatted
        assert "  - Std Dev: 0.7071" in formatted
