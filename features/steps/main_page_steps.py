from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


@given('Open Reely main page')
def open_reely(context):
    context.driver.get('https://soft.reelly.io/sign-up')
    # context.app.main_page.open_main()


@when('Click on Secondary option at the left side menu.')
def click_secondary_option(context):
    context.driver.find_element(By.CSS_SELECTOR, 'a[href*="/secondary-listings"]').click()


@then('Verify the right page opens')
def verify_secondary_page_url(context):
    current_url = context.driver.current_url
    expected_url = 'https://soft.reelly.io/secondary-listings'
    assert current_url == expected_url, f"URL mismatch: {current_url}, expected {expected_url}"



