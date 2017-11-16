Generating a gallery with sphinx-gallery
========================================

``sphinx-gallery`` lets us generate scripts using reStructuredText **alongside python**.
This means that we can include formatting to make it easier to follow our work.
Let's add the next few blocks of code to our trapezoid plot and see how it looks.

Add the following sections of text to the ``plot_trapezoid.py`` file in the examples
folder.::


    ###############################################################################
    # Define our function
    # -------------------
    #
    # Below we'll define a function that we'll integrate
    # $$ 2.2a^3 + .3a^2 + 2a + .1 $$



    ###############################################################################
    # Now plot the function
    # ---------------------
    #
    # Using this function, we'll plot the function itself for a range of
    # points.



    ###############################################################################
    # Finally, plot the area
    # ----------------------
    #
    # Finally we'll show how the area under the curve changes as a
    # function of how many points we use to create the trapezoids.


Changing the chosen gallery image
---------------------------------

We can also manually choose the image we want for the gallery. Add this
comment to the beginning of the script to do so::

    # sphinx_gallery_thumbnail_number = 2

Now build the documentation::

  make html

and open the built page for the trapezoid example::

  ../sphinx_template/docs/build/html/auto_examples/plot_trapezoid.html

.. note::

   We should also update our ``index.rst`` file so that the built gallery shows
   up in our table of contents.::

     auto_examples/index

Adding a subfolder of gallery images
------------------------------------

If we have multiple galleries, we can easily pass them to sphinx-gallery by using
sub-folders in our examples folder. Let's split our two examples into their own folders.

Note that we need to have a `README.txt` file for **each folder**.


Wrapping up
-----------

``sphinx-gallery`` has many more things you can do with it, and we encourage you to check
out their documentation to learn more about this toolbox.

If you want some inspiration, you can `find a list of projects
<https://github.com/sphinx-gallery/sphinx-gallery#who-uses-sphinx-gallery>`_
using ``sphinx-gallery`` on their github readme.
