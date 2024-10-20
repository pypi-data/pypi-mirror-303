Masterpiece
===========

Welcome to **Masterpiece™ - Quite a Piece of Work**. Masterpiece™ is a **Python framework** designed for creating scalable, plugin-aware, multi-threaded, and object-oriented applications. (Yes, multi-threading! Python’s Global Interpreter Lock (GIL) might raise an eyebrow, but I trust the community will address that soon™.)

The toolkit is essentially a tree container, providing core classes for building applications with a hierarchical structure, allowing any payload to be integrated into the hierarchy. It supports configuration, serialization, the factory method pattern, a plugin API, and many other features commonly required when developing applications.

If you appreciate these design concepts, look no further. You've come to the right place!

Quick Introduction
------------------

Masterpiece introduces two Python projects/packages:

1. **Masterpiece (core toolkit)**:  
   This is the core toolkit for building plugin-aware, multi-threaded applications. It includes a simple example application to get you started.

2. **Masterpiece Plugin (plugin example)**:  
   This is a basic plugin example that demonstrates how to create third-party plugins for applications built using Masterpiece. It’s as simple as saying **"Hello, World!"**, literally.

Note: This project contains only the core toolkit. The plugin is provided as a separate project.

Example Usage
-------------

Step 1: Install Masterpiece and run the example application
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To install the core toolkit:

.. code-block:: bash

    pip install masterpiece

Then, navigate to the example folder and run the application:

.. code-block:: bash

    python examples/myapp.py

The application will print out the instance hierarchy of the app. This is a minimal starting point for developing your own multi-threaded, plugin-based, scalable applications.

Example output:

.. code-block:: text

    home
        ├─ grid
        ├─ downstairs
        │   └─ kitchen
        │       ├─ oven
        │       └─ fridge
        └─ garage
            └─ EV charger

The application also demonstrates the usage of startup arguments. If you start the application with the '-s 10' argument, a new object named 'Solar plant 10kW' will appear in the hierarchy.

Step 2: Install the Masterpiece Plugin
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To extend the application with the **masterpiece_plugin**:

.. code-block:: bash

    pip install masterpiece_plugin

Run the application again:

.. code-block:: bash

    python examples/myapp.py

You'll now see a new object in the instance hierarchy, along with a friendly "Hello, World!" object.

Example output:

.. code-block:: text

    home
        ├─ grid
        ├─ downstairs
        │   └─ kitchen
        │       ├─ oven
        │       └─ fridge
        ├─ garage
        │   └─ EV charger
        └─ Hello World - A Plugin

The **HelloWorldPlugin** class is a basic starting point for building more sophisticated plugins.

Origin
------

The project has evolved from two distinct projects: RTE (Real Theory of Everything) and JUHAM (Juha's Ultimate Home Automation Masterpiece).

**RTE** is, without a doubt, the most complex project I’ve ever written — it tackles the biggest problem of all (and that’s no exaggeration). On the other hand, **JUHAM** might just be the simplest thing I’ve ever coded — it powered my home automation system, managing things like heating radiators to minimize the electricity bill.

Despite their differences in scale, these two projects shared some common, reusable classes. So, I decided to extract those classes and turn them into a standalone toolkit. You might find it useful, even if your project doesn’t involve solving the universe's mysteries or managing your living room lights.

Contributing
------------

Contributions are welcome!

Please check out the `CONTRIBUTING <CONTRIBUTING.rst>`_ file and the `Issue Board <https://gitlab.com/juham/masterpiece/-/boards>`_ for tracking progress and tasks.

Project Status and Current State
--------------------------------

Here's what is currently available:

* Absolutely bug-free (just kidding) — no known bugs remain, as far as I can tell.
* Package Infrastructure: The basic Python package setup is in place, configured with 'pyproject.toml'.
* Early Drafts: Initial, yet fully working, versions of the essential core classes implemented.
* Example application 'examples/myhome.py', which prints out its instance structure when run.
* A separate plugin project named 'masterpiece_plugin' plugs in a 'Hello World' greeting to 'myhome.py', demonstrating a minimal yet fully functional plugin.

In its current state, you might call the project a "mission" rather than a "masterpiece," but I'm working hard to turn it into the latter!

Goals
-----

The key objectives of this framework include:

* No deprecated API in future releases.
* Robustness: A minimal yet robust API providing developers with 100% control.
* First-Time Excellence: The aim is to build a reliable framework that is correct and efficient from the start, avoiding disruptive changes or backward compatibility issues in future releases.
* Abstraction: Provide a layer of abstraction to shield the API from the impacts of external code, including third-party libraries and APIs.

About the Project
-----------------

Just as all creatures on Earth share a common ancestor, all components in this framework trace their lineage back to this foundational "ancestor" named "masterpiece" ... (okay, perhaps that’s a bit dramatic).

The name 'Masterpiece' was chosen to reflect a commitment to fine-grained modular design ("pieces"), with a touch of humor.

Developer Documentation
-----------------------

As a C/C++ boomer, Doxygen was naturally my tool of choice. However, I ditched it in favor of Python's native tool, Sphinx. The migration wasn’t exactly pure joy—there were several moments of frustration—but it's all good now. The documentation is improving, though it will still require a few more hours (okay, days) of effort to become truly usable.

For full documentation and usage details, see the full documentation at `Documentation Index <docs/build/html/index.html>`_ (it doesn't work yet, I believe I still have some issues mastering Sphinx).

Special Thanks
--------------

My ability to translate my architecture ideas into this Python framework is greatly due to the generous support of an extraordinary gentleman: [Mahi.fi](https://mahi.fi).
