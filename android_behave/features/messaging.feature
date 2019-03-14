@Messaging
Feature: SMS Messaging

Scenario: Run messaging
   Given the menu is open
   When the user clicks OS button
   And clicks the sms messaging option
   Then enter recipient and message body
