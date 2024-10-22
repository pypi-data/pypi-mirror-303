__version__ = "0.2"
try:
    from . import _version

    __version__ = _version.version
except ImportError:
    pass

from .simulate_discoal import Simulator, DISCOAL
from .fv import summary_statistics
from .data import Data
from .cnn import CNN
