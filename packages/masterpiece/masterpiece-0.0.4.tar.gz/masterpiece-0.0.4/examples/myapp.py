"""Example application demonstrating a typical masterpiece application featuring:

- Class initialization through startup arguments 
- Automatically created class configuration files
- Serialization/deserialization

Implements the following classes:
- MyHomeArgs - application startup options
- MyHome - application
"""

from argparse import ArgumentParser
from typing import Optional
from masterpiece.core import Application, MasterPiece, Composite, Args


class MyHomeArgs(Args):
    """Startup arguments"""

    solar: Optional[float] = None


class MyHome(Application):
    """Application demonstrating the structure of masterpiece applications.
    Also demonstrates plugin awareness and startup arguments.
    When run, the application prints out its instance hierarchy:

    Example:
        home
        ├─ grid
        ├─ downstairs
        │   └─ kitchen
        │       ├─ oven
        │       └─ fridge
        ├─ garage
        │   └─ EV charger
        └─ solar plant 5.0 kW

    If the --solar [kW] startup argument is passed with a power value, the
    "solar plant" instance is added to the hierarchy.

    """

    # Class attributes can be configured in two ways: either through class
    # configuration files, automatically created for each class when the
    # application is first started, or via startup arguments. If both are defined,
    # the startup arguments take precedence.
    solar_plant: float = 0

    def __init__(self, name: str = "myhome") -> None:
        """Initialize the home application with the given name.

        Instance attributes can be initialized from class attributes,
        through a serialization file, or from constructor parameters.

        Args:
            name (str): The name of the application.
        """
        super().__init__(name)
        self.create_home()
        self.install_plugins()

    def create_home(self):
        """Create a default built-in home structure, which can be overridden
        by the instance hierarchy defined in the serialization file. See --file
        startup argument.
        """
        self.create_power_grid()
        self.create_downstairs()
        self.create_garage()
        self.create_solar_plant()

    def create_power_grid(self):
        """Create the power grid."""
        grid = MasterPiece("grid")
        self.add(grid)

    def create_solar_plant(self):
        """Create solar plant, if configured by '~/.myhome/config/MyHomeApp.json',
        or the '-s' startup argument."""
        if self.solar_plant > 0:
            self.add(MasterPiece(f"solar plant {self.solar_plant} kW"))

    def create_downstairs(self):
        """Create the downstairs section with a kitchen and appliances."""
        downstairs = Composite("downstairs")
        self.add(downstairs)
        kitchen = Composite("kitchen")
        downstairs.add(kitchen)
        oven = MasterPiece("oven")
        kitchen.add(oven)
        fridge = MasterPiece("fridge")
        kitchen.add(fridge)

    def create_garage(self) -> None:
        """Create the garage with an EV charger."""
        garage = Composite("garage")
        self.add(garage)
        ev_charger = MasterPiece("EV charger")
        garage.add(ev_charger)

    # @overwrite
    def run(self) -> None:
        """Start the application."""
        super().run()

        # Print out the instance hierarchy
        self.print()

    @classmethod
    def register_args(cls, parser: ArgumentParser) -> None:
        """Register startup arguments to be parsed.

        Args:
            parser (argparse.ArgumentParser): Parser to add the startup arguments.
        """
        parser.add_argument(
            "-s",
            "--solar",
            type=float,
            help="Add a solar power plant with the given power (in kW).",
        )

    @classmethod
    def configure_args(cls, args) -> None:
        """Configure class attributes based on parsed arguments."""
        if args.solar is not None and args.solar > 0.0:
            cls.solar_plant = float(args.solar)


def main() -> None:
    """Main function that initializes, instantiates, and runs the MyHome application."""

    # Make this app plugin-aware. See the 'masterpiece_plugin' project for a minimal plugin example.
    MyHome.load_plugins()

    # Support class initialization through startup arguments
    MyHome.parse_args()

    # Create an instance of MyHome application
    home = MyHome("home")

    # Initialize from the serialization file if specified
    home.deserialize()

    # Start event processing or the application's main loop
    home.run()

    # Save the application's state to a serialization file (if specified)
    home.serialize()


if __name__ == "__main__":
    main()
