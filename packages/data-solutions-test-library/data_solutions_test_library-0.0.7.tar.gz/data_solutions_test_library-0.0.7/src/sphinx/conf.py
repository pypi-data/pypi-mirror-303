# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "Data Solutions Python SDK"
copyright = "2024, Rah Tarar, Kurt Bugbee"
author = "Rah Tarar, Kurt Bugbee"
release = "0.8.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary",
]

# Optionally, if you want to allow Markdown files to be parsed by Sphinx
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    os.path.abspath("../test/**"),
]

# add_module_names = False  # Remove import paths from modules

autodoc_default_options = {
    "members": True,
    "special-members": "__call__",
    "undoc-membes": True,
    "show-inheritance": True,
    "exclude-members": "exceptions, constants",
    # "imported-members": True,
}

html_theme = "furo"
# html_static_path = ["_static"]

autosummary_generate = False

autodoc_member_order = "bysource"
