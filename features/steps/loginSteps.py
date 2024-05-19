from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


# @given('launch chrome browser')
# def launchBrowser(context):
#     context.driver = webdriver.Chrome
#
#
# @when('open orange hrm homepage')
# def openHomePage(context):
#     context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

@when('Enter username and password')
def openHomePage(context):
    context.driver.implicitly_wait(5)
    username_field=context.driver.find_element(By.XPATH, "//input[@name='username']")
    password_field=context.driver.find_element(By.XPATH, "//input[@name='password']")
    username_field.send_keys("admin")
    password_field.send_keys("admin123")


@when('click on login button')
def openHomePage(context):
    context.driver.implicitly_wait(5)
    context.driver.findElement(By.XPATH, "//button[@type='submit']").click()



