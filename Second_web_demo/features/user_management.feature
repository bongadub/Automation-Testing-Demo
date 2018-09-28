@Users
Feature: User management

  Scenario: Manage users
    Given the login page is already open
    #Given the login page is open
     When the admin logs with username "Admin" and password "admin123"
     And  the admin clicks admin tab
     And  the admin clicks add button
     Then  the admin insert user details
