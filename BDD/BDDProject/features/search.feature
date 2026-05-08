


Feature: Search
  Scenario: Search for product that has results
    Given buyer is on the olx home page
    When buyer types product in the searchbar
    Then search results should be displayed


#  Scenario: search for a product that has no results
#    Given buyer is on the olx home page
#    When buyer types product in the searchbar
#    Then error message