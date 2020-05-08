# Created by xihengwang at 8/5/20
Feature: Signup pointzi# Enter feature name here
  # Enter feature description here

  Scenario: signup# Enter scenario name here
    Given I open url and click on register
    When I input email, password, confirm password，press next
      And I choose role, No.of app users
      And I input First name, Last name, Company name, Phone number, click terms and conditions, click press sign up
    Then Sign up successfully
# Enter steps here

