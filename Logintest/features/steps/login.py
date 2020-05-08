from selenium import webdriver
import time
from behave import *

@Given('I open url')
def step_impl(context):
    context.driver.get(context.pointzi_url)



@When('I input usename & password, press login')
def step_impl(context):
    context.driver.find_element_by_name("username").send_keys("wxh604328815@gmail.com")
    context.driver.find_element_by_name("password").send_keys("diandian2710")
    context.driver.find_element_by_class_name("md-button").click()



@Then('Login successful')
def step_impl(context):
    time.sleep(3)
    currentURL = context.driver.current_url
    if currentURL == ('https://dashboard.pointzi.com/tutorial'):
        assert True
    else:
        assert False












