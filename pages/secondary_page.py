from selenium.webdriver.common.by import By
from pages.base_page import Page


class SecondaryPage(Page):
    CLICK_FINAL_PAGE = (By.CSS_SELECTOR, 'a[wized="nextPageMLS"]')
    RETURN_TO_FIRST_PAGE = (By.CSS_SELECTOR, '[wized="previousPageMLS"]')

    def open_secondary(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[href*="/secondary-listings"]').click()

    def confirm_url(self,*locator):
        current_url = self.driver.current_url
        expected_url = 'https://soft.reelly.io/secondary-listings'
        assert current_url == expected_url, f"URL mismatch: {current_url}, expected {expected_url}"

    def click_final(self):
        for i in range(0, 73):
            self.driver.find_element(*self.CLICK_FINAL_PAGE).click()

    def return_to_first(self):
        for i in range(73, 0):
            self.driver.find_element(*self.RETURN_TO_FIRST_PAGE).click()