Flake8 TODO plugin
==================

Check for TODO notes.

This module provides a plugin for ``flake8``, the Python code checker.


Installation
------------

You can install or upgrade ``flake8-todo`` with these commands::

  $ pip install flake8-todo
  $ pip install --upgrade flake8-todo


Plugin for Flake8
-----------------

When both ``flake8 2.0`` and ``flake8-todo`` are installed, the plugin is
available in ``flake8``::

    $ flake8 --version
    2.0 (pep8: 1.4.5, mccabe: 0.2, flake8-todo: 0.1, pyflakes: 0.6.1)


Changes
-------

0.7 - 2016-11-15
````````````````

* Relax dependency pinning


0.6 - 2016-08-11
````````````````

* Fixed entry point for flake8 3.0


0.5 - 2016-07-24
````````````````

* Moved from pep8 to pycodestyle


0.4 - 2015-08-06
````````````````

* Show XXX as TODO entry


0.3 - 2013-04-03
````````````````
* Fixed setup for Python 3.


0.2 - 2013-03-26
````````````````
* Use unique entry point (previous version conflicted with mccabe)


0.1 - 2013-03-26
````````````````
* First release
