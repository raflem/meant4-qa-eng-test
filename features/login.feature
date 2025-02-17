Feature: Login
  Functionality to log in into an account

  Scenario: Logging in
    Given Browser is open on the Sign In page
    And I have an account

    When I enter account name
    And I enter password
    And I press the 'log in' button

    Then I should be logged in
    And I shouldn't see an error message
