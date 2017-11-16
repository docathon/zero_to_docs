Adding a new file to our documentation
======================================

Now that our site structure is ready to go, let's add a page to our documentation. This should
give you an idea for how to add new content to the site.

Each section below is a file we'll create and add t othe documentation.

``API.rst``
-----------
We'll generate a single new page for our API reference, called ``API.rst``. The file should
contain the following text::


    API Reference
    =============

    .. automodule:: my_package
       :members:


``overview.rst``
----------------
We'll also generate a short overview document that gives more
detail about the project. Paste in this text::

    Overview
    ========

    This is the example documentation for a fictitious piece of software called
    `my_package`.

    The example shows how to:

    - Include `NumPy-style docstrings <https://github.com/numpy/numpydoc>`__.
    - Generate a `Sphinx gallery <https://github.com/sphinx-gallery/sphinx-gallery>`__.


``awesomepage.rst``
-------------------

To show off some other cool things that sphinx can do, we'll add in an extra
page with a little more pizzaz.::

    What a great page
    =================

    This page, truly, is the greatest page on the internet.

    See, we've even got `David Bowie <https://www.youtube.com/watch?v=iYYRH4apXDo>`_.

    as well as pictures of cute cats

    .. image::  https://lh6.ggpht.com/sw_iT7GZASdAYeiecsZEHJE-EgDhdK2rCWUzZOJS0OFiGpoi9qn8iMH2nuXHgWg2PA=h900
       :align:   center
       :target: https://en.wikipedia.org/wiki/Cat/

Edit the index file
===================

Now that we've added pages, we also need to add a reference to them in our site's
table of contents. We'll add a line for each page to the TOC (inside ``index.rst``)
so that the section looks like this::

    Contents:

    .. toctree::
       :maxdepth: 2

       API
       overview
       awesomepage

.. note:: Make sure all the page names are indented to the same level as the ``:`` above.
