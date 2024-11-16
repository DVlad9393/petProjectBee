import pytest

from pages.bee_basket_page import BeeBasketPage
from pages.bee_home_page import BeeHomePage
from pages.bee_search_page import BeeSearchPage
from pages.bee_planb_page import BeePlanBPage
from settings import BASE_URL


class TestSearch:
    @pytest.mark.parametrize('keyword', ['Смартфоны'])
    def test_search_smartphone_page(
        self,
        keyword: str,
            bee_home_page: BeeHomePage,
            bee_search_page: BeeSearchPage
    ):

        bee_home_page.visit(BASE_URL)
        bee_home_page.navbar.open_search()
        bee_home_page.navbar.search_modal.find_result_by_input_keyword(
            keyword
        )

        bee_search_page.product_category_smartphone_present(product=keyword)


    @pytest.mark.smoke
    def test_search_and_buy_tariff(
        self,
            bee_home_page: BeeHomePage,
            bee_planb_page: BeePlanBPage,
            bee_basket_page: BeeBasketPage
    ):

        bee_home_page.visit(BASE_URL)
        bee_home_page.navbar.open_search()
        bee_home_page.navbar.search_modal.find_result_by_clicking_frequent_keyword_tariff()

        bee_planb_page.product_planb_present("настрой план б. под себя")
        bee_planb_page.find_and_click_buy_tariff_button()
        bee_basket_page.product_basket_present("план б.")