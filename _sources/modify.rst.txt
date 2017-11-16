Customizing the index file
==========================

What is rST?
------------

You may notice the new extension here, ``rst``.

``.rst`` stands for reStructuredText. This is a language for structuring text such that it can be used
to generate beautiful HTML output.

* `Here's a good guide <http://www.sphinx-doc.org/en/stable/rest.html#rst-primer>`_ on learning about the rST language
* `Here's a cheatsheet <http://docutils.sourceforge.net/docs/user/rst/cheatsheet.txt>`_ with some simple rST examples
* `Here's an app <http://rst.ninjs.org/>`_ to quickly demo what your rST will look like.

Updating our index file
-----------------------

Let's see what this looks like below. Note the peculiar way in which the text is structured.
This is what allows sphinx to parse it properly.

Comparing the two, we can see how `rst` files define things like titles (with ``=======``, ``-------``, or some
version of this). We also see how it is possible to point to other pages with ``:ref:``.
These links point to other parts of the sphinx website.
