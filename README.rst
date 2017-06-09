===============
cookiecutter QA
===============

.. image:: https://readthedocs.org/projects/cookiecutter-qa/badge/?version=latest
          :target: http://cookiecutter-qa.readthedocs.io

This is a (still work in progress) complete rewrite of the tierra_qa_ package
empowered by the Cookiecutter_ scaffolding project.

Until the rewrite has finished please refer to the original tierra_qa_ project meantime.

Usage
=====

Install Cookiecutter_, use ``cookiecutter-qa`` as project template
and bake your new QA package providing some information::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/tierratelematics/cookiecutter-qa
    full_name [Davide Moro]: 
    email [davide.moro@gmail.com]: 
    github_username [tierratelematics]: 
    project_name [Project QA]: 
    project_slug [project_qa]: 
    project_short_description [Project QA contains all the boilerplate you need to create a QA package]: 
    pypi_username [tierratelematics]: 
    version [0.0.1]: 
    create_author_file [y]: 
    Select open_source_license:
    1 - MIT license
    2 - BSD license
    3 - ISC license
    4 - Apache Software License 2.0
    5 - GNU General Public License v3
    6 - Not open source
    Choose from 1, 2, 3, 4, 5, 6 [1]: 
    base_url [http://tierratelematics.com]: 
    browserstack_username [USERNAME]: YOUR_BROWSERSTACK_USERNAME_HERE
    browserstack_access_key [ACCESS_KEY]: YOUR_BROWSERSTACK_ACCESS_KEY_HERE
    $ cd project_qa

As result cookiecutter will create for you a new package.

If you want to launch your hello world Selenium based tests against Browserstack_ you can just
type the following commands::

    $ make docker-build
    $ make docker-run


In the next future you will be able to choose a very basic test example or another one with a
more opinionated stack.

Sponsored by
============

.. image:: http://cookiecutter-qa.readthedocs.io/en/latest/_static/browserstack.svg
     :target: https://www.browserstack.com
     :alt: Browserstack

.. _tierra_qa: https://github.com/tierratelematics/tierra_qa
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Browserstack: https://www.browserstack.com
