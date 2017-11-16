# Zero to Docs

A step by step guide to set up your own documentation. This repository
contains the documentation for the guide, as well as an example sphinx
repository to demonstrate how finished documentation looks.

The Zero to Docs guide can be found here:

https://docathon.github.io/zero_to_docs/

## sphinx_template

This folder has materials to help you go from zero to full
documentation as quickly as possible.

The folder is essentially a self-contained repository, including its
own documentation folder. It contains the following directories:

* docs/
  * The Sphinx source of the documentation.
* my_package/
  * An example Python package.  We'll grab docstrings from this package and
  generate documentation for it.
* examples/
  * Visual examples that illustrate the use of `my_package`.  These examples
  will be turned into a gallery.

Of particular interest may be the `docs/source/conf.py` file, which is used to
configure Sphinx.

The documentation may be built by doing:

```
cd sphinx_template/docs
make html
```
