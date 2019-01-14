===============
cookiecutter QA
===============

.. image:: https://travis-ci.org/davidemoro/cookiecutter-qa.svg?branch=master
       :target: https://travis-ci.org/davidemoro/cookiecutter-qa

.. image:: https://pyup.io/repos/github/davidemoro/cookiecutter-qa/shield.svg
       :target: https://pyup.io/repos/github/davidemoro/cookiecutter-qa/
       :alt: Updates

.. .. image:: https://pyup.io/repos/github/davidemoro/cookiecutter-qa/python-3-shield.svg
         :target: https://pyup.io/repos/github/davidemoro/cookiecutter-qa/
         :alt: Python 3

.. image:: https://readthedocs.org/projects/cookiecutter-qa/badge/?version=latest
       :target: http://cookiecutter-qa.readthedocs.io

Coookiecutter QA let you create QA projects based on the Cookiecutter_ scaffolding project.

Usage
=====

Install Cookiecutter_, use ``cookiecutter-qa`` as project template
and bake your new QA package providing some information::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/davidemoro/cookiecutter-qa
    full_name [Davide Moro]: 
    email [davide.moro@gmail.com]: 
    github_username [davidemoro]: 
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
    base_url [https://www.tierratelematics.com]:
    selenium_grid_url [http://USERNAME:ACCESS_KEY@hub.browserstack.com:80/wd/hub]: YOUR_SELENIUM_GRID_URL_HERE
    testrail [y]:
    $ cd project_qa

As result cookiecutter will create for you a new package with a hello world test pytest_, Splinter_, BDD and page
objects ready.

**Important note**: be aware that the `selenium_grid_url` will be saved in ``project_name/Dockerfile``
so keep in mind that before distributing your project!


How to use it
=============


If you want to perform a quick tour create a BrowserStack_ free account and you will be able to
run your tests against a real remote browser without having to install locally all the needed
prerequisites (geckodriver, chromedriver, adjust executable paths, etc).

Once logged in on BrowserStack_ visit ``Account > Settings``, copy the Automate's username and access key
and generate a new cookiecutter project providing the remote selenium grid url following the format::

    http://USERNAME:ACCESS_KEY@hub.browserstack.com:80/wd/hub

You can use any Selenium grid provider (SauceLabs_, BrowserStack_, TestingBot_) or using your own local
grid with Zalenium_.

Docker
------

If you want to launch your hello world Selenium based tests against BrowserStack_ you can just
type the following commands (Docker required)::

    $ make docker-run

or::

    $ docker run --rm -it project_qa -epy36 -- \
        -vvv --splinter-webdriver=remote \
        --variables=credentials/credentials_template.yml \
        --splinter-remote-url=http://USERNAME:ACCESS_KEY@hub.browserstack.com:80/wd/hub \
        --variables capabilities/os/WIN10.json
        --variables capabilities/browsers/chrome/CHROME.json
        --variables capabilities/resolutions/1280x1024.json

Tox
---

With tox::

    $ pip install tox
    $ tox -epy36 -- -vvv --splinter-webdriver=remote \
        --variables=credentials/credentials_template.yml \
        --splinter-remote-url=http://USERNAME:ACCESS_KEY@hub.browserstack.com:80/wd/hub \
        --variables capabilities/os/WIN10.json
        --variables capabilities/browsers/chrome/CHROME.json
        --variables capabilities/resolutions/1280x1024.json


Run tests with local browsers
=============================

You can launch tests based on local browsers instead of relying to a
remote (SauceLabs_, BrowserStack_, TestingBot_) or local grid (using Zalenium_)
using the ``--splinter-webdriver firefox`` option for example.

See https://github.com/pytest-dev/pytest-splinter#command-line-options

Supported browser options:

* firefox

* remote (you need to provide a value for the ``--splinter-remote-url`` option)

* chrome

* phantomjs

Using local browsers it's up to you the configuration of geckodriver, chromedriver,
executable path settings, using the latest drivers
(eg: https://github.com/mozilla/geckodriver/releases) and updated browser versions.

pytest-play ready!
==================

``cookiecutter-qa`` supports also pytest-play_.

If you are not keen on programming or page objects you can run scenarios using
the **yaml** format.

See ``test_play.py`` and ``play.json``.


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
.. _BrowserStack: https://www.browserstack.com
.. _`@audreyr`: https://github.com/audreyr
.. _`cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`@davidemoro`: https://twitter.com/davidemoro
.. _`Splinter`: https://splinter.readthedocs.io/en/latest/
.. _`pytest`: https://docs.pytest.org/en/latest/
.. _`pytest-play`: http://pytest-play.readthedocs.io/en/latest/
.. _`Zalenium`: https://github.com/zalando/zalenium
.. _`SauceLabs`: https://saucelabs.com/
.. _`TestingBot`: https://testingbot.com/
