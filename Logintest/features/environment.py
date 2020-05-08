from selenium import webdriver


def before_all(context):
    context.pointzi_url = 'https://dashboard.pointzi.com/login'
    context.driver = webdriver.Firefox()
    context.driver.implicitly_wait(20)


def after_all(context):
    context.driver.quit()
