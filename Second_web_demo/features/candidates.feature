@candidates
Feature: Adding a candidate

  Scenario: adding a candidate
    Given the login page is open
     When the user logs with username "Admin" and password "admin123"
     Then the user hovers over recruitment tab

    Given the user clicks on candidates
     When the user clicks on add button
     Then the user fills the candidates web form
     When the user views the candidate information and clicks the back button

    Given the user deletes the candidates records 
     When the user clicks the checklist button
     Then the user clicks the delete button
     