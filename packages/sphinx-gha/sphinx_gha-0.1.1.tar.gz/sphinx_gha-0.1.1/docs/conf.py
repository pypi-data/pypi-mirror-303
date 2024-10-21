# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from pathlib import Path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx-gha'
copyright = '2024, Andrew Cassidy'
author = 'Andrew Cassidy'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_gha',
    'myst_parser',
    'sphinx_examples',
    'sphinx_copybutton',
    'sphinx.ext.intersphinx'
]
default_role = 'any'

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = []

# -- Options for sphinx-gha --------------------------------------------------

sphinx_gha_repo_root = str(Path(__file__).parent.parent.absolute())  # docs/..
sphinx_gha_repo_slug = 'drewcassidy/sphinx-gha'

# -- Options for myst-parser -------------------------------------------------

myst_heading_anchors = 3
myst_enable_extensions = ['attrs_inline']
