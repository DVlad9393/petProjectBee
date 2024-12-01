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


@pytest.fixture(scope='function', params=['chromium'])
def browser_page(request) -> Page:
    '''
    :params browser_name: 'chromium', 'firefox', 'webkit'
    '''
    browser_name = request.param
    with sync_playwright() as playwright:
       browser = getattr(playwright, browser_name).launch(headless=False, args=["--start-maximized", "--window-position=0,0"])
       context = browser.new_context(viewport={"width": 1600, "height": 900}, record_video_dir="allure-results/")
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
def bee_home_page(browser_page: Page) -> BeeHomePage:
    return BeeHomePage(browser_page)

@pytest.fixture(scope='function')
def bee_search_page(browser_page: Page) -> BeeSearchPage:
    return BeeSearchPage(browser_page)

@pytest.fixture(scope='function')
def bee_planb_page(browser_page: Page) -> BeePlanBPage:
    return BeePlanBPage(browser_page)

@pytest.fixture(scope='function')
def bee_basket_page(browser_page: Page) -> BeeBasketPage:
    return BeeBasketPage(browser_page)