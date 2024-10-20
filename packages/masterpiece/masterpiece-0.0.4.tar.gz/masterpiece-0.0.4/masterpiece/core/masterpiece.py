"""
    masterpiece.py

    This module defines the foundational classes for the framework. These elementary
    base classes form the core upon which all other classes in the framework are built.

    Classes:
        MasterPiece: A base class representing a fundamental component in the framework.
        These objects can be copied, serialized, instantiated through class 
        id (factory method pattern).

        Args: Base class for per-class startup arguments

    The `MasterPiece` class can be described as a named object with a payload and parent object.
    In other words, the object can be linked to any other 'MasterPiece' object as a children,
    and it can carry any other object with it. It is up to the sub classes define the payload
    objects. 

    Example:
        from masterpiece import MasterPiece

        obj = MasterPiece(name="livingroom", payload = TemperatureSensor(t))

    Note:
        Ensure `from __future__ import annotations` is included at the top of this module
        to avoid issues with forward references in type hints.

"""

from __future__ import annotations
import os
import sys
import json
import logging
import datetime
from typing import Any, Callable, Optional
import atexit
import argparse


class Args:
    """Defines typing for ArgumentParser arguments.
    Subclasses of `MasterPiece` can extend this base class to define
    additional startup arguments.

    .. todo:: Update the implementation to address Liskov's Substitution Principle warning.
    """

    config: Optional[str] = "config"


