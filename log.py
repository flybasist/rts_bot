import logging
import settings

namelog = settings.namelog()

logging.basicConfig(level=logging.INFO, filename=namelog,filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

# logging.debug("A DEBUG Message")
# logging.info("An INFO")
# logging.warning("A WARNING")
# logging.error("An ERROR")
# logging.critical("A message of CRITICAL severity")