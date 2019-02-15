===============
cookiecutter QA
===============

.. image:: https://travis-ci.org/davidemoro/cookiecutter-qa.svg?branch=master
       :target: https://travis-ci.org/davidemoro/cookiecutter-qa

.. image:: https://pyup.io/repos/github/davidemoro/cookiecutter-qa/shield.svg
       :target: https://pyup.io/repos/github/davidemoro/cookiecutter-qa/
       :alt: Updates

.. image:: https://readthedocs.org/projects/cookiecutter-qa/badge/?version=latest
       :target: http://cookiecutter-qa.readthedocs.io

Coookiecutter QA let you create QA projects based on the Cookiecutter_ scaffolding project.

Usage
=====

Install Cookiecutter_, use ``cookiecutter-qa`` as project template
and bake your new QA package providing some information::

    $ pip install cookiecutter
    $ cookiecutter https://github.com/davidemoro/cookiecutter-qa
    email [davide.moro@gmail.com]: 
    project_name [Project QA]: 
    project_slug [project_qa]: 
    project_short_description [Project QA contains all the boilerplate you need to create a QA package]: 
    version [0.0.1]: 
    base_url [https://www.tierratelematics.com]:
    selenium_grid_url [http://USERNAME:ACCESS_KEY@hub.browserstack.com:80/wd/hub]: YOUR_SELENIUM_GRID_URL_HERE
    pytest_play [y]:
    testrail [y]:
    $ cd project_qa

As result cookiecutter will create for you a new package with a hello world test pytest_, Splinter_, pytest-play_,
BDD and page objects ready.

**Important note**: be aware that the `selenium_grid_url` will be saved in ``project_name/pytest.ini``!

And now you can launch your helo world project test (linux)::

    $ docker run --rm -it -v $(pwd):/src davidemoro/pytest-play

or you are using Windows substitute the `$(pwd)` command with your project full path.

You can also use custom options provided by pytest and other installed third party plugins
or request for custom browser capabilities. For example::

    $ docker run --rm -it -v $(pwd):/src davidemoro/pytest-play \
        --variables capabilities/os/WIN10.json
        --variables capabilities/browsers/chrome/CHROME.json
        --variables capabilities/resolutions/1280x1024.json
        -x
        --pdb

Local browsers testing is supported too (covered in next sections).

Setup
=====

Prerequisites:

* python >= 3.6, needed for the scaffolding tool

* cookiecutter scaffolding tool for generating your project (``pip install cookiecutter`` command)

* docker, suggested method for executing your tests using the well
  tested https://github.com/davidemoro/pytest-play-docker container.
  Using docker is the easiest and faster solution for running your tests

* a selenium grid url or ``geckodriver``/``chromedriver`` installed

Browsers setup and selenium_grid_url
------------------------------------

If you are not yet comfortable with `geckodriver`/`chromedriver` installations, `PATH` environment variable
update I suggest to start creating a BrowserStack_ free account and you will be able to
run your tests against a real remote browser without having to install locally all the needed
prerequisites.

Once logged in on BrowserStack_ visit ``Account > Settings``, copy the Automate's username and access key
and generate a new cookiecutter project providing the remote selenium grid url following the format::

    http://USERNAME:ACCESS_KEY@hub.browserstack.com:80/wd/hub

You can use any Selenium grid provider (SauceLabs_, BrowserStack_, TestingBot_) or using your own local
grid with Zalenium_.

Otherwise local browsers testing is supported too thanks to the option ``splinter-webdriver``, read the
following section. 

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

Using local browsers it's up to you the configuration of geckodriver, chromedriver,
executable path settings, using the latest drivers
(eg: https://github.com/mozilla/geckodriver/releases) and updated browser versions.

pytest-play ready!
==================

``cookiecutter-qa`` supports also pytest-play_ including by default all the third
party external plugins like play_selenium_, play_requests_ and their brothers
(see `Third party pytest-play plugins`_) so you can execute plain **yaml** files.

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

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _BrowserStack: https://www.browserstack.com
.. _`@audreyr`: https://github.com/audreyr
.. _`cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`@davidemoro`: https://twitter.com/davidemoro
.. _`Splinter`: https://splinter.readthedocs.io/en/latest/
.. _`pytest`: https://docs.pytest.org/en/latest/
.. _`pytest-play`: http://pytest-play.readthedocs.io/en/latest/
.. _`play_selenium`: https://github.com/davidemoro/play_selenium
.. _`play_requests`: https://github.com/davidemoro/play_request
.. _`Third party pytest-play plugins`: https://github.com/pytest-dev/pytest-play#third-party-pytest-play-plugins
.. _`Zalenium`: https://github.com/zalando/zalenium
.. _`SauceLabs`: https://saucelabs.com/
.. _`TestingBot`: https://testingbot.com/
