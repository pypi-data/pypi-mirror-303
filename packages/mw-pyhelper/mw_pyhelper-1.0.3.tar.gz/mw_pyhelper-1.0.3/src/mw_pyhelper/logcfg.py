import logging
import logging.config
import yaml

DEFAULT_LOGGING_CFG_NAME = 'logging.yaml'

def load(targetCfgPath: str = DEFAULT_LOGGING_CFG_NAME) -> dict:
    # Load the logging config file
    with open(targetCfgPath, 'rt') as yaml_file:
        logging_cfg_map = yaml.safe_load(yaml_file.read())
    
    # init logging
    logging.config.dictConfig(logging_cfg_map)

    # return dictionary
    return logging_cfg_map
