import networkx as nx
import numpy as np
import pytest

from nxlu.processing.preprocess import (
    CleanGraph,
    CleanGraphConfig,
    GraphRescaling,
    GraphRescalingConfig,
    GraphThresholding,
    GraphThresholdingConfig,
    SubgraphSelection,
    SubgraphSelectionConfig,
    is_symmetric,
    remove_self_loops,
    symmetrize_graph,
)


@pytest.fixture
def example_clean_graph_config():
    return CleanGraphConfig(
        force_symmetry=True,
        remove_self_loops=True,
        threshold=GraphThresholdingConfig(method="absolute", value=0.3),
        subgraph=SubgraphSelectionConfig(
            defragment=True, prune_components=True, min_nodes=2
        ),
        rescale=None,
    )


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
def fully_connected_graph():
    return nx.complete_graph(5)


@pytest.fixture
def partially_connected_graph():
    G = nx.Graph()
    edges = [(0, 1), (1, 2), (3, 4)]
    G.add_edges_from(edges)
    return G


@pytest.fixture
def disconnected_graph():
    G = nx.Graph()
    G.add_nodes_from([0, 1, 2, 3, 4])
    return G


@pytest.fixture
def weighted_graph():
    G = nx.Graph()
    edges = [(0, 1, 0.5), (1, 2, 0.7), (2, 3, 0.2)]
    G.add_weighted_edges_from(edges)
    return G


@pytest.fixture
def binary_graph():
    G = nx.Graph()
    edges = [(0, 1), (1, 2), (2, 3), (3, 4)]
    G.add_edges_from(edges)
    return G


@pytest.mark.parametrize(
    ("graph_fixture_name", "config", "expected_node_count"),
    [
        (
            "fully_connected_graph",
            SubgraphSelectionConfig(
                defragment=True, prune_components=False, use_lcc=False
            ),
            5,
        ),
        (
            "fully_connected_graph",
            SubgraphSelectionConfig(
                defragment=False, prune_components=True, min_nodes=2
            ),
            5,
        ),
        (
            "fully_connected_graph",
            SubgraphSelectionConfig(
                defragment=True, prune_components=True, min_nodes=2, use_lcc=True
            ),
            5,
        ),
        # For partially_connected_graph
        (
            "partially_connected_graph",
            SubgraphSelectionConfig(
                defragment=True, prune_components=False, use_lcc=False
            ),
            5,
        ),
        (
            "partially_connected_graph",
            SubgraphSelectionConfig(
                defragment=False, prune_components=True, min_nodes=2
            ),
            5,
        ),
        (
            "partially_connected_graph",
            SubgraphSelectionConfig(
                defragment=True, prune_components=True, min_nodes=2, use_lcc=True
            ),
            3,
        ),
        # For disconnected_graph
        (
            "disconnected_graph",
            SubgraphSelectionConfig(
                defragment=True, prune_components=False, use_lcc=False
            ),
            0,
        ),
        (
            "disconnected_graph",
            SubgraphSelectionConfig(
                defragment=False, prune_components=True, min_nodes=2
            ),
            0,
        ),
        (
            "disconnected_graph",
            SubgraphSelectionConfig(
                defragment=True, prune_components=True, min_nodes=2, use_lcc=True
            ),
            0,
        ),
        # For weighted_graph
        (
            "weighted_graph",
            SubgraphSelectionConfig(
                defragment=True, prune_components=False, use_lcc=False
            ),
            4,
        ),
        (
            "weighted_graph",
            SubgraphSelectionConfig(
                defragment=False, prune_components=True, min_nodes=2
            ),
            4,
        ),
        (
            "weighted_graph",
            SubgraphSelectionConfig(
                defragment=True, prune_components=True, min_nodes=2, use_lcc=True
            ),
            4,
        ),
        # For binary_graph
        (
            "binary_graph",
            SubgraphSelectionConfig(
                defragment=True, prune_components=False, use_lcc=False
            ),
            5,
        ),
        (
            "binary_graph",
            SubgraphSelectionConfig(
                defragment=False, prune_components=True, min_nodes=2
            ),
            5,
        ),
        (
            "binary_graph",
            SubgraphSelectionConfig(
                defragment=True, prune_components=True, min_nodes=2, use_lcc=True
            ),
            5,
        ),
    ],
)
def test_subgraph_selection_apply(
    request, graph_fixture_name, config, expected_node_count
):
    varied_graph = request.getfixturevalue(graph_fixture_name)
    selector = SubgraphSelection(config)
    result = selector.apply(varied_graph)
    assert isinstance(result, nx.Graph)
    assert result.number_of_nodes() == expected_node_count


