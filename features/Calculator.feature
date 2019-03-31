@calculator
Feature: Addition of two number
Scenario: check if addition is successfully completed
    Given App is launched
    When user adds number
    Then output should be displayed
    And close app