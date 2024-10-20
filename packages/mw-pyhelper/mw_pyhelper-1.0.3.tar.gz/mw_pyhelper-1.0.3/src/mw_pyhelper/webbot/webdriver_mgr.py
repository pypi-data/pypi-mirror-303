import logging
from typing import Optional, List, Union
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

# normal webdriver
from selenium import webdriver

from ..cfgloader import AppCfg
from . import constants

#general method for getting webdriver
def get_webdriver(appcfg: AppCfg) -> Optional[RemoteWebDriver]:
   mylogger = logging.getLogger(__name__)

   is_headless = False
   if appcfg.get(constants.CFG_KEY_HEADLESS_MODE) and appcfg.get(constants.CFG_KEY_HEADLESS_MODE).lower() == 'true':
      is_headless = True

   cfg_value = appcfg.get(constants.CFG_KEY_BROWSER_TYPE)
   if cfg_value and cfg_value.lower() == 'chrome':
      chrome_option = webdriver.ChromeOptions()
      
      if appcfg.get(constants.CFG_KEY_BROWSER_BINARY):
         chrome_option.binary_location = appcfg.get(constants.CFG_KEY_BROWSER_BINARY)

      if is_headless:
         chrome_option.add_argument('--headless=new')
         #override user-agent as some site disallow headless mode browser
         chrome_option.add_argument('--user-agent=' + constants.DEFAULT_USER_AGENT_CHROME)
      
      mylogger.debug('Chrome type driver return')
      return webdriver.Chrome(options=chrome_option)
   elif cfg_value and cfg_value.lower() == 'firefox':
      firefox_option = webdriver.FirefoxOptions()
      if appcfg.get(constants.CFG_KEY_BROWSER_BINARY):
         firefox_option.binary_location = appcfg.get(constants.CFG_KEY_BROWSER_BINARY)
      
      if is_headless:
         firefox_option.add_argument('-headless')

      mylogger.debug('Firefox type driver return')
      return webdriver.Firefox(options=firefox_option)
   
   mylogger.debug('No webdriver')
   return None

def navigate_to(remote_webdriver: RemoteWebDriver, explicit_waittime: int, page_url: str, match_title: str, retry_count: int = 0, partial_match_only: bool = False) -> bool:
    mylogger = logging.getLogger(__name__)

    tryCount = 0
    while tryCount <= retry_count:
        tryCount += 1
        try:
            mylogger.debug('Loading URL - (%d:%d): %s' % (tryCount, retry_count, page_url))
            remote_webdriver.get(page_url)

            WebDriverWait(remote_webdriver, explicit_waittime).until(
                ExpectedConditions.title_is(match_title) \
                    if not partial_match_only else ExpectedConditions.title_contains(match_title)
            )
            if tryCount > 1:
                mylogger.info('Retry success at count: %d' % tryCount)
            return True
        except TimeoutException:
            mylogger.error('Page title not match - (%d:%d) with "%s":"%s"' % (tryCount, retry_count, match_title, remote_webdriver.title))

    return False

def check_url(remote_webdriver: RemoteWebDriver, explicit_waittime: int, pattern: str) -> bool:
    mylogger = logging.getLogger(__name__)
    try:
        WebDriverWait(remote_webdriver, explicit_waittime).until(
            ExpectedConditions.url_matches(pattern)
        )
        return True
    except TimeoutException:
        mylogger.error('Current URL does not match with "%s":"%s"' % (pattern, remote_webdriver.current_url))
    return False

def get_element_by_css(remote_webdriver: RemoteWebDriver, explicit_waittime: int, css_selector: str) -> Optional[WebElement]:
    mylogger = logging.getLogger(__name__)
    try:
        return WebDriverWait(remote_webdriver, explicit_waittime).until(
            ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )
    except TimeoutException:
        mylogger.error('Cannot get element by css: %s' % css_selector)
        mylogger.debug('Page source dump: %s' % remote_webdriver.page_source)
    return None

