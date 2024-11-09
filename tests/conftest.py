import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.sync_api import Page, sync_playwright

from pages.playwright_home_page import BeeHomePage
from pages.playwright_languages_page import BeeSearchPage


@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False)
        yield chromium.new_page()


@pytest.fixture(scope='function')
def bee_home_page(chromium_page: Page) -> BeeHomePage:
    return BeeHomePage(chromium_page)


@pytest.fixture(scope='function')
def bee_search_page(chromium_page: Page) -> BeeSearchPage:
    return BeeSearchPage(chromium_page)