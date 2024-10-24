import functools
import inspect
import logging
from abc import ABCMeta
from collections.abc import Callable
from threading import Lock
from typing import Any

import networkx as nx

from _nxlu.info import get_info
from nxlu.config import NxluConfig
from nxlu.core.base import BaseBackend
from nxlu.exceptions import handle_error
from nxlu.explanation.explain import GraphExplainer
from nxlu.getters import get_available_algorithms
from nxlu.processing.analyze import map_algorithm_result
from nxlu.utils.misc import ReadableDict

logger = logging.getLogger("nxlu")


__all__ = ["explain_algorithm", "LLMGraph", "BackendMeta", "BackendInterface"]


def explain_algorithm(func: Callable) -> Callable:
    """Decorate NetworkX algorithms to generate explanations.

    This decorator enhances NetworkX algorithms by generating natural language
    explanations for the algorithm's results using the LLMGraph class.

    Parameters
    ----------
    func : Callable
        The NetworkX algorithm function to be decorated.

    Returns
    -------
    Callable
        A decorated function that provides the original algorithm's output
        along with natural language explanations.
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        G = kwargs.get("G")
        if G is None and args:
            G = args[0]
            kwargs["G"] = G
            args = args[1:]
        if not isinstance(G, LLMGraph):
            return func(*args, **kwargs)

        result = func(*args, **kwargs)

        algorithm_name = func.__name__
        explanation = G.explainer.explain_algorithm(G, algorithm_name, result)

        G._algorithm_explanations[algorithm_name] = explanation

        return result

    return wrapper


class LLMGraph(nx.Graph):
    """A NetworkX Graph subclass that integrates nxlu's GraphExplainer to provide
    natural language explanations for graph algorithms.

    This subclass extends the standard NetworkX Graph functionality by adding
    the ability to run algorithms and generate natural language explanations
    for their outputs.

    Attributes
    ----------
    explainer : GraphExplainer
        An instance of GraphExplainer used to generate explanations.
    _algorithm_explanations : dict
        A dictionary that stores explanations for algorithms that have been run.

    Methods
    -------
    run_algorithm(algorithm_name: str, **kwargs) -> Dict[str, Any]:
        Run a specified graph algorithm and generates a natural language explanation.
    get_explanation(algorithm_name: str) -> str:
        Retrieve the explanation for a specified algorithm.
    """

    __networkx_backend__ = "nxlu"

    def __init__(self, *args, **kwargs):
        """Initialize the LLMGraph with nxlu's GraphExplainer.

        Parameters
        ----------
        *args : Any
            Variable length argument list for NetworkX Graph.
        **kwargs : Any
            Arbitrary keyword arguments for NetworkX Graph.
        """
        super().__init__(*args, **kwargs)
        config = NxluConfig()
        self.explainer = GraphExplainer(config)
        self._algorithm_explanations = {}
        self._explanations_lock = Lock()
        logger.info("LLMGraph initialized with GraphExplainer.")

    def run_algorithm(self, algorithm_name: str, **kwargs) -> dict[str, Any]:
        """Run a specified graph algorithm and generates a natural language explanation.

        Parameters
        ----------
        algorithm_name : str
            The name of the algorithm to run.
        **kwargs : dict
            Additional arguments to pass to the algorithm.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the algorithm's result and its natural language
            explanation.

        Raises
        ------
        ValueError
            If the algorithm is not available in NetworkX or the provided graph is
            invalid.
        """
        logger.debug(
            f"run_algorithm called for '{algorithm_name}' with kwargs: {kwargs}"
        )

        available_algorithms = get_available_algorithms(nxlu_only=False)

        if algorithm_name not in available_algorithms:
            raise ValueError(
                f"Algorithm '{algorithm_name}' is not available in NetworkX."
            )

        algorithm_func = available_algorithms[algorithm_name]

        original_algorithm_func = inspect.unwrap(algorithm_func)

        standard_graph = nx.Graph(self)

        sig = inspect.signature(original_algorithm_func)
        for param in sig.parameters.values():
            if param.name == "G":
                kwargs["G"] = standard_graph
            if param.name == "seed":
                seed = kwargs.get("seed", None)
                if seed is None:
                    import random

                    import numpy as np

                    if "algebraic_connectivity" in algorithm_name:
                        seed = np.random.RandomState(42)
                    else:
                        seed = random.Random(42)
                kwargs["seed"] = seed
        try:
            kwargs.pop("backend", None)
            result = original_algorithm_func(**kwargs)
            logger.debug(f"Algorithm '{algorithm_name}' result: {result}")
        except Exception as e:
            handle_error(e, f"Error executing algorithm '{algorithm_name}'")
            raise

        map_algorithm_result(self, algorithm_name, result)
        logger.debug(f"Mapped results for '{algorithm_name}'")

        explanation = self.explainer.explain_algorithm(self, algorithm_name, result)
        logger.debug(
            f"Generated explanation for '{algorithm_name}': {explanation[:50]}..."
        )

        with self._explanations_lock:
            self._algorithm_explanations[algorithm_name] = explanation
        logger.debug(
            f"Stored explanation for '{algorithm_name}' in _algorithm_explanations"
        )

        return ReadableDict(
            {
                "algorithm": algorithm_name,
                "result": result,
                "explanation": explanation,
            }
        )

    def get_explanation(self, algorithm_name: str) -> str:
        """Retrieve the explanation for a specified algorithm.

        Parameters
        ----------
        algorithm_name : str
            The name of the algorithm whose explanation is to be retrieved.

        Returns
        -------
        str
            The natural language explanation of the algorithm's results.

        Raises
        ------
        KeyError
            If no explanation exists for the specified algorithm.
        """
        try:
            with self._explanations_lock:
                return self._algorithm_explanations[algorithm_name]
        except KeyError:
            error_msg = (
                f"No explanation found for algorithm '{algorithm_name}'. Run "
                "the algorithm first."
            )
            logger.exception(error_msg)
            raise KeyError(error_msg)


class BackendMeta(ABCMeta):
    """Meta class for dispatching graph algorithms with the NxLU Backend.

    This class enables dynamic dispatching of graph algorithms based on the
    algorithm name, integrating them with the LLM-based graph explanation.

    Methods
    -------
    __getattr__(name: str) -> callable:
        Dispatches the graph algorithm when accessed via class attributes.
    """

    def __getattr__(cls, name):
        if name in cls.get_supported_functions():

            def method(*args, **kwargs):
                if not args:
                    raise ValueError(
                        f"Graph must be provided as the first argument to '{name}'"
                    )
                graph = args[0]
                return cls.run_algorithm(graph, name, **kwargs)

            return method
        raise AttributeError(f"'{cls.__name__}' object has no attribute '{name}'")


class BackendInterface(BaseBackend, metaclass=BackendMeta):
    """Dispatcher for the NxLU Backend.

    This backend integrates individual graph algorithms with NxLU,
    providing natural language explanations for algorithm outputs.

    Methods
    -------
    run_algorithm(graph: nx.Graph, algorithm_name: str, **kwargs) -> Dict[str, Any]:
        Run a specified graph algorithm and returns its results along with explanations.
    convert_from_nx(graph, *args, edge_attrs=None, weight=None, **kwargs):
        Convert a NetworkX graph to an LLMGraph.
    convert_to_nx(result, *, name=None):
        Convert an LLMGraph back to a NetworkX graph.
    """

    def __init__(self):
        """Initialize the BackendInterface with the LLMGraph class."""
        self.graph_class = LLMGraph
        logger.info("NxLU Backend initialized.")

    @staticmethod
    def run_algorithm(graph: nx.Graph, algorithm_name: str, **kwargs) -> dict[str, Any]:
        """Run a specified graph algorithm and returns its results along with
        explanations.

        Parameters
        ----------
        graph : nx.Graph
            The input graph to run the algorithm on.
        algorithm_name : str
            The name of the algorithm to run.
        **kwargs : dict
            Additional arguments to pass to the algorithm.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the algorithm's result and its natural language
            explanation.

        Raises
        ------
        Exception
            If there is an error while executing the algorithm.
        """
        logger.info(f"Running algorithm '{algorithm_name}' with arguments {kwargs}")
        logger.debug(
            f"run_algorithm invoked for '{algorithm_name}' with graph: {graph}"
        )

        try:
            if isinstance(graph, LLMGraph):
                logger.debug(
                    "Graph is an instance of LLMGraph. Using existing instance."
                )
                results = graph.run_algorithm(algorithm_name, **kwargs)
            else:
                logger.debug(
                    "Graph is not an instance of LLMGraph. Wrapping with LLMGraph."
                )
                llm_graph = LLMGraph(graph)
                results = llm_graph.run_algorithm(algorithm_name, **kwargs)
            logger.info(f"Algorithm '{algorithm_name}' executed successfully.")
        except Exception:
            logger.exception(f"Failed to execute algorithm '{algorithm_name}'")
            raise

        return ReadableDict(results)

    @staticmethod
    def convert_from_nx(graph, *args, edge_attrs=None, weight=None, **kwargs):
        """Convert a NetworkX graph to an LLMGraph.

        Parameters
        ----------
        graph : nx.Graph
            The input NetworkX graph.
        edge_attrs : dict, optional
            Edge attributes to apply to the new graph.
        weight : str, optional
            The name of the edge attribute to treat as weights.

        Returns
        -------
        LLMGraph
            The converted LLMGraph.
        """
        if isinstance(graph, LLMGraph):
            return graph

        if weight is not None:
            if edge_attrs is not None:
                raise TypeError(
                    "edge_attrs and weight arguments should not both be given"
                )
            edge_attrs = {weight: 1}
        return LLMGraph(graph, *args, edge_attrs=edge_attrs, **kwargs)

    @staticmethod
    def convert_to_nx(result, *, name=None):
        """Convert an LLMGraph back to a NetworkX graph.

        Parameters
        ----------
        result : LLMGraph
            The LLMGraph to convert.
        name : str, optional
            Name of the algorithm.

        Returns
        -------
        nx.Graph
            The converted NetworkX graph.
        """
        if isinstance(result, LLMGraph):
            return result
        return result

    @classmethod
    def can_run(cls, name: str, *args, **kwargs) -> bool:
        return name in cls.get_supported_functions()

    @classmethod
    def should_run(cls, name: str, *args, **kwargs) -> bool:
        return cls.can_run(name, *args, **kwargs)

    @classmethod
    def get_supported_functions(cls) -> set:
        """Get the set of functions supported by the backend.

        Returns
        -------
        set
            Set of supported function names.
        """
        info = cls.get_info()
        return set(info.get("functions", {}).keys())

    @classmethod
    def get_info(cls) -> dict[str, Any]:
        """Retrieve the backend's information including supported algorithms and
        features.

        Returns
        -------
        Dict[str, Any]
            Dictionary containing backend information.
        """
        return get_info()
