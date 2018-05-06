# -*- coding: utf-8 -*-
#
# Project Euler documentation build configuration file, created by
# sphinx-quickstart on Fri Nov 10 15:37:22 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
import sys
# sys.path.insert(0, os.path.abspath('.'))
sys.path.append('./pe001_multiples_of_3_and_5')
sys.path.append('./pe002_even_fibonacci_numbers')
sys.path.append('./pe003_largest_prime_factor')
sys.path.append('./pe004_largest_palindrome_product')
sys.path.append('./pe005_smallest_multiple')
sys.path.append('./pe006_sum_square_difference')
sys.path.append('./pe007_10001st_prime')
sys.path.append('./pe008_largest_product_in_a_series')
sys.path.append('./pe009_special_pythagorean_triplet')
sys.path.append('./pe010_summation_of_primes')
sys.path.append('./pe011_largest_product_in_a_grid')
sys.path.append('./pe012_highly_divisible_triangular_number')
sys.path.append('./pe013_large_sum')
sys.path.append('./pe014_longest_collatz_sequence')
sys.path.append('./pe015_lattice_paths')
sys.path.append('./pe016_power_digit_sum')
sys.path.append('./pe017_number_letter_counts')
sys.path.append('./pe018_maximum_path_sum_i')
sys.path.append('./pe019_counting_sundays')
sys.path.append('./pe020_factorial_digit_sum')
sys.path.append('./pe021_amicable_numbers')
sys.path.append('./pe022_names_scores')
sys.path.append('./pe023_non_abundant_sums')
sys.path.append('./pe024_lexicographic_permutations')
sys.path.append('./pe025_1000-digit_fibonacci_number')
sys.path.append('./pe026_reciprocal_cycles')
sys.path.append('./pe027_quadratic_primes')
sys.path.append('./pe028_number_spiral_diagonals')
sys.path.append('./pe029_distinct_powers')
sys.path.append('./pe030_digit_fifth_powers')
sys.path.append('./pe158_exploring_strings_for_which_only___')
sys.path.append('./pe304_primonacci')
sys.path.append('./pe335_gathering_the_beans')
sys.path.append('./pe358_cyclic_numbers')
sys.path.append('./pe375_minimum_of_subsequences')

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.mathjax']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Project Euler'
copyright = u'2017, Zdenek Nemec'
author = u'Zdenek Nemec'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u'1.0'
# The full version, including alpha/beta/rc tags.
release = u'1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ProjectEulerdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'ProjectEuler.tex', u'Project Euler Documentation',
     u'Zdenek Nemec', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'projecteuler', u'Project Euler Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ProjectEuler', u'Project Euler Documentation',
     author, 'ProjectEuler', 'One line description of project.',
     'Miscellaneous'),
]

html_sidebars = {
   '**': ['localtoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'], 'using/windows': ['windowssidebar.html', 'searchbox.html'],
}
