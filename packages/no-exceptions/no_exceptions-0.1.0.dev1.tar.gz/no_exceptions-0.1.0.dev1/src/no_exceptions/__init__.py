"""
Errors as values for Python.

A more functional alternative to `try-except` blocks, offering less indented code and a chainable API.
"""

from ._all import NoArgsClosure, Result, try_expecting  # noqa: F401

__all__ = [
    'NoArgsClosure',
    'Result',
    'try_expecting',
]
