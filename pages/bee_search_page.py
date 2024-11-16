from playwright.sync_api import Page

from page_factory.title import Title
from pages.base_page import BasePage


class BeeSearchPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.product_title = Title(
            page, locator="//span[@class='AIVQ3 sTx01 ylczO' and contains(text(), 'Смартфоны')]", name='Product title'
        )

    def product_category_smartphone_present(self, product: str):
        self.product_title.should_be_visible(product=product)
        self.product_title.should_have_text(
            product.capitalize(), product=product
        )