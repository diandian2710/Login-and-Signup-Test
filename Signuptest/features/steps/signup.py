from selenium import webdriver
import time
from behave import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@Given('I open url and click on register')
def step_impl(context):
    context.driver.get(context.pointzi_url)
    time.sleep(3)
    context.driver.find_element_by_xpath("/html/body/div[1]/md-content/div[2]/div/sh-login/form/div[1]/a").click()


@When('I input email, password, confirm password，press next')
def step_impl(context):
    context.driver.find_element_by_name("username").send_keys("neilwang92@gmail.com")
    context.driver.find_element_by_name("password").send_keys("diandian2710")
    context.driver.find_element_by_name("confirmPassword").send_keys("diandian2710")
    context.driver.find_element_by_xpath("/html/body/div[1]/md-content/div[2]/div/sh-register/form/div[4]/div[2]/button[1]").click()

@When('I choose role, No.of app users')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/md-content/div[2]/div/sh-register/form/div[2]/md-input-container[1]/md-select").click()
    role_choice = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "md-option[value = 'Developer']")))
    role_choice.click()
    context.driver.find_element_by_xpath("/html/body/div[1]/md-content/div[2]/div/sh-register/form/div[2]/md-input-container[2]/md-select").click()
    user_choice = WebDriverWait(context.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "md-option[value = '50,001 - 100,000']")))
    user_choice.click()
    context.driver.find_element_by_xpath("/html/body/div[1]/md-content/div[2]/div/sh-register/form/div[4]/div[2]/button[1]").click()

@When('I input First name, Last name, Company name, Phone number, click terms and conditions, click press sign up')
def step_impl(context):
    context.driver.find_element_by_xpath("/html/body/div[1]/md-content/div[2]/div/sh-register/form/div[3]/md-input-container[1]/input").send_keys("Neil")
    context.driver.find_element_by_xpath("/html/body/div[1]/md-content/div[2]/div/sh-register/form/div[3]/md-input-container[2]/input").send_keys("Wang")
    context.driver.find_element_by_xpath("/html/body/div[1]/md-content/div[2]/div/sh-register/form/div[3]/md-input-container[3]/input").send_keys("PE")
    context.driver.find_element_by_xpath("/html/body/div[1]/md-content/div[2]/div/sh-register/form/div[3]/md-input-container[4]/input").send_keys("0450xxxx")
    context.driver.find_element_by_xpath("/html/body/div[1]/md-content/div[2]/div/sh-register/form/div[3]/p/md-checkbox/div[1]").click()
    context.driver.find_element_by_xpath("/html/body/div[1]/md-content/div[2]/div/sh-register/form/div[4]/div[2]/button[2]").click()

@Then('Sign up successfully')
def step_impl(context):
    def step_impl(context):
        time.sleep(3)
        currentURL = context.driver.current_url
        if currentURL == ('https://dashboard.pointzi.com/tutorial'):
            assert True
        else:
            assert False