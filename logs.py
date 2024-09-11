import os
import logging
from datetime import datetime, timedelta

log_folder = 'log'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Удаление логов старше определенного времени (например, 30 дней)
log_retention_days = 30  # Количество дней для хранения логов, можно изменить
now = datetime.now()

for filename in os.listdir(log_folder):
    file_path = os.path.join(log_folder, filename)
    if os.path.isfile(file_path):
        # Извлечение даты из имени файла, если имя в формате 'bot_ГГГГ-ММ-ДД.log'
        try:
            date_str = filename.split('_')[1].split('.')[0]
            file_date = datetime.strptime(date_str, '%Y-%m-%d')
            # Проверка, если файл старше log_retention_days
            if now - file_date > timedelta(days=log_retention_days):
                os.remove(file_path)
                logging.info(f"Removed old log file: {filename}")
        except (IndexError, ValueError):
            # Если имя файла не соответствует ожидаемому формату, пропустить его
            continue

# Get log file name from settings module
namelog = "bot"

# Generate log filename with current date
current_date = now.strftime('%Y-%m-%d')
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