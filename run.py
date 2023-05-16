"""Running the ETL application"""
import logging
import logging.config

import yaml

def main():
    """
    entry point to run the ETL job
    """
    # Parsing YAML file
    config_path = 'C:/Users/Andre Brito/Documents/ETL/etl/configs/report-config.yml'
    config = yaml.safe_load(open(config_path))
    # Configure logging
    log_config = config['Logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    logger.info("This is a test.")

if __name__ == '__main__':
    main()