"""
Fixture Diagrams
----------------

The following diagram shows the interactions between the `pytest fixtures`_
created in the ``{{cookiecutter.project_slug}}`` package:

.. graphviz::

   digraph {
      credentials_mapping;
      skin;
      base_url;
      page_mappings,
      default_page_class;
      base_page;
      page_instance;
      navigation;
      navigation_class;
      skip_by_skin_names;
      variables [color="grey"];
      request [color="grey"];
      browser [color="grey"];
      skin -> {credentials_mapping base_url default_page_class navigation
               skip_by_skin_names};
      variables -> {credentials_mapping base_url} [color="grey"];
      request -> {skin skip_by_skin_names} [color="grey"];
      page_mappings -> {default_page_class base_page navigation}
      base_url -> {base_page navigation};
      browser -> {base_page} [color="grey"];
      default_page_class -> {base_page navigation};
      base_page -> {page_instance};
      navigation_class -> {navigation};
      page_instance -> {navigation};
      credentials_mapping -> {navigation};
   }


.. _pytest fixtures: http://doc.pytest.org/en/latest/fixture.html
"""

import os
import platform

import pytest

import {{cookiecutter.project_slug}}
from {{cookiecutter.project_slug}}.config import DEFAULT_PAGES


@pytest.fixture(autouse=True)
def bdd_vars(bdd_vars, variables, skin, data_base_path):
    """ Inject bdd_vars so they becomes available in play_json """
    bdd_vars['data_base_path'] = data_base_path
    return bdd_vars


@pytest.fixture
def data_base_path():
    """ where pytest-play json files live """
    here = os.path.abspath(os.path.dirname(__file__))
    data_path = os.path.join(here, 'data')
    if 'WIN' in platform.system().upper():
        data_path = data_path.replace(os.sep, os.sep*2)
    return data_path


@pytest.fixture
def pytestbdd_feature_base_dir():
    """Feature files base directory."""
    return os.path.join(os.path.dirname({{cookiecutter.project_slug}}.__file__), 'features')


@pytest.fixture(scope='session', params=DEFAULT_PAGES.keys())
def skin(request):
    """ This fixture provides the skin associated with the application
        on which starts the test session.
    """
    return request.param


@pytest.fixture(scope="session")
def default_pages():
    """ A mapping with the default page object class for each skin

        It's up to you override this fixture with your settings.

        For example::

            DEFAULT_PAGES = {
                'skin1': 'mypackage.pages.BasePage',
            }
    """
    return DEFAULT_PAGES


@pytest.fixture(scope='session')
def base_url(skin, variables):
    """ Returns the base_url associated to the skin.
    """
    return variables['skins'][skin]['base_url']


@pytest.fixture(scope="session")
def page_mappings():
    """
        Returns the page mappings dictionary with all known page with:

        * paths
        * optional page object class (otherwise the default implementation
          will be used as fallback provided by :py:func:`default_page_class`)

        See :py:mod:`{{cookiecutter.project_slug}}.config` for further details.

        :return: dictionary with all known pages
        :rtype: dict`
    """
    return {{cookiecutter.project_slug}}.config.PAGE_MAPPINGS


@pytest.fixture(scope="session")
def splinter_screenshot_dir():
    """Feature files base directory."""
    return os.path.join(os.path.dirname({{cookiecutter.project_slug}}.__file__), 'screenshots')


@pytest.fixture(scope='session')
def splinter_driver_kwargs(splinter_webdriver, variables, metadata):
    """Webdriver kwargs."""
    capabilities = {}
    if splinter_webdriver == 'remote':
        build = metadata.get('BUILD_TAG', None)
        if build:
            capabilities['build'] = build
        capabilities.update(variables.get('capabilities', {}))
    return capabilities
