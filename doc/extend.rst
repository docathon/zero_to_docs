Extending your Sphinx setup
===========================

This page covers some common ways to improve upon your Sphinx documentation. Most
of this is accomplished with sphinx plugins and modifications to
your documentation's configuration files.

Adding references between your modules
--------------------------------------

Sometimes you want to reference something without having to manually specify a URL.
In this case, we can use intersphinx to make this easy. This lets us specify a reference
by name, or by reference to a python module / function.

To add references for specific words
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add the following to ``conf.py``::

    intersphinx_mapping = {'python': ('https://docs.python.org/3/', None),
                           'matplotlib': ('http://matplotlib.org/', None)
    }


To add references to a function or module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Try adding the following to the bottom of a docstring for one of our functions::

    :any:`os.environ`

Next we need to tell sphinx to generate the documentation for our API::

    sphinx-apidoc my_package -o docs/source

Now, when we generate the site, it should automatically link to our own functions.

Using autosummary with sphinx
-----------------------------

Autosummary (and a similar plugin called ``autodoc``) is useful for automatically
generating API documentation for your functions, classes, etc. Setting up autosummary
involves activating a sphinx plugin. TODO

- Add an `automodule` entry for the module you wish to document (see
  [sphinx_template](https://raw.githubusercontent.com/choldgraf/sphinx_template/master/docs/source/API.rst)).
