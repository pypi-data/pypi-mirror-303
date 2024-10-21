import json
import logging
import os
import random
import string
from logging.handlers import TimedRotatingFileHandler

from cnvrgv2.config import Config, GLOBAL_CNVRG_PATH


class CnvrgHttpErrorLogger:
    DEFAULT_KEEP_DURATION_DAYS = 7
    HTTP_ERROR_LOGGER = "http-error-logger"
    LOGS_DIR = os.path.join(GLOBAL_CNVRG_PATH, "logs")
    LOG_FILE_NAME = "cnvrg_http_errors.log"

    def __init__(self):
        # prepare command will create the config file if it does not exist
        config = Config()
        keep_duration_days = (
            config.keep_duration_days or
            CnvrgHttpErrorLogger.DEFAULT_KEEP_DURATION_DAYS
        )

        self.logger = logging.getLogger(CnvrgHttpErrorLogger.HTTP_ERROR_LOGGER)
        self.logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s \t [%(levelname)s] > %(message)s')

        if not os.path.isdir(CnvrgHttpErrorLogger.LOGS_DIR):
            os.makedirs(CnvrgHttpErrorLogger.LOGS_DIR)

        log_file_path = os.path.join(CnvrgHttpErrorLogger.LOGS_DIR, CnvrgHttpErrorLogger.LOG_FILE_NAME)
        handler = TimedRotatingFileHandler(
            log_file_path,
            when="midnight",
            backupCount=keep_duration_days
        )

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_http_error(self, method, url, headers=None, body=None, res_status=None, res_body=None):
        letters_and_digits = string.ascii_letters + string.digits
        log_id = ''.join(random.choice(letters_and_digits) for i in range(7))
        body_str = json.dumps(body, indent=4)
        details = {
            "LOG_ID": log_id,
            "METHOD": method,
            "URL": url,
            "HEADERS": headers,
            "BODY": body_str[0:400] if body else None,
            "RESPONSE_STATUS": res_status,
            "RESPONSE_BODY": res_body
        }

        if body and len(body_str) > 400:
            details["BODY"] = details["BODY"] + "..."
            body_log_file_path = os.path.join(CnvrgHttpErrorLogger.LOGS_DIR, "body_{}.log".format(log_id))
            with open(body_log_file_path, "w") as body_log:
                body_log.write(body_str)

        self.logger.error(str(details))
