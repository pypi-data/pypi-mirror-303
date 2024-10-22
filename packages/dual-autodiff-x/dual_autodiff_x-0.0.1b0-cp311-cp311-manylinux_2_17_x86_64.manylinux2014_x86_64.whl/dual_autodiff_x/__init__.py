import toml
import os

# Load the version from pyproject.toml
def get_version():
    pyproject_path = os.path.join(os.path.dirname(__file__), "../..", "pyproject.toml")
    with open(pyproject_path, "r") as f:
        parsed_toml = toml.load(f)
    return parsed_toml['project']['version']

__version__ = get_version()

# Import the main classes
from .dual import Dual
from .autodiff_tools import get_autodiff_fun

__all__ = ["Dual", "get_autodiff_fun"]