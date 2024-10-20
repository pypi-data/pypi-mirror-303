from typing import Dict, Optional
import os
import logging
from jproperties import Properties

# Combine cfgloader and logcfg
from .logcfg import DEFAULT_LOGGING_CFG_NAME
from .logcfg import load as load_logcfg

DEFAULT_APP_CFG_NAME = 'app.properties'


class AppCfg:
    def __init__(self, targetCfgPath: str = DEFAULT_APP_CFG_NAME) -> None:
        # Define internal logger
        self.mylogger = logging.getLogger(__name__)
        # Load config into map
        self.propertyMap = self.__load(targetCfgPath)


    def __load(self, targetCfgPath: str) -> Dict[str, str]:
        self.mylogger.debug('Loading appCfg file: %s' % targetCfgPath)

        cfgMap: Dict[str, str] = {}
        properties_tuple = Properties()

        # if cfg file not exist, return empty dictionary
        if not os.path.isfile(targetCfgPath):
            self.mylogger.info('appCfg not exist !!! path: %s' % targetCfgPath)
            return cfgMap

        # Load the app config file
        with open(targetCfgPath, 'rb') as cfg_file:
            properties_tuple.load(cfg_file)

        # Migrate tuple into dictionary
        for key in properties_tuple.keys():
            cfgMap[key] = str(properties_tuple[key].data)

        return cfgMap
    
    def debug_content(self) -> None:
        self.mylogger.debug('Listing appProperties ...')

        # Just to list out the content to debug log
        for cfg_tuple in self.propertyMap.items():
            self.mylogger.debug('%s : %s' % (cfg_tuple[0], cfg_tuple[1]))

    def get(self, key: str, include_env_variables = True, default_value: Optional[str] = None) -> Optional[str]:
        if include_env_variables:
            #We need replace all '.' value with '_' for environment variables
            env_var = os.environ.get(key.replace('.', '_'))

            #If environment variable exist, just return it (as expected env override cfg value)
            if env_var:
                return env_var
            
        #If no env_var, then just get from cfg
        return_value = self.propertyMap.get(key)
        if return_value is None and default_value is not None:
            return default_value
        return return_value
    
    def remove(self, key: str) -> Optional[str]:
        if key in self.propertyMap:
            return self.propertyMap.pop(key)
        
        return None
    
    