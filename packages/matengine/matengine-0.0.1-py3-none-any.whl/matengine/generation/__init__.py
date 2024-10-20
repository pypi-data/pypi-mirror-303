# src/matengine/generation/__init__.py

"""
The generation subpackage provides tools for generating material structures at various scales.
"""

# Import modules to simplify access
from . import plurigaussian
from . import generators
from . import decisiontree
from . import filters


__all__ = [
    "generators",
    "plurigaussian"
]
