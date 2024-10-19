import logging
from unittest.mock import Mock, patch

import networkx as nx
import numpy as np
import pytest

from nxlu.io import load_algorithm_encyclopedia
from nxlu.processing.analyze import (
    GraphProperties,
    apply_algorithm,
    filter_relevant_nodes,
    get_algorithm_function,
    map_algorithm_result,
    register_custom_algorithm,
)
from nxlu.utils.misc import normalize_name, parse_algorithms

algorithm_encyclopedia = load_algorithm_encyclopedia()

SUPPORTED_ALGORITHMS, ALGORITHM_CATEGORIES, STANDARDIZED_ALGORITHM_NAMES = (
    parse_algorithms(algorithm_encyclopedia, normalize_name)
)


@pytest.fixture
def algorithm_encyclopedia_fixture():
    """Load the algorithm encyclopedia."""
    return algorithm_encyclopedia


@pytest.fixture
def simple_graph():
    G = nx.Graph()
    G.add_nodes_from([1, 2, 3])
    G.add_edges_from([(1, 2), (2, 3)])
    return G


@pytest.fixture
def multi_graph_with_edge_attrs():
    G = nx.MultiGraph()
    G.add_nodes_from([1, 2, 3])
    G.add_edges_from(
        [
            (1, 2, {"weight": 1.0}),
            (1, 2, {"weight": 1.5}),
            (2, 3, {"weight": 2.0}),
        ]
    )
    return G


@pytest.fixture
def empty_graph():
    G = nx.Graph()
    return G


@pytest.fixture
def directed_dag():
    G = nx.DiGraph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])
    return G


@pytest.fixture
def tree_graph():
    G = nx.DiGraph()
    G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5)])
    return G


@pytest.fixture
def large_graph():
    G = nx.gnm_random_graph(100, 1000)
    while not nx.is_connected(G):
        G = nx.gnm_random_graph(100, 1000)

    zero_degree_nodes = [n for n, d in G.degree() if d == 0]
    G.remove_nodes_from(zero_degree_nodes)
    return G


ALGORITHM_FIXTURE_MAPPING = {
    "rich_club_coefficient": "large_graph",
    "katz_centrality": "directed_dag",
    "all_node_cuts": "large_graph",
    "all_pairs_lowest_common_ancestor": "tree_graph",
}


def get_fixture_for_algorithm(algorithm_name):
    """Retrieve the appropriate fixture name for a given algorithm."""
    return ALGORITHM_FIXTURE_MAPPING.get(algorithm_name, "simple_graph")


def test_map_algorithm_result_node_attributes(simple_graph):
    """Test mapping algorithm results to node attributes."""
    algorithm = "test_algorithm"
    result = {1: 0.5, 2: 0.7, 3: 0.9}
    map_algorithm_result(simple_graph, algorithm, result)

    for node_id, attrs in simple_graph.nodes(data=True):
        assert "algorithm_results" in attrs
        assert algorithm in attrs["algorithm_results"]
        assert attrs["algorithm_results"][algorithm] == result[node_id]


def test_map_algorithm_result_edge_attributes(multi_graph_with_edge_attrs):
    """Test mapping algorithm results to edge attributes in a MultiGraph."""
    algorithm = "test_algorithm"
    result = {(1, 2): 0.5, (2, 3): 0.7}

    map_algorithm_result(multi_graph_with_edge_attrs, algorithm, result)

    for u, v, _key, attrs in multi_graph_with_edge_attrs.edges(keys=True, data=True):
        edge_key = (u, v)
        if edge_key in result:
            assert "algorithm_results" in attrs
            assert algorithm in attrs["algorithm_results"]
            # Compare with the expected value
            assert attrs["algorithm_results"][algorithm] == result[edge_key]


def test_map_algorithm_result_scalar_attribute(simple_graph):
    """Test mapping a scalar result to graph-level attributes."""
    algorithm = "test_algorithm"
    result = 42  # scalar result

    map_algorithm_result(simple_graph, algorithm, result)

    assert "algorithm_results" in simple_graph.graph
    assert algorithm in simple_graph.graph["algorithm_results"]
    assert simple_graph.graph["algorithm_results"][algorithm] == result


def test_map_algorithm_result_list_of_edges(multi_graph_with_edge_attrs):
    """Test mapping a list of edges to edge attributes in a MultiGraph."""
    algorithm = "test_algorithm"
    result = [(1, 2), (2, 3)]  # list of edges

    map_algorithm_result(multi_graph_with_edge_attrs, algorithm, result)

    for u, v in result:
        if multi_graph_with_edge_attrs.has_edge(u, v):
            for key in multi_graph_with_edge_attrs[u][v]:
                attrs = multi_graph_with_edge_attrs.edges[u, v, key]
                assert "algorithm_results" in attrs
                assert algorithm in attrs["algorithm_results"]
                assert attrs["algorithm_results"][algorithm] is True


