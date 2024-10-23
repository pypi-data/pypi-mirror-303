from .logger import Logger


def get_logger(dd_api_key, dd_customer, environment, workspace_name, log_level):
    return Logger(dd_api_key, dd_customer, environment, workspace_name, log_level)
