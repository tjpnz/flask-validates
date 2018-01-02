import os
import sys
sys.path.append(os.path.abspath(".."))
sys.path.append(os.path.abspath("_themes"))


# -- General configuration ------------------------------------------------
extensions = ["sphinx.ext.autodoc"]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
pygments_style = "sphinx"

project = "Flask-Validates"
copyright = "2018, Thomas Prebble"
author = "Thomas Prebble"
version = "0.2.0"
release = "0.2.0"


# -- Options for HTML output ----------------------------------------------
html_theme_options = dict(
    github_fork="tjpnz/flask-validates",
    index_logo=False
)
html_theme_path = ["_themes"]
html_theme = "flask_small"
html_static_path = ["_static"]
