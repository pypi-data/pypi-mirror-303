import logging
import re
from typing import Optional, List, Union, Pattern

from playwright.sync_api import Playwright, Browser, Page, Locator, expect

from ..cfgloader import AppCfg
from . import constants

def get_browser(appcfg: AppCfg, playwright: Playwright) -> Optional[Browser]:
    if playwright is None:
        mylogger.debug('No playwright')
        return None

    mylogger = logging.getLogger(__name__)

    is_headless = False
    if appcfg.get(constants.CFG_KEY_HEADLESS_MODE) and appcfg.get(constants.CFG_KEY_HEADLESS_MODE).lower() == 'true':
        is_headless = True

    cfg_value = appcfg.get(constants.CFG_KEY_BROWSER_TYPE)
    if cfg_value and cfg_value.lower() == 'chrome':
        mylogger.debug('Chrome type browser return')
        return playwright.chromium.launch(headless=is_headless)
    elif cfg_value and cfg_value.lower() == 'firefox':
        mylogger.debug('Firefox type browser return')
        return playwright.firefox.launch(headless=is_headless)
    elif cfg_value and cfg_value.lower() == 'webkit':
        mylogger.debug('Webkit type browser return')
        return playwright.webkit.launch(headless=is_headless)

    mylogger.debug('No playwright return')
    return None

def navigate_to(page: Page, explicit_waittime: int, page_url: str, match_title: Union[Pattern[str], str], retry_count: int = 0) -> bool:
    mylogger = logging.getLogger(__name__)

    tryCount = 0
    while tryCount <= retry_count:
        tryCount += 1
        try:
            mylogger.debug(f'Loading URL - ({tryCount}:{retry_count}): {page_url}')
            page.goto(page_url)

            expect(page).to_have_title(match_title, timeout=explicit_waittime * 1000)

            if tryCount > 1:
                mylogger.info(f'Retry success at count: {tryCount}')
            return True
        except AssertionError:
            mylogger.error(f'Page title not match - ({tryCount}:{retry_count}) with "{match_title}":"{page.title()}"')

    return False

def check_title(page: Page, explicit_waittime: int, pattern: Union[Pattern[str], str]) -> bool:
    mylogger = logging.getLogger(__name__)
    try:
        expect(page).to_have_title(pattern, timeout=explicit_waittime * 1000)
        return True
    except AssertionError:
        mylogger.error(f'Page title not match with "{pattern}":"{page.title()}"')
    return False

def check_url(page: Page, explicit_waittime: int, pattern: Union[Pattern[str], str]) -> bool:
    mylogger = logging.getLogger(__name__)
    try:
        expect(page).to_have_url(pattern, timeout=explicit_waittime * 1000)
        return True
    except AssertionError:
        mylogger.error(f'Current URL does not match with "{pattern}":"{page.url}"')
    return False

def expect_to_be_attached(locator: Locator, explicit_waittime: int) -> bool:
    mylogger = logging.getLogger(__name__)
    try:
        expect(locator).to_be_attached(timeout=explicit_waittime * 1000)
        return True
    except AssertionError:
        mylogger.error('Cannot get element by locator')
        mylogger.debug(f'Page source dump: {locator.page.content()}')
    return False

def expect_to_be_visible(locator: Locator, explicit_waittime: int) -> bool:
    mylogger = logging.getLogger(__name__)
    try:
        expect(locator).to_be_visible(timeout=explicit_waittime * 1000)
        return True
    except AssertionError:
        mylogger.error('Element not visible')
        mylogger.debug(f'Page source dump: {locator.page.content()}')
    return False

def expect_to_have_count(locator: Locator, explicit_waittime: int, count: int) -> bool:
    mylogger = logging.getLogger(__name__)
    try:
        expect(locator).to_have_count(count, timeout=explicit_waittime * 1000)
        return True
    except AssertionError:
        mylogger.error('Element count not match by locator')
        mylogger.debug(f'Page source dump: {locator.page.content()}')
    return False
