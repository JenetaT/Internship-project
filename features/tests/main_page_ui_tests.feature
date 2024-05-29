Feature: Tests for main page UI

  Scenario: User can open the secondary deals page and go through pagination
    Given Open Reely main page
    When Click login
    And Enter email and password
    And Click on Secondary option at the left side menu.
    Then Verify the right page opens
    Then Go to the final page using the pagination button
    Then  Go back to the first page using the pagination button