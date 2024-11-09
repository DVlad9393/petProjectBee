import pytest

from pages.playwright_home_page import BeeHomePage
from pages.playwright_languages_page import BeeSearchPage
from settings import BASE_URL


class TestSearch:
    @pytest.mark.parametrize('keyword', ['смартфон'])
    def test_search(
        self,
        keyword: str,
            bee_home_page: BeeHomePage,
            bee_search_page: BeeSearchPage
    ):
        bee_home_page.visit(BASE_URL)
        bee_home_page.navbar.open_search()
        bee_home_page.navbar.search_modal.find_result(
            keyword, result_number=0
        )

        bee_search_page.product_present(product=keyword)