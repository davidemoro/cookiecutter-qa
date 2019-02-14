Feature: Logout
  A logged user try to logout from the application

  @UI @logout
  Scenario: Successful logout
    Given I am logged in as Administrator
    When I logout from the application
    Then I land on the LoginPage page
