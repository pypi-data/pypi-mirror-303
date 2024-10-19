from nxlu._version import __version__

from .core import *
from .explanation import *
from .processing import *
from .utils import *
from .utils.log import initialize_logging

__packagename__ = "nxlu"
__url__ = "https://github.com/dpys/NxLU"

DOWNLOAD_URL = f"https://github.com/dpys/{__packagename__}/archive/{__version__}.tar.gz"

initialize_logging()
