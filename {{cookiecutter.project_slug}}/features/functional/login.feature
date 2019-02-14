Feature: Login
  A user login try to login to the application

  @UI @login
  Scenario: Successful login
    Given I am logged in as Administrator
    Then I am logged in
