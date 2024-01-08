import logging

# we can set the logging level
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', filename='app.log', filemode='w')

# we can log 5 levels of messages
# debug
logging.debug("This is a debug message")
# info
logging.info("This in an nfo message")
# warning
logging.warning("This is a warning message")
# error
logging.error("This is an error message")
# critical
logging.critical("This is a critical message")
