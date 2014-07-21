# -*- coding: utf-8 -*-
import os
import pkg_resources

try:
    import sphinx_rtd_theme
except ImportError:
    sphinx_rtd_theme = None


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage']

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'pytest-django-casperjs'
copyright = u'2014, Christopher Grebs'

dist = pkg_resources.get_distribution('pytest-django-casperjs')

version = release = dist.version

exclude_patterns = []

pygments_style = 'sphinx'

if sphinx_rtd_theme:
    html_theme = "sphinx_rtd_theme"
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
else:
    html_theme = "default"

html_static_path = ['_static']

htmlhelp_basename = 'pytest-django-casperjsdoc'

latex_elements = {}

latex_documents = [
    ('index', 'pytest-django-casperjs.tex', u'pytest-django-casperjs Documentation',
     u'pytest-django-casperjs', 'manual'),
]

man_pages = [
    ('index', 'pytest-django-casperjs', u'pytest-django-casperjs Documentation',
     [u'pytest-django-casperjs'], 1)
]

texinfo_documents = [
    ('index', 'pytest-django-casperjs', u'pytest-django-casperjs Documentation',
     u'pytest-django-casperjs', 'pytest-django-casperjs', 'Integrate CasperJS with your django tests as a pytest fixture.',
     'Miscellaneous'),
]

epub_title = u'Integrate CasperJS with your django tests as a pytest fixture.'
epub_author = u'Christopher Grebs'
epub_publisher = u'Christopher Grebs'
epub_copyright = u'2014, Christopher Grebs'

intersphinx_mapping = {'http://docs.python.org/': None}
