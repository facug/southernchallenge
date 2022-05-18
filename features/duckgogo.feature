Feature: DuckGoGo search

  Scenario: Michael Jordan search
    Given i launch chrome browser
    When i open DuckGogo homepage
    And search for "Michael Jordan"
    Then verify Michael Jordan profile picture is displayed
    Then verify there is one "wikipedia" page result
    Then verify there is one "nba" page result