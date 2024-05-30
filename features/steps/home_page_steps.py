from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@then('Verify the home page opens')
def verify_home_page_url(context):
    context.app.home_page.open_home()


@then('Click on Secondary option at the left side menu')
def click_secondary_option(context):
    context.app.secondary_page.open_secondary()