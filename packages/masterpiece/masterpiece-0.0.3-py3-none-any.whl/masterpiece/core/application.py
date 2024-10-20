import argparse
from typing import List, Type, Optional, Union

from .plugmaster import PlugMaster
from .composite import Composite
from .masterpiece import MasterPiece


class Application(Composite):
    """Masterpiece application base class. Implements startup argument parsing,
    plugin management and initialization of class attributes through
    class specific JSON configuration files.

    .. todo:: Abstract the serialization API to support multiple formats (e.g., JSON, XML, etc.).
    """

    plugins: List[Type[MasterPiece]] = []
    serialization_file: str = ""
    plugin_groups = ["masterpiece"]
    _plugmaster: PlugMaster

    def __init__(self, name: str, payload: Optional[MasterPiece] = None) -> None:
        """Instantiates and initializes. By default, the application log
        filename is set to the same as the application name.

        Args:
            name (str): The name of the application, determining the default log filename.
            payload (MasterPiece): Playload object associated with this object.
        """
        super().__init__(name, payload)

    @classmethod
    def load_class_attributes(cls) -> None:
        MasterPiece.parse_initial_args()
        for name, ctor in MasterPiece.get_registered_classes().items():
            ctor.load_from_json()

    @classmethod
    def register_plugin_group(cls, name: str) -> None:
        """Registers a new plugin group within the application. Only plugins that match
        the registered groups will be loaded. By default, all 'masterpiece' plugins
        are included. Frameworks built on the MasterPiece framework can define
        framework-specific group names, enabling plugins to be developed for any
        application built on those frameworks. Additionally, individual applications
        can introduce application-specific groups (typically named after the application),
        allowing plugins to be developed exclusively for that specific application.


        Args:
            name (str): The name of the plugin group to be registered
        """

        if not name in cls.plugin_groups:
            cls.plugin_groups.append(name)

    @classmethod
    def load_plugins(cls) -> None:
        """Loads and initializes all plugins for instantiation. This method
        corresponds to importing Python modules with import clauses."""
        for g in cls.plugin_groups:
            cls._plugmaster.load(g)

    def instantiate_plugin_by_name(self, name: str) -> Union[MasterPiece, None]:
        """Installs the plugin by name, that is, instantiates the plugin class
        and inserts the instance as child to the application.
        Args:
            name (str): name of the plugin class
        """
        return self._plugmaster.instantiate_class_by_name(self, name)

    def install_plugins(self) -> None:
        """Installs plugins into the application by invoking the `install()` method
        of each loaded plugin module.
        **Note:** This method is intended for testing and debugging purposes only.
        In a typical use case, the application should handle the instantiation of classes and
        manage their attributes as needed.
        """
        self._plugmaster.install(self)

    def deserialize(self) -> None:
        """Deserialize instances from the startup file specified by 'serialization_file' class attribute, or
        '--file' startup argument.

        TODO: or by optional method parameter
        """
        if self.serialization_file != "":
            self.info(f"Loading masterpieces from {self.serialization_file}")

            with open(self.serialization_file, "r", encoding="utf-8") as f:
                self.deserialize_from_json(f)
                self.info(f"File {self.serialization_file} successfully loaded")

    def serialize(self) -> None:
        """Serialize application state to the file specified by 'serialization_file' class attribute'.

        TODO: or by optional method parameter
        """
        if self.serialization_file != "":
            self.info(f"Saving masterpieces to {self.serialization_file}")

            with open(self.serialization_file, "w", encoding="utf-8") as f:
                self.serialize_to_json(f)
                self.info(f"File {self.serialization_file} successfully written")

    @classmethod
    def register_args(cls, parser: argparse.ArgumentParser):
        """Register startup arguments to be parsed.

        Args:
            parser (argparse.ArgumentParser): parser to add the startup arguments.
        """
        parser.add_argument(
            "-f",
            "--file",
            help="Specify the file to load or save application state.",
        )

    @classmethod
    def configure_args(cls, args) -> None:
        if args.file is not None:
            cls.serialization_file = args.file

    @classmethod
    def register(cls):
        cls._plugmaster = PlugMaster(MasterPiece.get_app_name())
