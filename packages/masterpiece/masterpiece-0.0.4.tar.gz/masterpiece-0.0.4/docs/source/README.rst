Welcome to MasterPiece - A Piece of Work
========================================

A compact and unified set of general purpose Python classes for writing 
plugin aware, object oriented applications. 



Project Status and Current State
--------------------------------

The framework is in its early development phase.

Here's what is currently available:

* Package Infrastructure: The basic Python package setup is in place, configured with 'pyproject.toml'.
* Early Drafts: Initial yet fully working versions of the essential core classes implemented.
* Example application 'examples/myhome.py', which prints out its instance structure when run.
* A plugin package named 'masterpiece_plugin' plugging in 'Hello World' greeting to 'myhome.py', demonstrating minimal yet complete and 
  fully functional plugin.

Tn this current state, you might call the project merely a mission, rather than masterpiece, but I'm
working hard to turn it into a masterpiece!



Goals
-----

The key objectives of this framework include:

* Robusness: Minimal yet robust API providing the developer with 100% control.
* First-Time Excellence: The aim is to build a robust and reliable framework that is correct and efficient from the start,
  eliminating the need for disruptive changes or backward compatibility issues in future releases.
* Abstraction: Provide a layer of abstraction to shield the API from the impacts of external code, including
  third-party libraries and APIs. 



Design
------

The design patterns employed to achieve the goals include:

* Object-Oriented Paradigm
* Factory Method Pattern
* Layered Design Pattern
* Plugin API
* [ More later, too busy now ] 


If you appreciate these design concepts, you've come to the right place!


About the project name
----------------------

Just as all creatures on Earth share a common ancestor, all components in this framework trace their lineage
back to this foundational anchestor named "masterpiece" ... (okay, perhaps a bit too dramatic).

The name 'MasterPiece' was chosen to reflect commitment to fine-grained modular design ("pieces"), with
a touch of humour.  Masterpiece is an object, a piece of work, actually a piece of data, designed to master something,
like ones home automation.



Install
-------

1. To install the masterpiece:

   `pip install masterpiece`.

2. To install the demo-plugin:

  `pip install masterpiece_plugin`

3. To run:
::

    cd masterpiece/examples
    python myapp.py



The minimum Python version known to work is 3.8.




Developer Documentation
-----------------------

Getting better, but will reguire a few more hours (okay, days) of effort to produce something really usable.



Special Thanks
--------------

My ability to translate my architecture ideas into this Python framework is greatly due to the generous support of an
extraordinary gentleman: [Mahi.fi](https://mahi.fi).


Anything else?
--------------

Can't think of ..
