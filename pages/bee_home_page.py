from playwright.sync_api import Page

from pages.base_page import BasePage


class BeeHomePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)