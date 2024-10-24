from _nxlu.config import NxluConfig
from nxlu.core.base import BaseBackend
from nxlu.core.factory import get_backend

__all__ = ["BackendManager"]


class BackendManager:
    """Manage the NetworkX backend for nxlu.

    Parameters
    ----------
    config : NxluConfig
        Configuration settings for the model and backend.
    """

    def __init__(self, config: NxluConfig):
        """Initialize the BackendManager with the given configuration.

        Parameters
        ----------
        config : NxluConfig
            Configuration settings for the model and backend.
        """
        self.config = config
        self.backend = get_backend(config.get_backend_name())

    def get_backend(self) -> BaseBackend:
        """Retrieve the instantiated backend.

        Returns
        -------
        BaseBackend
            The instantiated backend.
        """
        return self.backend
