Feature: Tests for home page

  Scenario: Verify home page opens
    Given Open Reely main page
    When Click login
    Then Enter email and password
    Then Verify the home page opens

  Scenario:Go to secondary page
    Given Open Reely main page
    When Click login
    Then Enter email and password
    Then Click on Secondary option at the left side menu


