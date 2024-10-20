"""
Description
===========

Base classes for MasterPiece - a light-weight and general purpose object-oriented toolkit
for implementing modular plugin-aware applications.

"""

from .masterpiece import MasterPiece, Args
from .composite import Composite
from .application import Application
from .log import Log
from .plugin import Plugin
from .plugmaster import PlugMaster


__all__ = [
    "MasterPiece",
    "Composite",
    "Application",
    "Args",
    "Log",
    "Plugin",
    "PlugMaster",
]
