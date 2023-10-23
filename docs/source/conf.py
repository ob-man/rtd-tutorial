# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
]

templates_path = ['_templates']

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = None

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_static_path = ['_static']

latex_elements = {
}

# -- Options for EPUB output
epub_show_urls = 'footnote'

epub_title = project

epub_exclude_files = ['search.html']

html_favicon = "img/favicon.png"