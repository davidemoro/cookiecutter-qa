# coding=utf-8
"""Logout feature tests."""

from functools import partial
import pytest_bdd

scenario = partial(pytest_bdd.scenario, "functional/logout.feature")


@scenario("Successful logout")
def test_successfull_logout():
    """Logout."""
