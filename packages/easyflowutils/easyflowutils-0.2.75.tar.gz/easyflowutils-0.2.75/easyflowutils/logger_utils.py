import logging
import sys

import google.cloud.logging


# by this great doc: https://cloud.google.com/functions/docs/create-deploy-http-python
def configure_cloud_logger():
    client = google.cloud.logging.Client()
    client.setup_logging()

    logger = logging.getLogger()
    formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(filename)s:%(lineno)d | %(message)s")
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.handlers = []
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
