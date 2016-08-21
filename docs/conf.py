# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst
#
# Astropy documentation build configuration file.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this file.
#
# All configuration values have a default. Some values are defined in
# the global Astropy configuration which is loaded here before anything else.
# See astropy.sphinx.conf for which values are set there.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('..'))
# IMPORTANT: the above commented section was generated by sphinx-quickstart, but
# is *NOT* appropriate for astropy or Astropy affiliated packages. It is left
# commented out with this explanation to make it clear why this should not be
# done. If the sys.path entry above is added, when the astropy.sphinx.conf
# import occurs, it will import the *source* version of astropy instead of the
# version installed (if invoked as "make html" or directly with sphinx), or the
# version in the build directory (if "python setup.py build_docs" is used).
# Thus, any C-extensions that are needed to build the documentation will *not*
# be accessible, and the documentation will not build correctly.

import os
ON_RTD = os.environ.get('READTHEDOCS') == 'True'

try:
    import astropy_helpers
except ImportError:
    # Building from inside the docs/ directory?
    import os
    import sys
    if os.path.basename(os.getcwd()) == 'docs':
        a_h_path = os.path.abspath(os.path.join('..', 'astropy_helpers'))
        if os.path.isdir(a_h_path):
            sys.path.insert(1, a_h_path)

    # If that doesn't work trying to import from astropy_helpers below will
    # still blow up

# We now check for any dependencies that are required to build the docs that
# depend on Astropy, since these may not be installed yet. For instance, on
# ReadTheDocs, we can't set up wcsaxes with conda since that would result in the
# astropy conda package getting installed, which would shadow the developer
# version installed just prior to building the docs. So we should set up any
# such dependencies here.
if ON_RTD:
    from setuptools import Distribution
    Distribution({'setup_requires': 'wcsaxes'})

# Load all of the global Astropy configuration
from astropy_helpers.sphinx.conf import *
from astropy.extern import six

import astropy

# Use the astropy style when building docs
from astropy import visualization
plot_rcparams = visualization.astropy_mpl_docs_style
plot_apply_rcparams = True


# -- General configuration ----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.1'

# To perform a Sphinx version check that needs to be more specific than
# major.minor, call `check_sphinx_version("x.y.z")` here.
check_sphinx_version("1.2.1")

# The intersphinx_mapping in astropy_helpers.sphinx.conf refers to astropy for
# the benefit of affiliated packages who want to refer to objects in the
# astropy core.  However, we don't want to cyclically reference astropy in its
# own build so we remove it here.
del intersphinx_mapping['astropy']

# add any custom intersphinx for astropy
intersphinx_mapping['pytest'] = ('http://pytest.org/latest/', None)
intersphinx_mapping['ipython'] = ('http://ipython.readthedocs.io/en/stable/', None)
intersphinx_mapping['pandas'] = ('http://pandas.pydata.org/pandas-docs/stable/', None)

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns.append('_templates')
exclude_patterns.append('_pkgtemplate.rst')

# Add any paths that contain templates here, relative to this directory.
if 'templates_path' not in locals():  # in case parent conf.py defines it
    templates_path = []
templates_path.append('_templates')


# This is added to the end of RST files - a good place to put substitutions to
# be used globally.
rst_epilog += """
.. |minimum_numpy_version| replace:: {0.__minimum_numpy_version__}

.. Astropy
.. _Astropy: http://astropy.org
.. _`Astropy mailing list`: http://mail.scipy.org/mailman/listinfo/astropy
.. _`astropy-dev mailing list`: http://groups.google.com/group/astropy-dev
""".format(astropy)

# -- Project information ------------------------------------------------------

project = u'Astropy'
author = u'The Astropy Developers'
copyright = u'2011-2016, ' + author

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The short X.Y version.
version = astropy.__version__.split('-', 1)[0]
# The full version, including alpha/beta/rc tags.
release = astropy.__version__


# -- Options for HTML output ---------------------------------------------------

