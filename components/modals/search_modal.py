from playwright.sync_api import Page

from page_factory.input import Input
from page_factory.list_item import ListItem
from page_factory.title import Title


class SearchModal:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.search_modal_title = Title(
            page, locator='//p[@class="n3jKk" and text()="поиск"]', name='Search modal title'
        )
        self.search_input = Input(
            page, locator='//*[@aria-label="найти в билайне"]', name='Search products'
        )
        self.search_all_results = ListItem(
            page, locator='//span[@class="n3jKk c9sHF duPxy" and text()="все результаты"]', name='All Results item'
        )

    def modal_is_opened(self):
        self.search_input.should_be_visible()
        self.search_modal_title.should_be_visible()

    def find_result(self, keyword: str, result_number: int) -> None:
        self.search_input.fill(keyword, validate_value=True)
        self.search_all_results.click(result_number=result_number)