class MasterPiece:
    """An object with a name. Base class of everything. Serves as the
    foundational class offering key features needed by any robust
    object-oriented software.

    Logging
    -------

    All objects have logging methods e.g. info() and error() at their fingertips, for
    centralized logging.
    ::

        if (err := self.do_good()) < 0:
            self.error(f"Damn, did bad {err}")

    Factory Method Pattern
    ----------------------

    Instantiation via class identifiers, adhering to the factory method pattern.
    This allows for the dynamic creation of instances based on class identifiers,
    promoting decoupled and extensible design required by plugin architecture.
    ::

        # instead of fixed implementation car = Ferrari()
        car = Object.instantiate(car_class_id)


    Serialization
    -------------

    Serialization of both class and instance attributes serves as a means of configuration.

    Class attributes should follow a consistent naming convention where an underscore prefix
    ('_' or '__') implies the attribute is private and transient, meaning it is not serialized.
    Class attributes without an underscore prefix are initialized from configuration files named
    '~/.masterpiece/[appname]/[classname].json', if present. If the class-specific configuration
    files do not already exist, they are automatically created upon the first run.


    Instance attributes can be serialized and deserialized using the `serialize()`
    and `deserialize()` methods:
    ::

        # serialize to json file
        with open("foo.json", "w") as f:
            foo.serialize(f)

        # deserialize
        foo = F()
        with open("foo.json", "r") as f:
            foo.deserialize(f)

    Deserialization must restore the object's state to what it was when it was serialized.
    As Python does not have 'transient' keyword to tag attributes that should be serialized, all
    classes must explicitely describe information for the serialization. This is done with
    `to_dict()` and `from_dict()` methods:
    ::

        def to_dict(self):
            data = super().to_dict()
            data["_foo"] = {
                "topic": self.topic,
                "temperature": self.temperature,
            }
            return data

        def from_dict(self, data):
            super().from_dict(data)
            for key, value in data["_foo"].items():
                setattr(self, key, value)


    Copying Objects
    ---------------

    Any object can be copied using the `copy()` method. This feature is based on serialization, so
    typically, subclasses don't need to implement the `copy()` method; everything is taken care of
    by the base class.
    ::

        foo2 = foo.copy()

    """

    # non-serializable private class attributes
    _app_name = "masterpiece"
    _config = "config"
    _log: Optional[logging.Logger] = None
    _factory: dict = {}
    _arg_parser = argparse.ArgumentParser()
    _class_id: str = ""

    def __init_subclass__(cls, **kwargs: dict[str, Any]) -> None:
        """Called when a new sub-class is created.

        Automatically registers the sub class by calling its register()
        method. For more information on this method consult Python
        documentation.
        """
        super().__init_subclass__(**kwargs)
        cls.register()

    @classmethod
    def register(cls) -> None:
        """Register the class.

        Called immediately upon class initialization, right before the class attributes
        are loaded from the class specific configuration files.

        Subclasses can extend this with custom register functionality:

        .. code-block:: python

            class MyMasterPiece(MasterPiece):

                @classmethod
                def register(cls):
                    super().register()  # Don't forget
                    cls._custom_field = True
        """
        cls._class_id = cls.__name__

        if not cls.is_abstract():
            cls.register_class(cls.get_class_id(), cls)

        if cls.has_class_method_directly("register_args"):
            cls.register_args(cls._arg_parser)

        # automatically create configuration file, if not created already
        atexit.register(cls.save_to_json)

    @classmethod
    def app_name(cls, name: str):
        """Set application name

        Args:
            name (str): application name
        """
        cls._app_name = name

    @classmethod
    def get_app_name(cls) -> str:
        """Get application name

        Returns:
            name (str): application name
        """
        return cls._app_name

    @classmethod
    def initialize_class(cls, load_class_attrs: bool = True) -> bool:
        """Initialize the class for instantiation. Initializes the class identifier.
        Initialize public class attributes from the class-specific configuration files,
        unless disabled with the `load_class_attrs` parameter.
        Call the `register()` method of the class to let each class do custom initializations.
        Set up `atexit` callback to generate class-specific initialization files if they
        don't exist already.

        Args:
            load_class_attrs (bool, optional): If true, then attempts to initialize class attributes
                from the class-specific configuration files. Defaults to True.

        Returns:
            bool: Returns true if the class was initialized. False implies the class is already
            initialized, in which case the method call has no effect.
        """
        if cls._class_id == "":
            cls._class_id = cls.__name__
            cls.register_class(cls.__name__, cls)
            cls.register()
            if load_class_attrs:
                cls.load_from_json()
                atexit.register(cls.save_to_json)
            return False
        else:
            return True

    @classmethod
    def is_abstract(cls) -> bool:
        """Check whether the class is abstract or real. Override in the derived
        sub-classes. The default is False.

        Returns:
            True (bool) if abstract
        """
        return False

    @classmethod
    def set_log(cls, l: logging.Logger) -> None:
        """Set logger.

        Args:
            l (logger): logger object
        """

        cls._log = l

    @classmethod
    def get_class_id(cls) -> str:
        """Return the class id of the class. Each class has an unique
        identifier that can be used for instantiating the class via
        :meth:`Object.instantiate` method.

        Args:
            cls (class): class

        Returns:
            id (int) unique class identifier through which the class can be
            instantiated by factory method pattern.
        """
        return cls.__name__

    def __init__(
        self, name: str = "noname", payload: Optional[MasterPiece] = None
    ) -> None:
        """Creates object with the given name and  payload. The payload object
        must be of type  `MasterPiece` as well.

        Example:
            ```python
            obj = MasterPiece('foo', Foo("downstairs"))
            obj.info('Yippee, object created')
            ```
        """
        self.name = name
        self.payload = payload

    @classmethod
    def parse_initial_args(cls):
        """Parse application name and configuration name  arguments. Note that argument parsing
        is two stage process. This method must be
        called  at very early on to know where to load class initialization  files.
        See `register_args()` method.
        """

        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument("-a", "--app", type=str, help="Application name")
        parser.add_argument("-c", "--config", type=str, help="Configuration")

        args, remaining_argv = parser.parse_known_args()
        sys.argv = [sys.argv[0]] + remaining_argv
        if args.config is not None:
            cls._config = args.config
        if args.app is not None:
            cls._app_name = args.app

        print(
            f"{cls._app_name} started with configuration ~.{cls._app_name}/{cls._config}"
        )

    def debug(self, msg: str, details: str = "") -> None:
        """Logs the given debug message to the application log.

        Args:
            msg (str): The information message to be logged.
            details (str): Additional detailed information for the message to be logged
        """
        if self._log is not None:
            self._log.debug(f"{self.name} : {msg} - {details}")

    def info(self, msg: str, details: str = "") -> None:
        """Logs the given information message to the application log.

        Args:
            msg (str): The information message to be logged.
            details (str): Additional detailed information for the message to be logged
        """
        if self._log is not None:
            self._log.info(f"{self.name} : {msg} - {details}")

    def warning(self, msg: str, details: str = "") -> None:
        """Logs the given warning message to the application log.

        Args:
            msg (str): The message to be logged.
            details (str): Additional detailed information for the message to be logged
        """
        if self._log is not None:
            self._log.warn(f"{self.name} : {msg} - {details}")

    def error(self, msg: str, details: str = "") -> None:
        """Logs the given error message to the application log.

        Args:
            msg (str): The message to be logged.
            details (str): Additional detailed information for the message to be logged
        """
        if self._log is not None:
            self._log.error(f"{self.name} : {msg} - {details}")

    @classmethod
    def get_json_file(cls):
        """Generate the JSON file name based on the class name.

        The file is created into users home folder.
        """
        return os.path.join(
            os.path.expanduser("~"),
            "." + cls._app_name,
            cls._config,
            cls.__name__ + ".json",
        )

    def to_dict(self):
        """Convert instance attributes to a dictionary."""

        return {
            "_class": self.get_class_id(),  # the real class
            "_version:": 0,
            "_object": {
                "name": self.name,
                "payload": (
                    self.payload.to_dict() if self.payload is not None else None
                ),
            },
        }

    def from_dict(self, data):
        """Update instance attributes from a dictionary."""

        if self.get_class_id() != data["_class"]:
            raise ValueError(
                f"Class mismatch, expected:{self.get_class_id()}, actual:{data['_class']}"
            )
        for key, value in data["_object"].items():
            if key == "payload":
                if value is not None:
                    self.payload = MasterPiece.instantiate(value["_class"])
                    self.payload.from_dict(value)
                else:
                    self.payload = None
            else:
                setattr(self, key, value)

    def serialize_to_json(self, f):
        """Serialize the object to given JSON file"""
        json.dump(self.to_dict(), f, indent=4)

    def deserialize_from_json(self, f):
        """Load  attributes from the given JSON file."""
        attributes = json.load(f)
        self.from_dict(attributes)

    def copy(self) -> MasterPiece:
        """Create and return a copy of the current object.

        This method serializes the current object to a dictionary using the `to_dict` method,
        creates a new instance of the object's class, and populates it with the serialized data
        using the `from_dict` method.

        This method uses class identifier based instantiation (see factory method pattern) to
        create a new instance of the object, and 'to_dict' and 'from_dict'  methods to initialize
        object's state.

        Returns:
            A new instance of the object's class with the same state as the original object.

        Example:
        ::

            clone_of_john = john.copy()
        """

        data = self.to_dict()
        copy_of_self = MasterPiece.instantiate(self.get_class_id())
        copy_of_self.from_dict(data)
        return copy_of_self

    def quantize(self, quanta: float, value: float):
        """Quantize the given value.

        Args:
            quanta (float): resolution for quantization
            value (float): value to be quantized

        Returns:
            (float): quantized value

        Example:
        ::

            hour_of_a_day = self.quantize(3600, epoch_seconds)
        """
        return (value // quanta) * quanta

    def epoc2utc(self, epoch):
        """Converts the given epoch time to UTC time string. All time
        coordinates are represented in UTC time. This allows the time
        coordinate to be mapped to any local time representation without
        ambiguity.

        Args:
            epoch (float) : timestamp in UTC time
            rc (str): time string describing date, time and time zone e.g 2024-07-08T12:10:22Z

        Returns:
            UTC time
        """
        utc_time = datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc)
        utc_timestr = utc_time.strftime("%Y-%m-%dT%H:%M:%S") + "Z"
        return utc_timestr

    def timestampstr(self, ts: float):
        """Converts the given timestamp to human readable string of format 'Y-m-d
        H:M:S'.

        Args:
            ts (timestamp):  time stamp to be converted

        Returns:
            rc (string):  human readable date-time string
        """
        return str(datetime.datetime.fromtimestamp(ts).strftime("%Y-%m-%d %H:%M:%S"))

    def timestamp(self):
        """Returns the current date-time in UTC.

        Returns:
            rc (datetime):  datetime in UTC.
        """
        return datetime.datetime.now(datetime.timezone.utc).timestamp()

    def timestamp_hour(self, ts: float):
        """Returns the hour in 24h format in UTC.

        Args:
            ts (float): timestamp
        Returns:
            rc (int):  current hour in UTC 0 ...23
        """
        dt = datetime.datetime.fromtimestamp(ts)
        return dt.hour

    def is_time_between(self, begin_time, end_time, check_time=None):
        """Check if the given time is within the given time line. All
        timestamps must be in UTC time.

        Args:
            begin_time (timestamp):  beginning of the timeline
            end_time (timestamp):  end of the timeline
            check_time (timestamp):  time to be checked

        Returns:
            rc (bool):  True if within the timeline
        """

        check_time = check_time or datetime.datetime.utcnow().time()
        if begin_time < end_time:
            return check_time >= begin_time and check_time <= end_time
        else:  # crosses midnight
            return check_time >= begin_time or check_time <= end_time

    def elapsed_seconds_in_hour(self, ts_utc: float) -> float:
        """Given timestamp in UTC, Compute elapsed seconds within an hour

        Args:
            ts  (float) : seconds since UTC epoch
        Returns:
            float: _description_
        """

        ts = datetime.datetime.fromtimestamp(ts_utc)
        # Define start time (for example 9:15:30)
        start_time = ts.replace(minute=15, second=30, microsecond=0)

        # Compute the difference between the times
        elapsed_time = ts - start_time

        # Convert the difference to seconds
        return elapsed_time.total_seconds()

    def elapsed_seconds_in_day(self, ts_utc: float) -> float:
        """Fetch the elapsed seconds since the be given time stamp 'ts_utc'.

        Returns:
            float: elapsed second today
        """
        # Convert the float timestamp into a datetime object
        timestamp_datetime = datetime.datetime.fromtimestamp(ts_utc)
        # Get the start of today (midnight)
        midnight = datetime.datetime.combine(timestamp_datetime.date(), datetime.time())
        # Calculate the elapsed seconds since midnight
        elapsed_seconds = (timestamp_datetime - midnight).total_seconds()
        return elapsed_seconds

    def print(self, prefix="", is_last=True):
        """Print the name of the object, decorated with prefix consisting of ├─, └─, and │."""

        print(prefix, end="")
        if prefix:
            print("└─ " if is_last else "├─ ", end="")
        print(self.name)

    def run(self) -> None:
        """Run the masterpiece.  Dispatches the call to `payload` object and
        returns  the control to the caller.
        """
        if self.payload is not None:
            self.payload.run()

    def run_forever(self) -> None:
        """Run the masterpiece forever. This method will return only when violently
        terminated.
        """
        if self.payload is not None:
            try:
                self.payload.run_forever()
                print("Newtorking loop exit without exception")
            except BaseException as e:
                print(f"Networking loop terminated with exception {e}")

    def shutdown(self) -> None:
        """Shutdown the masterpiece. It is up to the sub classes to implement this method.
        Dispatches the call to `payload` object.
        """
        if self.payload is not None:
            self.payload.shutdown()

    @classmethod
    def classattrs_to_dict(cls):
        """Convert class attributes to a dictionary."""
        return {
            attr: getattr(cls, attr)
            for attr in cls.__dict__
            if not callable(getattr(cls, attr))
            and not attr.startswith("__")
            and not attr.startswith(("_"))
        }

    @classmethod
    def classattrs_from_dict(cls, attributes):
        """Set class attributes from a dictionary."""
        for key, value in attributes.items():
            setattr(cls, key, value)

    @classmethod
    def save_to_json(cls):
        """Create class configuration file, if the file does not exist yet."""
        filename = cls.get_json_file()
        if not os.path.exists(filename):
            with open(cls.get_json_file(), "w", encoding="utf-8") as f:
                json.dump(cls.classattrs_to_dict(), f)
                if cls._log is not None:
                    cls._log.info(f"Configuration file {filename} created")

    @classmethod
    def load_from_json(cls):
        """Load class attributes from a JSON file."""
        try:
            filename = cls.get_json_file()
            with open(filename, "r", encoding="utf-8") as f:
                attributes = json.load(f)
                cls.classattrs_from_dict(attributes)
        except FileNotFoundError:
            if cls._log is not None:
                cls._log.info(f"No configuration file {filename} found")

    @classmethod
    def register_class(cls, class_id: str, ctor: Callable):
        """Register the given class identifier for identifier based
        instantiation . This, factory method pattern, as it is called,
        decouples the actual implementation from the interface.  For more
        information see :meth:`instantiate` method.

        Args:
            class_id (str): class identifier
            ctor  (function): constructor
        """
        cls._factory[class_id] = ctor

    @classmethod
    def get_registered_classes(cls) -> dict:
        """Get the dictionary holding the registered class identifiers and
        the corresponding classes.

        Returns:
            dict: dictionary of class identifier - class pairs
        """
        return cls._factory

    @classmethod
    def instantiate(cls, class_id: str) -> MasterPiece:
        """Create an instance of the class corresponding to the given class identifier.
        This method implements the factory method pattern, which is essential for a
        plugin architecture.

        Args:
            class_id (int): Identifier of the class to instantiate.

        Returns:
            obj: An instance of the class corresponding to the given class identifier.
        """
        if class_id in cls._factory:
            return cls._factory[class_id]()
        else:
            raise ValueError(f"Attempting to instantiate unregistered class {class_id}")

    @classmethod
    def find_class(cls, class_id: str) -> object:
        """Given class identifier find the registered class. If no class with
        the give identifier exists return None.

        Args:
            class_id (int): class identifier

        Returns:
            obj (obj): class or null if not registered
        """
        if class_id in cls._factory:
            return cls._factory[class_id]
        else:
            return None

    @classmethod
    def instantiate_with_param(cls, class_id: str, param: Any) -> MasterPiece:
        """Given class identifier and one constructor argument create the
        corresponding object.

        Args:
            class_id : class identifier
            param : class specific constructor parameter

        Returns:
            obj : instance of the given class.
        """
        return cls._factory[class_id](param)

    @classmethod
    def has_class_method_directly(cls, method_name: str) -> bool:
        """
        Check if the method is in the class's own dictionary
        """
        if method_name in cls.__dict__:
            method = cls.__dict__[method_name]
            # Check if it's a method and if it's a class method
            if isinstance(method, classmethod):
                return True
        return False

    @classmethod
    def register_args(cls, parser: argparse.ArgumentParser) -> None:
        """Register startup arguments to be parsed.

        Args:
            parser (argparse.ArgumentParser): parser to add the startup arguments.
        """

    @classmethod
    def parse_args(cls) -> None:
        """Parse registered startup arguments.

        Args:
            parser (argparse.ArgumentParser): parser to add the startup arguments.
        """

        args: Args = cls._arg_parser.parse_args(namespace=Args())
        for c in cls._factory:
            cls._factory[c].configure_args(args)

    @classmethod
    def configure_args(cls, args: Args) -> None:
        """Register startup arguments to be parsed.

        Args:
            parser (argparse.ArgumentParser): parser to add the startup arguments.
        """


# Register MasterPiece manually since __init_subclass__() won't be called on it.
MasterPiece.register()
