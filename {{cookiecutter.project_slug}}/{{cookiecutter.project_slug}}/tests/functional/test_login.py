# coding=utf-8
"""Login feature tests."""

from functools import partial
from pytest_bdd import (
    scenario as bdd_scenario,
    then,
)

scenario = partial(bdd_scenario, "functional/login.feature")


@scenario("Successful login")
def test_successfull_login():
    """Login."""


@then('I am logged in')
def check_loggedin_then(navigation, username):
    """Assert user is logged in. Implement here your
       project related login logics.
    """
    page = navigation.page
    assert page.is_loggedin()
    assert page.username() == username