@pytest.mark.parametrize(
    ("method", "value"),
    [
        ("absolute", 0.3),
        ("proportional", 0.5),
        ("MST", 0.3),
    ],
)
def test_graph_thresholding_apply(varied_graph, method, value):
    config = GraphThresholdingConfig(method=method, value=value)
    thresholder = GraphThresholding(config)
    matrix = nx.to_numpy_array(varied_graph)
    expected_shape = matrix.shape
    result = thresholder.apply(matrix)
    assert isinstance(result, np.ndarray)
    assert result.shape == expected_shape


@pytest.mark.parametrize(
    "rescaling_method",
    [
        "normalize",
        "standardize",
        "invert",
    ],
)
def test_graph_rescaling_apply(varied_graph, rescaling_method):
    config = GraphRescalingConfig(method=rescaling_method)
    rescaler = GraphRescaling(config)
    matrix = nx.to_numpy_array(varied_graph)
    result = rescaler.apply(matrix)
    assert isinstance(result, np.ndarray)

    if rescaling_method in ["normalize", "standardize"]:
        max_val = np.max(np.abs(matrix))
        if max_val > 1e-12:
            expected_max = 1.0
        else:
            expected_max = 0.0
    elif rescaling_method == "invert":
        nonzero_weights = matrix[matrix != 0]
        if nonzero_weights.size > 0:
            min_nonzero_weight = np.min(np.abs(nonzero_weights))
            expected_max = 1.0 / min_nonzero_weight
        else:
            expected_max = 0.0
    else:
        expected_max = None

    np.testing.assert_almost_equal(np.max(result), expected_max, decimal=3)


@pytest.mark.parametrize(
    "config",
    [
        CleanGraphConfig(
            prune=2,
            norm=1,
            force_symmetry=True,
            remove_self_loops=True,
            threshold=GraphThresholdingConfig(method="absolute", value=0.3),
            subgraph=SubgraphSelectionConfig(
                defragment=True, prune_components=True, min_nodes=2
            ),
        ),
        CleanGraphConfig(
            prune=2,
            norm=1,
            force_symmetry=False,
            remove_self_loops=False,
            threshold=GraphThresholdingConfig(method="proportional", value=0.5),
            subgraph=SubgraphSelectionConfig(
                defragment=False, prune_components=False, use_lcc=True
            ),
        ),
    ],
)
def test_clean_graph(varied_graph, config):
    cleaner = CleanGraph(varied_graph, config)
    G_cleaned = cleaner.clean()
    assert isinstance(G_cleaned, nx.Graph)
    assert G_cleaned.number_of_nodes() > 0


@pytest.mark.parametrize(
    ("k", "graph_fixture_name"),
    [
        (1, "fully_connected_graph"),
        (2, "fully_connected_graph"),
        (3, "fully_connected_graph"),
        (1, "partially_connected_graph"),
        (2, "partially_connected_graph"),
        (3, "partially_connected_graph"),
        (1, "disconnected_graph"),
        (2, "disconnected_graph"),
        (3, "disconnected_graph"),
        (1, "weighted_graph"),
        (2, "weighted_graph"),
        (3, "weighted_graph"),
        (1, "binary_graph"),
        (2, "binary_graph"),
        (3, "binary_graph"),
    ],
)
def test_knn_graph_dynamic(
    request,
    graph_fixture_name,
    k,
    example_clean_graph_config,
):
    varied_graph = request.getfixturevalue(graph_fixture_name)
    cleaner = CleanGraph(varied_graph, example_clean_graph_config)
    k_graph = cleaner.knn_graph(k)

    assert isinstance(
        k_graph, nx.Graph
    ), f"k={k}, graph={graph_fixture_name}: Result is not a NetworkX Graph."

    # Check that no node has more than k connections
    for node in k_graph.nodes():
        degree = k_graph.degree(node)
        assert (
            degree <= k
        ), f"k={k}, graph={graph_fixture_name}: Node {node} has degree {degree} "

    # If using LCC, ensure the graph is connected
    if (
        example_clean_graph_config.subgraph
        and example_clean_graph_config.subgraph.use_lcc
    ):
        if k_graph.number_of_nodes() > 0:
            assert nx.is_connected(
                k_graph
            ), f"k={k}, graph={graph_fixture_name}: Graph is not connected."


def test_remove_self_loops(varied_graph):
    # Add self-loops to the varied_graph
    varied_graph.add_edges_from([(n, n) for n in varied_graph.nodes()])
    initial_edge_count = varied_graph.number_of_edges()

    remove_self_loops(varied_graph)

    assert nx.number_of_selfloops(varied_graph) == 0
    assert varied_graph.number_of_edges() < initial_edge_count


