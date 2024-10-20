from .webdriver_mgr import *

# wire driver
from seleniumwire import webdriver as wire_webdriver

from . import constants

def get_webdriver(appcfg: AppCfg) -> Union[wire_webdriver.Chrome, wire_webdriver.Firefox, None]:
   mylogger = logging.getLogger(__name__)

   is_headless = False
   if appcfg.get(constants.CFG_KEY_HEADLESS_MODE) and appcfg.get(constants.CFG_KEY_HEADLESS_MODE).lower() == 'true':
      is_headless = True

   cfg_value = appcfg.get(constants.CFG_KEY_BROWSER_TYPE)
   if cfg_value and cfg_value.lower() == 'chrome':
      chrome_option = wire_webdriver.ChromeOptions()
      
      if appcfg.get(constants.CFG_KEY_BROWSER_BINARY):
         chrome_option.binary_location = appcfg.get(constants.CFG_KEY_BROWSER_BINARY)

      if is_headless:
         chrome_option.add_argument('--headless=new')
         #override user-agent as some site disallow headless mode browser
         chrome_option.add_argument('--user-agent=' + constants.DEFAULT_USER_AGENT_CHROME)
      
      mylogger.debug('Chrome type driver return')
      return wire_webdriver.Chrome(options=chrome_option)
   elif cfg_value and cfg_value.lower() == 'firefox':
      firefox_option = wire_webdriver.FirefoxOptions()
      if appcfg.get(constants.CFG_KEY_BROWSER_BINARY):
         firefox_option.binary_location = appcfg.get(constants.CFG_KEY_BROWSER_BINARY)
      
      if is_headless:
         firefox_option.add_argument('-headless')

      mylogger.debug('Firefox type driver return')
      return wire_webdriver.Firefox(options=firefox_option)
   
   mylogger.debug('No webdriver')
   return None