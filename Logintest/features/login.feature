# Created by xihengwang at 7/5/20
Feature: Login pointzi# Enter feature name here
  # Enter feature description here

  Scenario:login
    Given I open url
    When I input usename & password, press login
    Then Login successful