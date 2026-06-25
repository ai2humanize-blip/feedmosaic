import os
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = "feedmosaic"
author = "feedmosaic contributors"
copyright = "2026, feedmosaic contributors"
release = "0.3.0"
version = "0.3"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
]

autodoc_typehints = "description"
autodoc_member_order = "bysource"
napoleon_google_docstring = True
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_title = "feedmosaic"
html_static_path = []
