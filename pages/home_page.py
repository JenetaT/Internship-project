from pages.base_page import Page


class HomePage(Page):

    def open_home(self):
        self.driver.get('https://soft.reelly.io/')