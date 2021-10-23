Feature: Open Google

  Scenario: Navigate to existing Patron through IRB & IPM users
    Given I open google
    When I enter search query
    Then I see suggestions
