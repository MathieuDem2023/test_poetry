import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

project = 'Test poetry'
copyright = '2023, MathieuDem2023'
author = 'MathieuDem2023'
release = "0.1.0"
version = "0.1.0"

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    "sphinx_copybutton",
    "sphinx_togglebutton",
    'sphinx.ext.napoleon'
    ]

source_suffix = ['.rst','.md']
templates_path = ['_templates']
exclude_patterns = []

html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_title = project

html_theme_options = {
    "logo": {
        "text": project,
    },
    "header_links_before_dropdown": 7,
    "footer_start": ["copyright"],
    "footer_end": ["sphinx-version", "theme-version"],
}

html_sidebars = {
    "**": ["sidebar-nav-bs"]
}