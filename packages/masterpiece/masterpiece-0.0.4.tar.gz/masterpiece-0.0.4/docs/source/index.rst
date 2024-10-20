Welcome to MasterPiece documentation!
=====================================

.. image:: _static/masterpiece.png
    :alt: Masterpiece - A Piece of Work
    :width: 400px
    :height: 300px

.. toctree::
   :maxdepth: 2
   :caption: Contents:


   README
   CHANGELOG
   LICENSE
   CONTRIBUTING
   TODO
   masterpiece/index




Classes
-------

.. inheritance-diagram:: masterpiece.core.MasterPiece masterpiece.core.Composite masterpiece.core.Application masterpiece.core masterpiece.core.Plugin masterpiece.core.PlugMaster
   :parts: 1



Instances
---------

Instances of these classes can be grouped into hierarchical structure to model real world apparatuses.


Instance Diagram
----------------

(Just a test to play with mermaid)

.. mermaid::

   classDiagram
       class MainCompositeObject {
           MasterPiece1: MasterPiece
           SubCompositeObject: SubCompositeObject
       }
       class SubCompositeObject {
           SubMasterPiece1: MasterPiece
           SubMasterPiece2: MasterPiece
       }
       MainCompositeObject --> MasterPiece1 : contains
       MainCompositeObject --> SubCompositeObject : contains
       SubCompositeObject --> SubMasterPiece1 : contains
       SubCompositeObject --> SubMasterPiece2 : contains


Index
=====

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
