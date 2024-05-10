import json
import os
import logging

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='./data/log.txt', filemode='a')

def get_config():
    try:
        if os.path.exists('./data'):
            logger.info('Data directory exists')
        else:
            os.makedirs('./data')
            logger.info('Data directory created')        
        file = open('./data/config.json', 'r')
        config = json.load(file)
        file.close()
        logger.info('Config file loaded')
    except FileNotFoundError:
        file = open('./data/config.json', 'w')
        config = {
            "timePoints": {
                'workTime': 30, # 30 minutes
                'breakTime': 10, # 10 minutes
                'sleepTime': 23, # 11 PM
            },
            "data": {
                "mode": "file",
                "path": "./data/data.json",
            },
        }
        json.dump(config, file)
        file.close()
        logger.info('Config file created')
    except Exception as e:
        logger.error(f'Error: {e}')
        config = None
        logger.info('Config file not loaded')
        exit(1)
    return config