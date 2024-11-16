from playwright.sync_api import Page

from page_factory.button import Button
from page_factory.title import Title
from pages.base_page import BasePage


class BeePlanBPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.product_planb_title = Title(
            page, locator="//span[@class='AIVQ3 o2F3Q bDcRi' and contains(text(), 'план б')]", name='Product Plan B title')

        self.product_planb_buy_button = Button(
            page, locator="//button[@class='AdThl bMhN6 t0t9G prz9u l8VYk']", name='Product Plan B title'
        )

    def product_planb_present(self, product: str):
        self.product_planb_title.should_be_visible()
        self.product_planb_title.should_have_text(
            product, product=product
        )

    def find_and_click_buy_tariff_button(self) -> None:
        self.product_planb_buy_button.should_be_visible()

        self.product_planb_buy_button.click()