def find_element_by_css(remote_webdriver: RemoteWebDriver, css_selector: str) -> Optional[WebElement]:
    """No wait and no error log method, just get the element by css
    """
    try:
        return remote_webdriver.find_element(by=By.CSS_SELECTOR, value=css_selector)
    except NoSuchElementException:
        return None

def get_nested_element_by_css(remote_webdriver: RemoteWebDriver, explicit_waittime: int, parent_element: WebElement, css_selector: str) -> Optional[WebElement]:
    mylogger = logging.getLogger(__name__)
    try:
        return WebDriverWait(parent_element, explicit_waittime).until(
            ExpectedConditions.presence_of_element_located((By.CSS_SELECTOR, css_selector))
        )
    except TimeoutException:
        mylogger.error('Cannot get nested element by css: %s' % css_selector)
        mylogger.debug('Page source dump: %s' % remote_webdriver.page_source)
    return None

def find_nested_element_by_css(parent_element: WebElement, css_selector: str) -> Optional[WebElement]:
    """No wait and no error log method, just get the nested element by css
    """
    try:
        return parent_element.find_element(by=By.CSS_SELECTOR, value=css_selector)
    except NoSuchElementException:
        return None

def get_elements_by_css(remote_webdriver: RemoteWebDriver, explicit_waittime: int, css_selector: str) -> Optional[List[WebElement]]:
    mylogger = logging.getLogger(__name__)
    try:
        return WebDriverWait(remote_webdriver, explicit_waittime).until(
            ExpectedConditions.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector))
        )
    except TimeoutException:
        mylogger.error('Cannot get any element by css: %s' % css_selector)
        mylogger.debug('Page source dump: %s' % remote_webdriver.page_source)
    return None

def find_elements_by_css(remote_webdriver: RemoteWebDriver, css_selector: str) -> Optional[List[WebElement]]:
    """No wait and no error log method, just get list of elements by css
    """
    try:
        return remote_webdriver.find_elements(by=By.CSS_SELECTOR, value=css_selector)
    except NoSuchElementException:
        return None

def get_nested_elements_by_css(remote_webdriver: RemoteWebDriver, explicit_waittime: int, parent_element: WebElement, css_selector: str) -> Optional[List[WebElement]]:
    mylogger = logging.getLogger(__name__)
    try:
        return WebDriverWait(parent_element, explicit_waittime).until(
            ExpectedConditions.presence_of_all_elements_located((By.CSS_SELECTOR, css_selector))
        )
    except TimeoutException:
        mylogger.error('Cannot get any nested element by css: %s' % css_selector)
        mylogger.debug('Page source dump: %s' % remote_webdriver.page_source)
    return None

def find_nested_elements_by_css(parent_element: WebElement, css_selector: str) -> Optional[List[WebElement]]:
    """No wait and no error log method, just get list of nested elements by css
    """
    try:
        return parent_element.find_elements(by=By.CSS_SELECTOR, value=css_selector)
    except NoSuchElementException:
        return None
    
def get_pop_alert(remote_webdriver: RemoteWebDriver, explicit_waittime: int) -> Optional[Alert]:
    mylogger = logging.getLogger(__name__)
    try:
        return WebDriverWait(remote_webdriver, explicit_waittime).until(
            ExpectedConditions.alert_is_present()
        )
    except TimeoutException:
        mylogger.error('No alert at all')
        mylogger.debug('Page url: %s' % remote_webdriver.current_url)
    return None

def find_pop_alert(remote_webdriver: RemoteWebDriver) -> Optional[Alert]:
    try:
        return remote_webdriver.switch_to.alert
    except NoAlertPresentException:
        return None

def check_text_exist(remote_webdriver: RemoteWebDriver, explicit_waittime: int, css_selector: str, text: str) -> bool:
    mylogger = logging.getLogger(__name__)
    try:
        return WebDriverWait(remote_webdriver, explicit_waittime).until(
            ExpectedConditions.text_to_be_present_in_element((By.CSS_SELECTOR, css_selector), text)
        )
    except TimeoutException:
        mylogger.error('Text not exist by css: %s - %s' % (css_selector, text))
        mylogger.debug('Page source dump: %s' % remote_webdriver.page_source)
    return False
