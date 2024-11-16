from playwright.sync_api import Page

from page_factory.button import Button
from page_factory.title import Title
from pages.base_page import BasePage


class BeeBasketPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.first_added_product_to_basket_title = Title(
            page, locator="//div[@class='fLFZW qeeNs bsIdT align-stretch']/p", name='First added product to basket')


    def product_basket_present(self, product: str):
        self.first_added_product_to_basket_title.should_be_visible(product=product)
        self.first_added_product_to_basket_title.should_have_text(
            product, product=product
        )
