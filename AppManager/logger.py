### This file contain custom logging system.

from datetime import datetime
import logging
import os

## create the log folder, where all the logs are stored.
log_folder = os.path.join(os.getcwd(), 'Logs')

if not os.path.exists(log_folder):
    os.mkdir(log_folder)


## Define the log file path.
log_filename = datetime.now().strftime('logfile_%Y-%m-%d.log')
log_file_path = os.path.join(log_folder, log_filename)

## config the basic logger
logging.basicConfig(
    level=logging.DEBUG,
    filename=log_file_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)