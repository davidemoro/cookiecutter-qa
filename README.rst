===============
cookiecutter QA
===============

.. image:: https://travis-ci.org/tierratelematics/cookiecutter-qa.svg?branch=master
       :target: https://travis-ci.org/tierratelematics/cookiecutter-qa

.. image:: https://pyup.io/repos/github/tierratelematics/cookiecutter-qa/shield.svg
       :target: https://pyup.io/repos/github/tierratelematics/cookiecutter-qa/
       :alt: Updates

.. image:: https://pyup.io/repos/github/tierratelematics/cookiecutter-qa/python-3-shield.svg
       :target: https://pyup.io/repos/github/tierratelematics/cookiecutter-qa/
       :alt: Python 3

.. image:: https://readthedocs.org/projects/cookiecutter-qa/badge/?version=latest
       :target: http://cookiecutter-qa.readthedocs.io

.. image:: https://www.browserstack.com/automate/badge.svg?badge_key=cUZrc0xQdENBOTAyNnU0Zy9RZ3oxMUovalh0UTZ6VFpWT2J0RkxkUW5Rcz0tLWpJL2lkcEptbHdmSEN4WEZ0RGZ1dmc9PQ==--0a9b15d748993f1a0079f3256baa9e8348457ca4
       :target: https://www.browserstack.com/automate/public-build/cUZrc0xQdENBOTAyNnU0Zy9RZ3oxMUovalh0UTZ6VFpWT2J0RkxkUW5Rcz0tLWpJL2lkcEptbHdmSEN4WEZ0RGZ1dmc9PQ==--0a9b15d748993f1a0079f3256baa9e8348457ca4

Coookiecutter QA let you create QA projects based on the Cookiecutter_ scaffolding project.

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
    Select command_line_interface:
    1 - Click
    2 - No command-line interface
    Choose from 1, 2 [1]: 2
    base_url [http://www.tierratelematics.com]: 
    browserstack_username [USERNAME]: YOUR_BROWSERSTACK_USERNAME_HERE
    browserstack_access_key [ACCESS_KEY]: YOUR_BROWSERSTACK_ACCESS_KEY_HERE
    testrail [y]:
    $ cd project_qa

As result cookiecutter will create for you a new package with a hello world test pytest_, Splinter_, BDD and page
objects ready.

**Important note**: be aware that the Browserstack access key will be saved in ``project_name/Dockerfile``
so keep in mind that before distributing your project!


How to use it
=============


If you want to perform a quick tour create a Browserstack_ free account and you will be able to
run your tests against a real remote browser without having to install locally all the needed
prerequisites (geckodriver, chromedriver, adjust executable paths, etc).

Once logged in on Browserstack_ visit ``Account > Settings``, copy the Automate's username and access key
and generate a new cookiecutter project providing username and access key when asked (``browserstack_username``
and ``browserstack_access_key``)

Docker
------

If you want to launch your hello world Selenium based tests against Browserstack_ you can just
type the following commands (Docker required)::

    $ make docker-run

or::

    $ docker run --rm -it project_qa -epy36 -- \
        -vvv --splinter-webdriver=remote \
        --variables=credentials_tepmlate.yml \
        --splinter-remote-url=http://BROWSERSTACK_USERNAME:BROWSERSTACK_ACCESS_KEY@hub.browserstack.com:80/wd/hub \
        --variables capabilities/WIN10-FIREFOX53.json

Tox
---

With tox::

    $ pip install tox
    $ tox -epy35 -- -vvv --splinter-webdriver=remote \
        --variables=credentials_template.yml \
        --splinter-remote-url=http://BROWSERSTACK_USERNAME:BROWSERSTACK_ACCESS_KEY@hub.browserstack.com:80/wd/hub \
        --variables capabilities/WIN10-FIREFOX53.json


In the next future you will be able to choose a very basic test example or another one with a
more opinionated stack.


Credits
=======

* heavily based on `cookiecutter-pypackage`_: `@audreyr`_'s ultimate Python package project
  template.

Twitter
=======

cookiecutter-qa tweets happens here:

* `@davidemoro`_


Based on
========

.. image:: https://raw.github.com/audreyr/cookiecutter/3ac078356adf5a1a72042dfe72ebfa4a9cd5ef38/logo/cookiecutter_medium.png

Sponsored by
============

.. image:: http://cookiecutter-qa.readthedocs.io/en/latest/_static/browserstack.svg
     :target: https://www.browserstack.com
     :alt: Browserstack

.. _tierra_qa: https://github.com/tierratelematics/tierra_qa
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Browserstack: https://www.browserstack.com
.. _`@audreyr`: https://github.com/audreyr
.. _`cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`@davidemoro`: https://twitter.com/davidemoro
.. _`Splinter`: https://splinter.readthedocs.io/en/latest/
.. _`pytest`: https://docs.pytest.org/en/latest/
