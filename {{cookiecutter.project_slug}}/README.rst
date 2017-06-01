=========
{{cookiecutter.project_slug}}
=========

.. image:: https://travis-ci.org/tierratelematics/{{cookiecutter.project_slug}}.svg?branch=master
       :target: https://travis-ci.org/tierratelematics/{{cookiecutter.project_slug}}

.. image:: https://requires.io/github/tierratelematics/{{cookiecutter.project_slug}}/requirements.svg?branch=master
       :target: https://requires.io/github/tierratelematics/{{cookiecutter.project_slug}}/requirements/?branch=master

.. image:: https://readthedocs.org/projects/{{cookiecutter.project_slug}}/badge/?version=latest
       :target: http://{{cookiecutter.project_slug}}.readthedocs.io

.. image:: https://codecov.io/gh/tierratelematics/{{cookiecutter.project_slug}}/branch/master/graph/badge.svg
       :target: https://codecov.io/gh/tierratelematics/{{cookiecutter.project_slug}}

.. image:: https://api.codacy.com/project/badge/Grade/0698c7aa2e164ee996518737aad7d6f4
       :target: https://www.codacy.com/app/davide-moro/{{cookiecutter.project_slug}}?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=tierratelematics/{{cookiecutter.project_slug}}&amp;utm_campaign=Badge_Grade



``{{cookiecutter.project_slug}}`` is a package that aims to find a new repeatable pattern for 
QA testing applied to any web application.

It is internally based on:

* `pytest`_
* `pytest_splinter`_
* `pytest_bdd`_
* `PyPOM`_
* `pypom_form`_


Why py.test
===========

``py.test`` is a Python test framework that provides a clever dependency injection
mechanism for fixture management with strong focus on reusability and modularity.

Know more:

* http://pytest.org
* https://pytest.org/latest/fixture.html
* https://pytest.org/latest/example/markers.html
* https://pytest.org/latest/example/simple.html

How to install it
=================

Prerequisites:

* python-dev
* virtualenv
* Firefox (requires geckodriver), Chrome, etc

Clone the ``{{cookiecutter.project_slug}}`` package and run::

    $ pip install -r requirements.txt
    $ pip install -r tests_requirements.txt
    $ python setup.py develop

How to use it
=============

Once installed you can launch tests with::

    $ tox -epy36 -- --variables credentials_template.yml

With the ``--variables`` parameter you can read user credentials from a YAML file like that::

    credentials:
      USERID1:
        username: USERNAME1
        password: PASSWORD1

where:

* *USERID1*, stands for the user identifier used in test cases
* *USERNAME1*, stands for the username used for login
* *PASSWORD1*, password associated to the above username

The YAML file 'credentials_template.yml' has to be considered only a template for credentials and we
*stronlgy* suggest to do not put credential files under version control.
If you use Travis CI (http://travis-ci.org/) you can encrypt files with sensible information:

* https://docs.travis-ci.com/user/encrypting-files/

.. _pytest: http://doc.pytest.org
.. _pytest_splinter: http://pytest-splinter.readthedocs.io
.. _pytest_bdd: http://pytest-bdd.readthedocs.io
.. _PyPOM: http://pypom.readthedocs.io
.. _pypom_form: http://pypom-form.readthedocs.io
