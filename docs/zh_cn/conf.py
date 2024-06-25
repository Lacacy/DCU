#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# -- Project information

import os
import sys

# import pytorch_sphinx_theme
from m2r import MdInclude
from recommonmark.transform import AutoStructify
from sphinx.builders.html import StandaloneHTMLBuilder

sys.path.insert(0, os.path.abspath('../..'))

version_file = '../../version.py'
with open(version_file, 'r') as f:
    exec(compile(f.read(), version_file, 'exec'))
__version__ = locals()['__version__']

project = 'DCU'
copyright = '2024-now, DCU User'
author = 'DCU User'

# The short X.Y version
version = __version__
# The full version, including alpha/beta/rc tags
release = __version__




intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']



# -- General configuration
# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

#todo orginal
# extensions = [
#     'sphinx.ext.duration',
#     'sphinx.ext.doctest',
#     'sphinx.ext.autodoc',
#     'sphinx.ext.autosummary',
#     'sphinx.ext.intersphinx',
# ]

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel',
    'sphinx_tabs.tabs',
    'sphinx_markdown_tables',
    'myst_parser',
    'sphinx_copybutton',
    'sphinxcontrib.mermaid'
]  # yapf: disable


# 用于 Sphinx 文档构建系统中的配置项，它允许项目之间的交叉引用。这个功能使得文档作者可以在一个项目的文档中轻松引用另一个项目的文档中的对象（如函数、类或术语），从而提高文档的一致性和便利性
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}


#todo original
# intersphinx_disabled_domains = ['std']
# templates_path = ['_templates']
# -------------------------------------------------------
autodoc_mock_imports = []
autosectionlabel_prefix_document = True  # 自动生成前缀
intersphinx_disabled_domains = ['std']
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']


# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

#! The master toctree document.
# master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
# Sphinx 文档构建配置中的一个列表，用于指定在文档构建过程中需要排除的文件或目录模式
# 避免构建错误、提升构建效率、保持文档纯净
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# ----------------------- Options for HTML output -----------------------

# html_theme = 'sphinx_rtd_theme'
html_theme = 'sphinx_rtd_theme'
# html_theme = 'pytorch_sphinx_theme'
# html_theme_path = [pytorch_sphinx_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {
#     'logo_url': 'https://dcu.readthedocs.io/zh-cn/latest/',
#     'menu': [{
#         'name': 'GitHub',
#         'url': 'https://github.com/lacacy/DCU'
#     }],
#     'menu_lang': 'cn',
# }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']
# html_css_files = ['css/readthedocs.css']

# Enable ::: for my_st
# myst_enable_extensions = ['colon_fence']
# myst_heading_anchors = 5

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'DCU Doc'


# --------------------------------------------------------------------------------------------

# -- Options for LaTeX output ------------------------------------------------

#! latex_elements = {
#     # The paper size ('letterpaper' or 'a4paper').
#     #
#     # 'papersize': 'letterpaper',

#     # The font size ('10pt', '11pt' or '12pt').
#     #
#     # 'pointsize': '10pt',

#     # Additional stuff for the LaTeX preamble.
#     #
#     # 'preamble': '',

#     # Latex figure (float) alignment
#     #
#     # 'figure_align': 'htbp',
# }

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# !latex_documents = [
#     (master_doc, 'DCU.tex', 'DCU Documentation',
#      'DCU Contributors', 'manual'),
# ]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# !man_pages = [(master_doc, 'DCU', 'DCU Documentation', [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
# !texinfo_documents = [
#     (master_doc, 'DCU', 'DCU Documentation', author, 'DCU',
#      'One line description of project.', 'Miscellaneous'),
# ]

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
# -- Options for EPUB output
epub_show_urls = 'footnote'

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# --------------------------------------------------------------


# set priority when building html
# StandaloneHTMLBuilder.supported_image_types = [
#     'image/svg+xml', 'image/gif', 'image/png', 'image/jpeg'
# ]

# -- Extension configuration -------------------------------------------------
# Ignore >>> when copying code
copybutton_prompt_text = r'>>> |\.\.\. '
copybutton_prompt_is_regexp = True


# def setup(app):
#     app.add_config_value('no_underscore_emphasis', False, 'env')
#     app.add_config_value('m2r_parse_relative_links', False, 'env')
#     app.add_config_value('m2r_anonymous_references', False, 'env')
#     app.add_config_value('m2r_disable_inline_math', False, 'env')
#     app.add_directive('mdinclude', MdInclude)
#     app.add_config_value('recommonmark_config', {
#         'auto_toc_tree_section': 'Contents',
#         'enable_eval_rst': True,
#     }, True)
#     app.add_transform(AutoStructify)
