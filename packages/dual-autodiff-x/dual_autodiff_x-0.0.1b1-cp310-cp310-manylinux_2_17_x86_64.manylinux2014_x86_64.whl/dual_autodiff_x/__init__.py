import toml
import os



__version__ = "0.0.1b1"

# Import the main classes
from .dual import Dual
from .autodiff_tools import get_autodiff_fun

__all__ = ["Dual", "get_autodiff_fun"]