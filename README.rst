===============
cookiecutter QA
===============

.. image:: https://pyup.io/repos/github/tierratelematics/cookiecutter-qa/shield.svg
     :target: https://pyup.io/repos/github/tierratelematics/cookiecutter-qa/
     :alt: Updates

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
    project_name [Project QA]: 
    project_slug [project_qa]: 
    project_short_description [Project QA contains all the boilerplate you need to create a QA package]: 
    version [0.0.1]: 
    create_author_file [y]: 
    Select open_source_license:
    1 - MIT license
    2 - BSD license
    3 - ISC license
    4 - Apache Software License 2.0
    5 - GNU General Public License v3
    6 - Not open source
    Choose from 1, 2, 3, 4, 5, 6 [1]: 4
    ...

As result cookiecutter will create for you a new package.

You will be able to choose a very basic setup or a more opinionated stack.

Sponsored by
============

.. image:: https://raw.githubusercontent.com/tierratelematics/cookiecutter-qa/master/docs/_static/browserstack.eps
     :target: https://raw.githubusercontent.com/tierratelematics/cookiecutter-qa/master/docs/_static/browserstack.svg
     :alt: Browserstack

.. _tierra_qa: https://github.com/tierratelematics/tierra_qa
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
