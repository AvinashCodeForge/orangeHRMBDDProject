from behave import *
from selenium import webdriver


@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()


@when('open orange hrm homepage')
def openHomePage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


@when('close browser')
def closeBrowser(context):
    context.driver.close()
