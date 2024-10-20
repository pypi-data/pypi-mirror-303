# src/matengine/__init__.py

"""
MatEngine: A Python library for material generation, characterization, discovery, and simulation.
"""

from ._version import __version__

# Import subpackages to simplify access
from . import generation
from . import characterization
from . import discovery
from . import simulation
from . import utils
from . import data

# Optionally, define what is available when importing *
__all__ = [
    "generation",
    "characterization",
    "discovery",
    "simulation",
    "utils",
    "data",
]
