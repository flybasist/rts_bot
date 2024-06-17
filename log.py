import os
import logging
import settings
from datetime import datetime

log_folder = 'log'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Get log file name from settings module
namelog = settings.namelog()

# Generate log filename with current date
current_date = datetime.now().strftime('%Y-%m-%d')
log_filename = f"{namelog}_{current_date}.log"
log_path = os.path.join(log_folder, log_filename)

# Check if the log file already exists
if os.path.exists(log_path):
    # Log file already exists, so we will append to it
    filemode = "a"
else:
    # Log file does not exist, create a new one
    filemode = "w"

logging.basicConfig(level=logging.INFO,
                    filename=log_path,
                    filemode=filemode,
                    format="%(asctime)s %(levelname)s %(message)s")

# Example usage of logging
logging.info("starting bot")

# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")