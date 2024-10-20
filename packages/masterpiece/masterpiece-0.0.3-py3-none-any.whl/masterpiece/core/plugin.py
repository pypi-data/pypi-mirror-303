"""
Base classes for plugins.

This module implements an abstract base class for plugins.

Note: This base class is designed to be abstract, so ideally, you would subclass it from 'ABC'
and decorate the `install()` method with the `@abstractmethod` decorator to enforce implementation 
in subclasses. However, the base classes have conflicting metaclasses (`ABCMeta` vs `type`),
which results in a metaclass conflict error when using formal multiple inheritance.

For now, multi-inheritance is avoided to prevent the metaclass conflict. 
Feel free to revisit this and refine the structure later.

TODO: Consider a solution for resolving the metaclass conflict and implementing proper 
multi-inheritance.
"""

# from abc import ABC, abstractmethod

from .composite import Composite, MasterPiece


class Plugin(MasterPiece):
    """Base class for plugins.
    TODO: make formally abstract

    """

    # @abstractmethod
    def install(self, app: Composite):
        """Instantiates and installs the classes in the plugin module into the application.
        This is an abstract method that the plugin classes must implement. Plugins may
        choose not to do anything here and instead leave it up to the higher level software layers.

        Args:
            app (Composite): application to plug into
        """
