import pytest

from pages.bee_home_page import BeeHomePage
from pages.bee_search_page import BeeSearchPage
from settings import BASE_URL


class TestSearch:
    @pytest.mark.parametrize('keyword', ['Смартфоны'])
    def test_search(
        self,
        keyword: str,
            bee_home_page: BeeHomePage,
            bee_search_page: BeeSearchPage
    ):

        bee_home_page.visit(BASE_URL)
        bee_home_page.navbar.open_search()
        bee_home_page.navbar.search_modal.find_result(
            keyword
        )

        bee_search_page.product_category_smartphone_present(product=keyword)