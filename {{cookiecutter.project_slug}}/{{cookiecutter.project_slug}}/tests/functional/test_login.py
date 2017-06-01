# coding=utf-8
"""Login feature tests."""

from functools import partial
import pytest_bdd

scenario = partial(pytest_bdd.scenario, "functional/login.feature")


@scenario("Successful login")
def test_successfull_login():
    """Login."""


@pytest_bdd.then('I am logged in')
def check_loggedin_then(navigation, username):
    """Assert user is logged in. Implement here your
       project related login logics.
    """
    page = navigation.page
    assert page.is_loggedin()
    assert page.username() == username
