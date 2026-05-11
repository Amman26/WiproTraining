Feature: OrangeHRM Automation Testing

  Background:
    # Moving the login here means it will automatically run before EVERY scenario below
    Given I navigate to the OrangeHRM login page
    When I login with username "Admin" and password "admin123"

  # --- Assignment 1 ---
  Scenario: User Authentication
    Then I should be logged in successfully

  # --- Assignment 2 ---
  Scenario Outline: Employee Creation
    # Navigate to the correct page first!
    When I navigate to the "PIM" menu
    And I click on the "Add Employee" tab
    And I enter "<FirstName>" and "<LastName>"

    Examples:
      | FirstName | LastName |
      | Alice     | Smith    |
      | John      | Doe      |

  # --- Assignment 3 ---
  Scenario: Admin Search using Data Tables
    # Navigate to the Admin page first!
    When I navigate to the "Admin" menu
    And I enter the following search criteria:
      | Username | User Role | Status  |
      | Admin    | Admin     | Enabled |
      | EssUser  | ESS       | Enabled |

  # --- Assignment 4 ---
  Scenario: Leave Workflow State Verification
    # Navigate to the Leave Application page first!
    When I navigate to the "Leave" menu
    And I click on the "Apply" tab
    And I apply for exactly one day of leave
    Then I capture the success toast message
    And exactly one day of leave should be deducted

  # --- Assignment 5 ---
  Scenario: Profile Update File Upload
    # Navigate to the My Info page first!
    When I navigate to the "My Info" menu
    And I upload my new profile picture