def test_map_algorithm_result_unhandled_type(simple_graph, caplog):
    """Test handling of unhandled result types."""
    algorithm = "test_algorithm"
    result = {1, 2, 3}

    with caplog.at_level(logging.WARNING):
        map_algorithm_result(simple_graph, algorithm, result)

    # Check that a warning was logged
    assert any("Unhandled result type" in record.message for record in caplog.records)


@pytest.mark.parametrize("algorithm_name", SUPPORTED_ALGORITHMS)
def test_get_algorithm_function_builtin(algorithm_name):
    """Test retrieving a built-in NetworkX algorithm."""
    algorithm_func = get_algorithm_function(algorithm_name)
    assert callable(algorithm_func)
    if algorithm_name == "load_centrality":
        assert algorithm_func.__name__ == "newman_betweenness_centrality"
    else:
        assert algorithm_func.__name__ == algorithm_name


def test_get_algorithm_function_custom():
    """Test retrieving a custom algorithm using patch.dict."""
    algorithm_name = "custom_algo"

    with patch.dict(
        "nxlu.processing.analyze.CUSTOM_ALGORITHMS", {algorithm_name: lambda x: x}
    ):
        algorithm_func = get_algorithm_function(algorithm_name)
        assert callable(algorithm_func)
        assert algorithm_func("test") == "test"  # Verify functionality


def test_get_algorithm_function_not_found():
    """Test retrieving a non-existent algorithm raises ValueError."""
    algorithm_name = "non_existent_algorithm"

    with pytest.raises(ValueError, match=f"Algorithm '{algorithm_name}' not found."):
        get_algorithm_function(algorithm_name)


def test_apply_algorithm_builtin(simple_graph):
    """Test applying a built-in algorithm."""
    algorithm_name = "degree_centrality"

    result = apply_algorithm(algorithm_encyclopedia, simple_graph, algorithm_name)

    assert isinstance(result, dict)
    assert set(result.keys()) == set(simple_graph.nodes())

    # Correct degree centrality values:
    # For nodes 1 and 3: degree = 1, centrality = 1 / (3 - 1) = 0.5
    # For node 2: degree = 2, centrality = 2 / (3 - 1) = 1.0
    assert result[1] == pytest.approx(0.5)
    assert result[2] == pytest.approx(1.0)
    assert result[3] == pytest.approx(0.5)


def test_apply_algorithm_custom(simple_graph):
    """Test applying a custom algorithm."""
    algorithm_name = "custom_algo"

    def custom_algo(G):
        return "custom_result"

    with patch.dict("nxlu.constants.CUSTOM_ALGORITHMS", {algorithm_name: custom_algo}):
        result = apply_algorithm(algorithm_encyclopedia, simple_graph, algorithm_name)
        assert result == "custom_result"


@pytest.mark.parametrize("algorithm_name", SUPPORTED_ALGORITHMS)
def test_apply_algorithm(request, algorithm_name, algorithm_encyclopedia_fixture):
    """Test applying various algorithms to appropriate graphs."""
    fixture_name = get_fixture_for_algorithm(algorithm_name)

    if fixture_name is None:
        pytest.skip(f"No fixture available for algorithm '{algorithm_name}'")

    graph = request.getfixturevalue(fixture_name)

    # Some algorithms might modify the graph; ensure a copy is used
    graph_copy = graph.copy()

    try:
        result = apply_algorithm(
            algorithm_encyclopedia_fixture, graph_copy, algorithm_name
        )
        assert result is not None
    except ValueError as ve:
        pytest.fail(f"Test failed for algorithm '{algorithm_name}': {ve}")


def test_apply_algorithm_with_k_parameter(simple_graph):
    """Test applying an algorithm with the 'k' parameter."""
    algorithm_name = "k_core"

    # Test with default k=100, should return empty graph
    result = apply_algorithm(algorithm_encyclopedia, simple_graph, algorithm_name)

    assert isinstance(result, nx.Graph)
    assert result.number_of_nodes() == 0  # No nodes have degree >=100

    # Test with k=1
    result = apply_algorithm(algorithm_encyclopedia, simple_graph, algorithm_name, k=1)

    assert isinstance(result, nx.Graph)
    assert result.number_of_nodes() == 3  # All nodes have degree >=1


def test_apply_algorithm_with_weight_parameter(multi_graph_with_edge_attrs):
    """Test applying an algorithm that utilizes edge weights."""
    algorithm_name = "pagerank"
    result = apply_algorithm(
        algorithm_encyclopedia, multi_graph_with_edge_attrs, algorithm_name
    )

    assert isinstance(result, dict)
    assert set(result.keys()) == set(multi_graph_with_edge_attrs.nodes())
    assert all(isinstance(score, float) for score in result.values())


