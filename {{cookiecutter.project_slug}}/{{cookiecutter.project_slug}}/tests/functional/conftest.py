# coding=utf-8
"""Login feature tests."""

from pytest_bdd import (
    given,
    when,
    then,
)
from pytest_bdd.parsers import (
    parse,
)


@given(parse('I am logged in as {user_id}'))
def username(user_id, navigation):
    """Login and returns username for the given user_id """
    username, password = navigation.get_credentials(user_id)
    navigation.page.login(username, password)
    return username


# we need to change step description due to a nasty limitation of pytest-bdd.
# See https://github.com/pytest-dev/pytest-bdd/issues/199

@given(parse(
    '[outline] I am on the <page_id> page'))
@given(parse(
    'I am on the {page_id} page'))
def loggedin_page_given_outline(page_id, navigation):
    """Logged in fixture"""
    navigation.visit_page(page_id)


def _check_page_url(page, page_id):
    """ Check page url matches used by several BDD steps.
        Page is not a dictionary but the page object.
    """
    assert page.navigation.get_page_url(page_id) in page.current_url


@when(parse(
    'I visit the {page_id} page'))
def visit_page(navigation, page_id):
    """Visit the page."""
    navigation.visit_page(page_id)


@when(parse(
    'I logout from the application'))
def check_logout_when(navigation):
    """Check the user logout."""
    page = navigation.page
    page.logout()


@then(parse(
    'the page contains text <text>'))
def page_text_check(navigation, text):
    page = navigation.page
    assert page.has_text(text)


@then(parse(
    'I land on the {page_id} page'))
@then(parse(
    'I land on the <page_id> page'))
def check_page_url_no_follow(navigation,
                             page_id):
    """ Check page url matches """
    page = navigation.page
    _check_page_url(page, page_id)
