from playwright.sync_api import Page

from page_factory.button import Button
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
        self.frequent_keyword_tariff = Button(
            page, locator='//button[@data-metric-name ="headerMetric:handleClickSearchElementBlock"]/span[@class = "n3jKk ffb9F WfcVx" and text() = "тарифы"]'
            , name='Frequent Keyword Tariff button'
        )
        self.result_tariff_plan_b_button = Button(
            page, locator='//span[@class = "n3jKk ffb9F hCtRh" and text() = "план б."]', name='Plan B result button'
        )

    def modal_is_opened(self):
        self.search_input.should_be_visible()
        self.search_modal_title.should_be_visible()

    def find_result_by_input_keyword(self, keyword: str) -> None:
        self.search_input.fill(keyword, validate_value=True)
        self.search_all_results.click()

    def find_result_by_clicking_frequent_keyword_tariff(self) -> None:
        self.frequent_keyword_tariff.should_be_visible()
        self.frequent_keyword_tariff.click()
        self.search_input.should_have_value('тарифы')
        self.result_tariff_plan_b_button.should_be_visible()
        self.result_tariff_plan_b_button.click()
