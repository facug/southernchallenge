Feature: DuckDuckGo search

  Scenario: Michael Jordan search
    Given i launch chrome browser
    When i open DuckGogo homepage
    And search for "Michael Jordan"
    Then verify there is one "wikipedia" page result
    Then verify there is one "nba" page result
    Then verify Michael Jordan profile picture is displayed

    Scenario: Change duckduckgo theme
      Given i launch chrome browser
      When i open DuckGogo theme settings page
      And i change the theme to "Terminal"
      Then verify the background color changed

    Scenario: Change duckduckgo language
      Given i launch chrome browser
      When i open DuckGogo general settings page
      And i change the language to "Español (Argentina)"
      Then verify the language changed to "Español (Argentina)"
