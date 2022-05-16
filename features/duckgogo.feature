Feature: DuckGoGo search

  Scenario: Michael Jordan search
    Given i launch chrome browser
    When i open DuckGogo homepage
    And search for "Michael Jordan"
    Then verify DuckGoGo page