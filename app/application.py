from pages.base_page import Page
from pages.signin_page import Signin
from pages.secondary_page import SecondaryPage
from pages.main_page import MainPage
from pages.home_page import HomePage


class Application:

    def __init__(self, driver):
        self.base_page = Page(driver)
        self.signin_page = Signin(driver)
        self.secondary_page = SecondaryPage(driver)
        self.main_page = MainPage(driver)
        self.home_page = HomePage(driver)