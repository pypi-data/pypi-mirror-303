"""
Configuration file for the Sphinx documentation builder.

# TODO: As a professional Python developer (and defnitely a C++ boomer!), I won't 
# copy & paste this into every plugin and project. Implement a "super conf.py"
# from which plugin implementers can derive their specific conf.py files with 
# minimal, relevant plugin-specific information.

 For the full list of built-in configuration values, see the documentation:
https://www.sphinx-doc.org/en/master/usage/configuration.html
"""

import sys
import os
import sphinx_bootstrap_theme

# Sphinx can't find my source code without telling it to look the current folder, really?
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath("../.."))

try:
    from masterpiece.core import Application
    print("Successfully imported Application")
except Exception as e:
    print(f"Failed to import Application: {e}")
    
print("System Path:")
print(sys.path)

# Ensure master_doc is set to 'index'
# TODO: this yields pylint warning about not being upper case, don't sphinx developers know that?
master_doc = "index"


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project: str = "masterpiece"
copyright: str = "2024, juha meskanen"
author: str = "juha meskanen"
html_static_path: list[str] = ["_static"]


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",  # For support of Google and NumPy style docstrings
    "sphinx_autodoc_typehints",
    "sphinx.ext.autodoc",  # For automatic generation of API documentation from docstrings
    "sphinx.ext.intersphinx",  # For cross-referencing to external documentation
    "sphinx.ext.todo",  # For TODO list management
    "sphinx.ext.viewcode",  # For links to the source code
    "sphinx.ext.autosummary",  # For automatic generation of summary tables of contents
    "sphinx.ext.doctest",  # For running doctests in docstrings
    "sphinx.ext.ifconfig",  # For conditional content based on configuration values
    "sphinx.ext.githubpages",  # For publishing documentation to GitHub Pages
    "sphinx.ext.coverage",  # For measuring documentation coverage
    "sphinx.ext.mathjax",  # For rendering math via MathJax
    "sphinx.ext.imgmath",  # For rendering math via LaTeX and dvipng
    "sphinx.ext.inheritance_diagram",  # UML diagrams,
    "sphinxcontrib.plantuml",  # for UML class diagrams
    "sphinxcontrib.mermaid",  # for UML diagrams
]


# platuml
# Path to the PlantUML jar file
plantuml_jar_path: str = "../plantuml.jar"
plantuml = f"java -jar {plantuml_jar_path}"

# for UML diagrams
graphviz_output_format: str = "svg"

napoleon_google_docstring: bool = True
napoleon_numpy_docstring: bool = False
autodoc_inherit_docstrings: bool = False
templates_path: list[str] = ["_templates"]
exclude_patterns: list[str] = []
todo_include_todos: bool = True
pygments_style: str = "sphinx"  # Default syntax highlighting style
highlight_language: str = "python"  # Default language for code blocks


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme: str = "bootstrap"
html_theme_path: str = sphinx_bootstrap_theme.get_html_theme_path()

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# Add any CSS files here, relative to the static path.
# Example: "css/custom.css"
html_css_files = [
    "masterpiece.css",
]

# Additional theme options
# html_theme_options = {
# your other options here
# }
