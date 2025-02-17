Feature: Filter and sort
  Functionality to sort and filter items in the shop

  Scenario: Filter and sort
    Given The shop site is open
    And Default filters and sorting are enabled

    When I enable a dress type filter
    And Change sorting to price descending

    Then One dress type is shown
    And Prices are sorted high to low
