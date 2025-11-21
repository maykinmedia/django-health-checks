

Welcome to Maykin Health Checks' documentation!
===============================================

:Version: 0.1.0
:Source: https://github.com/maykinmedia/django-health-checks
:Keywords: ``Django``, ``Maykin``, ``health checks``
:PythonVersion: 3.12, 3.13

|build-status| |code-quality| |ruff| |coverage| |docs|

|python-versions| |django-versions| |pypi-version|

Library to help with defining and running health checks for Maykin Django projects.

.. contents::

.. section-numbering::


Installation
============

Requirements
------------

* Python 3.12 or above
* Django 4.2 or newer


Install
-------

.. code-block:: bash

    pip install maykin_health_checks


Usage
=====

<document or refer to docs>

Local development
=================

To develop the library locally, use:

.. code-block:: bash

    uv pip install -r pyproject.toml --all-extras

To run the test app, in the root of the repository run:

.. code:: bash

    export DJANGO_SETTINGS_MODULE=testapp.settings
    export PYTHONPATH=$PYTHONPATH:`pwd`

Then, you can run:

.. code:: bash

    django-admin runserver


.. |build-status| image:: https://github.com/maykinmedia/django-health-checks/workflows/Run%20CI/badge.svg
    :alt: Build status
    :target: https://github.com/maykinmedia/django-health-checks/actions?query=workflow%3A%22Run+CI%22

.. |code-quality| image:: https://github.com/maykinmedia/django-health-checks/workflows/Code%20quality%20checks/badge.svg
     :alt: Code quality checks
     :target: https://github.com/maykinmedia/django-health-checks/actions?query=workflow%3A%22Code+quality+checks%22

.. |ruff| image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

.. |coverage| image:: https://codecov.io/gh/maykinmedia/maykin_health_checks/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/maykinmedia/maykin_health_checks
    :alt: Coverage status

.. |docs| image:: https://readthedocs.org/projects/maykin_health_checks/badge/?version=latest
    :target: https://maykin_health_checks.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |python-versions| image:: https://img.shields.io/pypi/pyversions/maykin_health_checks.svg

.. |django-versions| image:: https://img.shields.io/pypi/djversions/maykin_health_checks.svg

.. |pypi-version| image:: https://img.shields.io/pypi/v/maykin_health_checks.svg
    :target: https://pypi.org/project/maykin_health_checks/
