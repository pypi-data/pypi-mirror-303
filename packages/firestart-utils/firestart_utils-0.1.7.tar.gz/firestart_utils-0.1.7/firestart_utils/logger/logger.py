import json
import logging
import time
import requests

CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0
METRIC_URL = "https://api.datadoghq.eu/api/v2/series"
LOG_URL = "https://http-intake.logs.datadoghq.eu/api/v2/logs"

nameToLevel = {
        'CRITICAL': CRITICAL,
        'ERROR': ERROR,
        'WARNING': WARNING,
        'INFO': INFO,
        'DEBUG': DEBUG,
        'NOTSET': NOTSET,
}


class Logger:
    def __init__(self, dd_api_key, dd_customer, environment, workspace_name, level):
        self.dd_api_key = dd_api_key
        self.dd_customer = dd_customer
        self.environment = environment
        self.workspace_name = workspace_name
        self.level = self.checkLevel(level)

    def debug(self, source, message):
        logging.debug(f"Debug: {message}")
        self.handleLogging(self.is_extern_logging("DEBUG", source, message))

    def info(self, source, message):
        logging.info(f"Info: {message}")
        self.handleLogging(self.is_extern_logging("INFO", source, message))

    def warning(self, source,  message):
        logging.warning(f"Warning: {message}")
        self.handleLogging(self.is_extern_logging("WARNING", source, message))

    def error(self, source, message):
        logging.error(f"Error: {message}")
        self.handleLogging(self.is_extern_logging("ERROR", source, message))

    def critical(self, source, message):
        logging.critical(f"Critical: {message}")
        self.handleLogging(self.is_extern_logging("CRITICAL", source, message))

    def failed(self, source):
        body = self.generate_metric_log_body(source, False)
        self.send_log(body, METRIC_URL)

    def success(self, source):
        body = self.generate_metric_log_body(source, True)
        self.send_log(body, METRIC_URL)


    def generate_log_body(self, level, source, message):
        return {
            "ddsource": f'Horizon - {self.workspace_name}',
            "ddtags": f'env:{self.environment},customer:{self.dd_customer}',
            "hostname": f'Fabric - {self.dd_customer}',
            "message": f'{level}: {message}',
            "service": f'{source}',
            "status": f'{level}'
        }

    def generate_metric_log_body(self, source, successfull):
        metric = "azure.datafactory_factories.pipeline_succeeded_runs" if successfull else "azure.datafactory_factories.pipeline_failed_runs"
        return {
            "series": [
                {
                    "metric": metric,
                    "type": 1,
                    "points": [
                        {
                            "timestamp": f'{int(time.time())}',
                            "value": 1
                        }
                    ],
                    "tags": [
                       "customer:{0}".format(self.dd_customer),
                        "environment:{0}".format(self.environment),
                        "name:{0}".format(source),
                        "resource_group:{0}".format(self.workspace_name),
                    ]
                }
            ]
        }

    def is_extern_logging(self, level, source, message):
        if (self.level <= nameToLevel[level]):
            return self.generate_log_body(level, source, message);
        else:
            return None

    def send_log(self, body, url):
        headers = {"Content-Type": "application/json",
                   "DD-API-KEY": self.dd_api_key,
                   "Accept": "application/json"}
        json_data = json.dumps(body)
        response = requests.post(url, data=json_data, headers=headers)
        logging.info(f"Status Code: {response.status_code}")
        logging.info(f"Response Body: {response.text}")

    def setLevel(self, level):
        self.level = self.checkLevel(level)

    def checkLevel(self, level):
        if isinstance(level, int):
            rv = level
        elif str(level) == level:
            if level not in nameToLevel:
                raise ValueError("Unknown level: %r" % level)
            rv = nameToLevel[level]
        else:
            raise TypeError("Level not an integer or a valid string: %r"
                            % (level,))
        return rv

    def handleLogging(self, body):
        if body:
            self.send_log(body, LOG_URL)
        else:
            logging.info("No log sent")
