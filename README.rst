========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-reconfigure/badge/?style=flat
    :target: https://readthedocs.org/projects/python-reconfigure
    :alt: Documentation Status


.. |travis| image:: https://travis-ci.org/egberts/python-reconfigure.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/egberts/python-reconfigure

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/egberts/python-reconfigure?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/egberts/python-reconfigure

.. |requires| image:: https://requires.io/github/egberts/python-reconfigure/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/egberts/python-reconfigure/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/egberts/python-reconfigure/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/egberts/python-reconfigure

.. |version| image:: https://img.shields.io/pypi/v/reconfigure.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/reconfigure

.. |commits-since| image:: https://img.shields.io/github/commits-since/egberts/python-reconfigure/v2.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/egberts/python-reconfigure/compare/v2.0.0...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/reconfigure.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/reconfigure

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/reconfigure.svg
    :alt: Supported versions
    :target: https://pypi.org/project/reconfigure

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/reconfigure.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/reconfigure


.. end-badges

An example package. Generated with cookiecutter-pylibrary.

* Free software: BSD 3-Clause License

Installation
============

::

    pip install reconfigure

Documentation
=============


https://python-reconfigure.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
