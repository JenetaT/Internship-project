Feature: Tests for secondary page

  Scenario: Verify secondary page opens
    Given Open Reely main page
    When Click login
    Then Enter email and password
    Then Click on Secondary option at the left side menu
    Then Verify the secondary page opens

  Scenario: Go to final page with pagination and return
    Given Open Reely main page
    When Click login
    Then Enter email and password
    Then Click on Secondary option at the left side menu
    Then Verify the secondary page opens
    Then Go to the final page using the pagination button
    Then Go back to the first page using the pagination button