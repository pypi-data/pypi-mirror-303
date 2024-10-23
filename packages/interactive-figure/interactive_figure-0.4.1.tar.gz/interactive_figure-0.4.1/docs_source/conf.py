# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Interactive Figure'
# copyright = 'Teun Mathijssen, https://github.com/teuncm/interactive-figure'
author = 'Teun Mathijssen'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_rtd_theme', 'autoapi.extension']
autoapi_dirs = ['../src/interactive_figure']
# autoapi_options = ['members', 'show-module-summary', 'undoc-members']

autoapi_options = ['show-module-summary', 'undoc-members']

# templates_path = ['_templates']
exclude_patterns = []

add_module_names = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'sphinx_rtd_theme'
# html_theme = 'furo'
# html_static_path = ['_static']

html_theme = 'sphinx_book_theme'

# html_theme_options = {
#     "hide_sidebar": True
# }