def test_symmetrize_graph(weighted_graph):
    DG = nx.DiGraph(weighted_graph)

    G_avg = symmetrize_graph(DG, method="avg")
    assert isinstance(G_avg, nx.Graph)
    assert G_avg.number_of_edges() <= DG.number_of_edges()
    for u, v in G_avg.edges():
        assert G_avg[u][v]["weight"] == pytest.approx(
            (DG[u][v]["weight"] + DG[v][u]["weight"]) / 2
        )

    G_triu = symmetrize_graph(DG, method="triu")
    assert isinstance(G_triu, nx.Graph)
    assert G_triu.number_of_edges() <= DG.number_of_edges()

    with pytest.raises(
        ValueError, match="Method must be one of 'avg', 'triu', 'tril'."
    ):
        symmetrize_graph(DG, method="invalid")


def test_is_symmetric(varied_graph):
    assert is_symmetric(varied_graph) is True

    DG = nx.DiGraph(varied_graph)
    assert is_symmetric(DG) is True

    # Make it asymmetric
    if DG.number_of_edges() > 0:
        DG.remove_edge(next(iter(DG.edges()))[1], next(iter(DG.edges()))[0])
        assert is_symmetric(DG) is False
    else:
        print("Warning: The graph has no edges to make it asymmetric")


@pytest.mark.parametrize("method", ["normalize", "standardize", "invert", "binarize"])
def test_graph_rescaling_methods(varied_graph, method):
    config = GraphRescalingConfig(method=method)
    rescaler = GraphRescaling(config)
    matrix = nx.to_numpy_array(varied_graph)
    result = rescaler.apply(matrix)

    assert isinstance(result, np.ndarray)
    assert result.shape == matrix.shape

    if method == "normalize":
        assert np.max(np.abs(result)) <= 1.0 + 1e-10  # Allow small floating-point error
    elif method == "standardize":
        assert 0 <= np.min(result) <= np.max(result) <= 1.0 + 1e-10
    elif method == "invert":
        non_zero_mask = matrix != 0
        assert np.all(result[non_zero_mask] > 0)
    elif method == "binarize":
        assert np.all(np.isin(result, [0, 1]))


@pytest.mark.parametrize(
    ("method", "value"),
    [
        ("absolute", 0.3),
        ("proportional", 0.5),
        ("MST", None),
    ],
)
def test_graph_thresholding_methods(varied_graph, method, value):
    config_kwargs = {
        "method": method,
        "value": value,
        "min_span_tree": method == "MST",
        "dens_thresh": False,
    }
    config = GraphThresholdingConfig(**config_kwargs)
    thresholder = GraphThresholding(config)
    matrix = nx.to_numpy_array(varied_graph)
    result = thresholder.apply(matrix)

    assert isinstance(result, np.ndarray)
    assert result.shape == matrix.shape

    if method == "absolute":
        assert np.all((result == 0) | (result >= value))
    elif method == "proportional":
        num_nonzero = np.count_nonzero(result)
        num_edges = np.count_nonzero(matrix) // 2  # Each edge counted twice
        expected_edges = int(num_edges * value)
        expected_nonzero = 2 * expected_edges  # Account for symmetry
        # Allow for a 50% relative tolerance
        assert num_nonzero == pytest.approx(expected_nonzero, rel=0.50)
    elif method == "MST":
        if nx.is_connected(varied_graph):
            expected_edges = varied_graph.number_of_nodes() - 1
        else:
            # Sum of (n_i - 1) for each connected component with n_i > 1
            connected_components = list(nx.connected_components(varied_graph))
            expected_edges = sum(len(c) - 1 for c in connected_components if len(c) > 1)
        expected_nonzero = 2 * expected_edges  # Account for symmetry
        assert np.sum(result != 0) == pytest.approx(expected_nonzero, abs=2)


@pytest.mark.parametrize(
    "config",
    [
        SubgraphSelectionConfig(defragment=True, prune_components=True, min_nodes=2),
        SubgraphSelectionConfig(use_lcc=True),
    ],
)
def test_subgraph_selection(varied_graph, config):
    selector = SubgraphSelection(config)
    result = selector.apply(varied_graph)

    assert isinstance(result, nx.Graph)
    assert result.number_of_nodes() >= 0

    if config.use_lcc:
        if result.number_of_nodes() == 0:
            # if the graph is empty, it's acceptable
            pass
        else:
            # only check connectivity if the graph is non-empty
            assert nx.is_connected(result), "Graph should be connected when using LCC."


def test_clean_graph_process(varied_graph, example_clean_graph_config):
    cleaner = CleanGraph(varied_graph, example_clean_graph_config)
    cleaned_graph = cleaner.clean()

    assert isinstance(cleaned_graph, nx.Graph)
    assert cleaned_graph.number_of_nodes() > 0
    if varied_graph.number_of_edges() > 0:
        assert cleaned_graph.number_of_edges() > 0
    if (
        example_clean_graph_config.subgraph
        and example_clean_graph_config.subgraph.use_lcc
    ):
        if cleaned_graph.number_of_nodes() > 1:
            assert nx.is_connected(cleaned_graph)
    else:
        # If 'use_lcc' is False, allow the cleaned graph to be disconnected
        pass
