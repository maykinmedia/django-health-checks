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

Running tests
=============

To run the tests without tox, you can do the following (from the root of the repository):

.. code:: bash

    export DJANGO_SETTINGS_MODULE=testapp.settings
    export PYTHONPATH=$PYTHONPATH:`pwd`
    pytest tests