def test_register_custom_algorithm():
    """Test registering and applying a custom algorithm."""

    def custom_algorithm(G):
        return "custom_result"

    register_custom_algorithm("my_custom_algo", custom_algorithm)

    # Now retrieve the algorithm
    algorithm_func = get_algorithm_function("my_custom_algo")
    assert algorithm_func == custom_algorithm

    # Apply the algorithm
    G = nx.Graph()
    G.add_node(1)
    result = apply_algorithm(algorithm_encyclopedia, G, "my_custom_algo")
    assert result == "custom_result"


def test_graph_properties(simple_graph):
    """Test the GraphProperties class for correct attribute computation."""
    props = GraphProperties(simple_graph)

    assert props.num_nodes == simple_graph.number_of_nodes()
    assert props.num_edges == simple_graph.number_of_edges()
    assert props.is_directed == simple_graph.is_directed()
    assert props.density == nx.density(simple_graph)
    assert props.is_connected == nx.is_connected(simple_graph)
    assert props.is_weighted == nx.is_weighted(simple_graph)
    assert props.is_multigraph == simple_graph.is_multigraph()

    degrees = [d for n, d in simple_graph.degree()]
    assert props.min_degree == min(degrees)
    assert props.max_degree == max(degrees)
    assert props.avg_degree == sum(degrees) / len(degrees)


def test_graph_properties_identify_hits():
    """Test the identification of hubs and authorities in a directed graph."""
    # For hubs and authorities, let's use a small directed graph
    G = nx.DiGraph()
    edges = [(1, 2), (2, 3), (2, 4), (3, 1)]
    G.add_edges_from(edges)

    props = GraphProperties(G, z_threshold=0.5)

    # Now hubs and authorities should be identified
    assert isinstance(props.hubs, list)
    assert isinstance(props.authorities, list)

    # Verify expected hub
    assert 2 in props.hubs

    # Verify at least one expected authority
    assert 4 in props.authorities


def test_filter_relevant_nodes():
    """Test filtering relevant nodes based on qsimilarity with lower z_threshold."""
    nodes = ["node1", "node2", "node3"]
    query = "node2"

    # Mock SentenceTransformer and cosine_similarity
    with (
        patch("sentence_transformers.SentenceTransformer") as mock_model_cls,
        patch("nxlu.processing.analyze.cosine_similarity") as mock_cosine_similarity,
    ):
        mock_model = Mock()
        mock_model_cls.return_value = mock_model

        # Mock the embeddings
        def mock_encode(x):
            # Return embeddings that will result in desired similarities
            embeddings = np.array([[0.1], [0.5], [0.9]])
            return embeddings[: len(x)]

        mock_model.encode.side_effect = mock_encode

        # Mock cosine_similarity to return predefined similarities
        mock_cosine_similarity.side_effect = lambda a, b: np.array([0.1, 0.5, 0.9])

        # Use a lower z_threshold to allow node3 to be selected
        relevant_nodes = filter_relevant_nodes(
            nodes, query, mock_model, z_threshold=0.5
        )

        assert relevant_nodes == ["node3"]


def test_filter_relevant_nodes_empty():
    """Test filtering when the node list is empty."""
    nodes = []
    query = "node"

    model = Mock()

    relevant_nodes = filter_relevant_nodes(nodes, query, model)

    assert relevant_nodes == []


def test_filter_relevant_nodes_no_relevant():
    """Test filtering when no nodes meet the similarity threshold."""
    nodes = ["node1", "node2", "node3"]
    query = "unrelated query"

    with (
        patch("sentence_transformers.SentenceTransformer") as mock_model_cls,
        patch("nxlu.utils.misc.cosine_similarity") as mock_cosine_similarity,
    ):
        mock_model = Mock()
        mock_model_cls.return_value = mock_model

        # Mock the embeddings
        def mock_encode(x):
            # Return embeddings that will result in low similarity
            return np.zeros((len(x), 1))

        mock_model.encode.side_effect = mock_encode

        # Mock cosine_similarity to return low similarities
        mock_cosine_similarity.return_value = np.array([0.1, 0.1, 0.1])

        relevant_nodes = filter_relevant_nodes(nodes, query, mock_model)

        assert relevant_nodes == []


def test_map_algorithm_result_non_multigraph(simple_graph):
    """Test mapping a list of edges in a simple Graph (should handle gracefully)."""
    algorithm = "test_algorithm"
    result = [(1, 2), (2, 3)]  # list of edges

    map_algorithm_result(simple_graph, algorithm, result)

    # Verify that 'algorithm_results' is set for each edge
    for u, v in result:
        attrs = simple_graph.edges[u, v]
        assert "algorithm_results" in attrs
        assert algorithm in attrs["algorithm_results"]
        assert attrs["algorithm_results"][algorithm] is True
