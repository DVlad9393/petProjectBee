import allure
import pytest
import sys
import os

from pages.bee_basket_page import BeeBasketPage
from pages.bee_planb_page import BeePlanBPage

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from playwright.sync_api import Page, sync_playwright

from pages.bee_home_page import BeeHomePage
from pages.bee_search_page import BeeSearchPage


@pytest.fixture(scope='function')
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        chromium = playwright.chromium.launch(headless=False,args=["--start-maximized", "--window-position=0,0"])
        context = chromium.new_context(viewport={"width": 1600, "height": 900}, record_video_dir = "allure-results/")
        page = context.new_page()

        yield page
        allure.attach(
            page.screenshot(),
            name='screenshot',
            attachment_type=allure.attachment_type.PNG,
        )

        video = page.video.path()

        page.close()
        context.close()

        allure.attach.file(
            video,
            name="video",
            attachment_type=allure.attachment_type.WEBM,
        )

@pytest.fixture(scope='function')
def bee_home_page(chromium_page: Page) -> BeeHomePage:
    return BeeHomePage(chromium_page)

@pytest.fixture(scope='function')
def bee_search_page(chromium_page: Page) -> BeeSearchPage:
    return BeeSearchPage(chromium_page)

@pytest.fixture(scope='function')
def bee_planb_page(chromium_page: Page) -> BeePlanBPage:
    return BeePlanBPage(chromium_page)

@pytest.fixture(scope='function')
def bee_basket_page(chromium_page: Page) -> BeeBasketPage:
    return BeeBasketPage(chromium_page)