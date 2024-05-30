from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click login')
def click_login(context, *locator):
    context.app.signin_page.sign_in_button()


@then("Enter email and password")
def enter_email_and_password(context):
    context.app.signin_page.email_and_password()



