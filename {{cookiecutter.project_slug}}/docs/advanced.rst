.. _api-{{cookiecutter.project_slug}}.tests.conftest:

========
Advanced
========

Here you can see the technical documentation.

.. automodule:: {{cookiecutter.project_slug}}.tests.conftest
   :members:
   :member-order: bysource

.. automodule:: {{cookiecutter.project_slug}}.config
   :members:
   :member-order: bysource

.. automodule:: {{cookiecutter.project_slug}}.pages.base
   :members:
   :member-order: bysource


BDD tests examples
==================

Here you can see a BDD test example:

.. include:: ../{{cookiecutter.project_slug}}/features/functional/login.feature
   :literal:

where ``Administrator`` stands for the user id.

You have to provide the Administrator ``username`` and ``password``
providing them in the ``credentials_template.yml``. For example:

.. include:: ../credentials_template.yml
   :literal:

