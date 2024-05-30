from selenium.webdriver.common.by import By
from pages.base_page import Page


class Signin(Page):
    CLICK_LOGIN_BUTTON = (By.CSS_SELECTOR, 'a[href="/sign-in"]')
    SIGNIN_PAGE_EMAIL = (By.CSS_SELECTOR, 'input[wized="emailInput"]')
    SIGNIN_PAGE_PASSWORD = (By.CSS_SELECTOR, 'input[wized="passwordInput"]')
    SIGNIN_BUTTON = (By.CSS_SELECTOR, 'a[wized="loginButton"]')
    CLICK_FINAL_PAGE = (By.CSS_SELECTOR, 'a[wized="nextPageMLS"]')
    RETURN_TO_FIRST_PAGE = (By.CSS_SELECTOR, '[wized="previousPageMLS"]')

    def sign_in_button(self):
        self.driver.find_element(*self.CLICK_LOGIN_BUTTON).click()
        self.driver.find_element(*self.SIGNIN_BUTTON).click()

    def email_and_password(self):
        email = "jeneta.test@gmail.com"
        password = "Butter11.5"
        self.driver.find_element(*self.SIGNIN_PAGE_EMAIL).send_keys(email)
        self.driver.find_element(*self.SIGNIN_PAGE_PASSWORD).send_keys(password)
        self.driver.find_element(*self.SIGNIN_BUTTON).click()
