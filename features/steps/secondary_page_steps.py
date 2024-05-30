from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then('Click on Secondary option at the left side menu')
def click_secondary_option(context):
    context.app.secondary_page.open_secondary()


@then('Verify the right page opens')
def verify_secondary_page_url(context):
    context.app.secondary_page.confirm_url()


@then("Go to the final page using the pagination button")
def click_final_page(context):
    context.app.secondary_page.click_final()


@then("Go back to the first page using the pagination button")
def return_to_first_page(context):
    context.app.secondary_page.return_to_first()