from BaseApp import BasePage
from selenium.webdriver.common.by import By


class TestSearchLocators:
    LOCATOR_TITLES = (By.CSS_SELECTOR, "h2.svelte-127jg4t")


class OperationsHelper(BasePage):
    def get_titles(self):
        return self.find_element(TestSearchLocators.LOCATOR_TITLES)
