Hosting your documentation
==========================

readthedocs
-----------
readthedocs provides free hosting for documentation, they've also got a lot
of useful features for keeping multiple versions of your documentation online
simultaneously.

<TODO add more info>

Doctr: Deploying documentation on GhPages
-----------------------------------------
This is a quick guide to auto-deploying documentation on gh-pages using Travis. You can find a
sister repository with a template that can be used to build your own documentation here:

* https://github.com/choldgraf/sphinx_template

First, install Doctr on your local machine::

 pip install doctr

Next, we'll enable Travis Continuous Integration so that it works on your repo.

Go to ``https://travis-ci.org/profile/<Your username>`` and enable your repository.


Setting up doctr
~~~~~~~~~~~~~~~~

Doctr has a quickstart configuration similar to ``sphinx-quickstart``. To use this,
navigate to your documentation folder and run::

  doctr configure

Doctr will then ask you several questions that it uses to authenticate
with your GitHub account. Once you've answered these questions, Doctr
will output instructions on what to do next.
