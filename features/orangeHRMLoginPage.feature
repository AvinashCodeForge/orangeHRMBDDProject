Feature: OrangeHRM Login
  Scenario: Login to orangeHRM home page with valid parameters
    Given launch chrome browser
    When open orange hrm homepage
    And Enter username and password
    And close browser
