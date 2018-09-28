@Employee
Feature: Add employee

  Scenario: Add a new employee
    Given the login page is already open
     When the admin logs using username "Admin" and password "admin123"
     And  the admin clicks PIM tab
     And  clicks Add Employee tab
     Then the admin fill in new employee details
     