from abc import ABC, abstractmethod
from typing import Any

import networkx as nx

__all__ = ["BaseBackend"]


class BaseBackend(ABC):
    """Abstract base class for all NetworkX backends in nxlu.

    This class defines the required interface that all backends must implement.
    """

    @abstractmethod
    def run_algorithm(
        self, graph: nx.Graph, algorithm_name: str, **kwargs
    ) -> dict[str, Any]:
        """Run the specified algorithm on the given graph and returns the results.

        Parameters
        ----------
        graph : networkx.Graph
            The graph instance on which the algorithm will be executed.
        algorithm_name : str
            The name of the NetworkX algorithm to run.
        **kwargs : Any
            Additional keyword arguments for the algorithm.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing the algorithm results and any relevant explanations.

        Raises
        ------
        NotImplementedError
            If the method is not implemented in the subclass.
        """

    @abstractmethod
    def get_info(self) -> dict[str, Any]:
        """Provide information about the backend.

        Returns
        -------
        Dict[str, Any]
            A dictionary containing metadata about the backend, such as name,
            version, description, author, and URL.

        Raises
        ------
        NotImplementedError
            If the method is not implemented in the subclass.
        """