# A NOTE ON HTML THEMES
#
# The global astropy configuration uses a custom theme,
# 'bootstrap-astropy', which is installed along with astropy. The
# theme has options for controlling the text of the logo in the upper
# left corner. This is how you would specify the options in order to
# override the theme defaults (The following options *are* the
# defaults, so we do not actually need to set them here.)

#html_theme_options = {
#    'logotext1': 'astro',  # white,  semi-bold
#    'logotext2': 'py',     # orange, light
#    'logotext3': ':docs'   # white,  light
#    }

# A different theme can be used, or other parts of this theme can be
# modified, by overriding some of the variables set in the global
# configuration. The variables set in the global configuration are
# listed below, commented out.

# Add any paths that contain custom themes here, relative to this directory.
# To use a different custom theme, add the directory containing the theme.
#html_theme_path = []

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes. To override the custom theme, set this to the
# name of a builtin theme or the name of a custom theme in html_theme_path.
#html_theme = None

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = ''

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = ''

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = '{0} v{1}'.format(project, release)

# Output file base name for HTML help builder.
htmlhelp_basename = project + 'doc'


# -- Options for LaTeX output --------------------------------------------------

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [('index', project + '.tex', project + u' Documentation',
                    author, 'manual')]

latex_logo = '_static/astropy_logo.pdf'


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [('index', project.lower(), project + u' Documentation',
              [author], 1)]


# -- Options for the edit_on_github extension ----------------------------------------

extensions += ['astropy_helpers.sphinx.ext.edit_on_github']

# Don't import the module as "version" or it will override the
# "version" configuration parameter
from astropy import version as versionmod
edit_on_github_project = "astropy/astropy"
if versionmod.release:
    edit_on_github_branch = "v{0}.{1}.x".format(
        versionmod.major, versionmod.minor)
else:
    edit_on_github_branch = "master"
edit_on_github_source_root = ""
edit_on_github_doc_root = "docs"

edit_on_github_skip_regex = '_.*|api/.*'

github_issues_url = 'https://github.com/astropy/astropy/issues/'

# Enable nitpicky mode - which ensures that all references in the docs
# resolve.

nitpicky = True
nitpick_ignore = []

for line in open('nitpick-exceptions'):
    if line.strip() == "" or line.startswith("#"):
        continue
    dtype, target = line.split(None, 1)
    target = target.strip()
    nitpick_ignore.append((dtype, six.u(target)))

if six.PY2:
    nitpick_ignore.extend([('py:obj', six.u('bases'))])

# -- Options for the Sphinx gallery -------------------------------------------

try:
    import sphinx_gallery
    extensions += ["sphinx_gallery.gen_gallery"]

    sphinx_gallery_conf = {
        'mod_example_dir': 'generated/modules', # path to store the module using example template
        'filename_pattern': '^((?!skip_).)*$', # execute all examples except those that start with "skip_"
        'examples_dirs': '..{}examples'.format(os.sep), # path to the examples scripts
        'gallery_dirs': 'generated/examples', # path to save gallery generated examples
        'reference_url': {
            'astropy': None,
            'matplotlib': 'http://matplotlib.org/',
            'numpy': 'http://docs.scipy.org/doc/numpy/',
        },
        'abort_on_example_error': False
    }

    # TODO: remove the code below once a better solution is implemented in
    # sphinx-gallery.
    # We want to make sure that gallery examples fail the build if there are
    # any errors, when building the docs with the option to fail if there are
    # any warnings. However, at the moment, we can only either fail the build
    # completely or not fail it at all, until this is fixed properly in
    # sphinx-gallery: https://github.com/sphinx-gallery/sphinx-gallery/pull/97
    # Therefore, for now we simply check if we are on Travis, and if so, we
    # enabled the abort_on_example_error.
    if os.environ.get('TRAVIS', 'false') == 'true':
        sphinx_gallery_conf['abort_on_example_error'] = True

except ImportError:
    def setup(app):
        app.warn('The sphinx_gallery extension is not installed, so the '
                 'gallery will not be built.  You will probably see '
                 'additional warnings about undefined references due '
                 'to this.')
