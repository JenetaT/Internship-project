Feature: Tests for secondary page

  Scenario: Verify correct page opens
    Given Open Reely main page
    When Click login
    Then Enter email and password
    Then Click on Secondary option at the left side menu
    Then Verify the right page opens
    Then Go to the final page using the pagination button
    Then Go back to the first page using the pagination button