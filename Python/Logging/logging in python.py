import logging

import logging.config

logging.config.fileConfig('logging.conf')

logger = logging.getLogger('smpleExample')
logger.debug('This is a debug message')