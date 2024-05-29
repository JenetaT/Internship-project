from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


CLICK_LOGIN_BUTTON = (By.CSS_SELECTOR, 'a[href="/sign-in"]')
SIGNIN_PAGE_EMAIL = (By.CSS_SELECTOR, 'input[wized="emailInput"]')
SIGNIN_PAGE_PASSWORD = (By.CSS_SELECTOR, 'input[wized="passwordInput"]')
SIGNIN_BUTTON = (By.CSS_SELECTOR, 'a[wized="loginButton"]')
CLICK_FINAL_PAGE = (By.CSS_SELECTOR, 'a[wized="nextPageMLS"]')
RETURN_TO_FIRST_PAGE = (By.CSS_SELECTOR, '[wized="previousPageMLS"]')


@when('Click login')
def click_login(context, *locator):
    context.driver.find_element(*CLICK_LOGIN_BUTTON).click()
    context.driver.find_element(By.CSS_SELECTOR, 'a[wized="loginButton"]').click()


@when("Enter email and password")
def enter_email_and_password(context):
    email = "jeneta.test@gmail.com"
    password = "Butter11.5"
    context.driver.find_element(*SIGNIN_PAGE_EMAIL).send_keys(email)
    context.driver.find_element(*SIGNIN_PAGE_PASSWORD).send_keys(password)
    context.driver.find_element(*SIGNIN_BUTTON).click()


@then("Go to the final page using the pagination button")
def click_final_page(context):
    for i in range(0,73):
        context.driver.find_element(*CLICK_FINAL_PAGE).click()


@then("Go back to the first page using the pagination button")
def return_to_first_page(context):
    for i in range(73,0):
        context.driver.find_element(*RETURN_TO_FIRST_PAGE).click()
