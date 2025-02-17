Feature: Register
  Functionality to create a new account

  Scenario: Registering new account
    Given Browser is open on the Sign In page
    And I don't have an account registered

    When I enter an unregistered email address
    And Click the Create Account button
    And Provide required information
    And Confirm form submission

    Then An account is created
    And I shouldn't see an error message
