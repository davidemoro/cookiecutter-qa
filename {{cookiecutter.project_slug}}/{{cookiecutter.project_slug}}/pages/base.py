"""
Base page implementation
========================

This is where the base page implementation lives.
"""

from pypom_navigation.pages import BasePage as BaseFormPage


class BasePage(BaseFormPage):
    """
        This is the base page to be used in {{cookiecutter.project_slug}}.

        Once you clone {{cookiecutter.project_slug}} for your own qa project, you should:

        * implement the login, is_loggedin and logout methods of this class
        * add your own page object classes depending on your business
          logics inheriting from this base class
    """

    def login(self, username, password):
        """
            This is the login method of the base page object.

            It's up to you implement this method once you cloned
            {{cookiecutter.project_slug}}.

            :return: BasePage instance
            :rtype: object
        """

    def is_loggedin(self):
        """
            This is the is_loggedin method of the base page object.

            It's up to you implement this method once you cloned
            {{cookiecutter.project_slug}}.

            :return: True if you are logged in or False
            :rtype: bool
        """
        return True

    def username(self):
        """
            This is the username method of the base page object.

            It's up to you implement this method once you cloned
            {{cookiecutter.project_slug}}.

            :return: the username or None
            :rtype: string or None
        """
        return 'admin'

    def logout(self):
        """
            This is the logout method of the base page object.

            It's up to you implement this method once you cloned
            {{cookiecutter.project_slug}}.

            :return: BasePage instance
            :rtype: object
        """
