from playwright.sync_api import Page

from components.modals.search_modal import SearchModal
from page_factory.button import Button


class Navbar:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_modal = SearchModal(page)

        self.search_button = Button(
            page, locator='//*[@aria-label="Открыть поиск"]', name='Search'
        )

    def open_search(self):
        self.search_button.should_be_visible()

        self.search_button.hover()
        self.search_button.click()

        self.search_modal.modal_is_opened()