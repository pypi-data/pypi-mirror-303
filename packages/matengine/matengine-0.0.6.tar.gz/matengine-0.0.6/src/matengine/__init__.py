# src/matengine/__init__.py

# Import subpackages to simplify access
from . import generation
from . import characterization
from . import discovery
from . import simulation
from . import utils

# Optionally, define what is available when importing *
__all__ = [
    "generation",
    "characterization",
    "discovery",
    "simulation",
    "utils",
]
