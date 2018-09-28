@Leaves
Feature: Assign leaves

  Scenario: Assign leaves to employees
    Given the login page is already open
   # Given the home page is open
     When the admin logs in with username "Admin" and password "admin123"
     And  the admin clicks Assign Leave
     And  the admin enters leave details
     Then the admin clicks OK button
     