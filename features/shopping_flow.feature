Feature: Shopping flow
  Add an item to the cart and proceed to checkout

  Scenario: Shopping flow
    Given I am registered and signed in
    And Browser is open on the shop page
    And Shopping cart is empty
    And Items are available

    When I add an item to the cart
    And Proceed to checkout
    And Provide a delivery address
    And Select a shipping option
    And Accept the ToS
    And Select a payment option
    And Confirm the transaction

    Then An order is placed
    And I shouldn't see an error message
