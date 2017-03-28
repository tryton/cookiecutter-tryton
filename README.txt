===================
cookiecutter-tryton
===================

Cookiecutter_ template for a Tryton module

(requires cookiecutter >= 1.4.0)

Features
--------

* Vanilla testing setup with `unittest` and `python setup.py test`
* Drone_: Ready for Drone Continuous Integration testing
* Tox_: Setup to easily test for Python (2.7, 3.3, 3.4 and 3.5), PyPy, SQlite,
  PostgreSQL and MySQL

Quickstart
----------

Generate a Tryton module project::

    cookiecutter hg+https://hg.tryton.org/cookiecutter

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Drone: https://github.com/drone/drone
.. _Tox: http://testrun.org/tox
