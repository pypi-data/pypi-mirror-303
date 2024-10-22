import logging
import sys
import os
import json
import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
from functools import wraps


class WorkflowLogger:
    def __init__(self):
        self.logger = logging.getLogger("WorkflowLogger")
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log(self, message: str, step: str = None, level: str = "INFO"):
        log_message = f"Step: {step} - {message}" if step else message
        if level == "ERROR":
            self.logger.error(log_message)
        elif level == "WARNING":
            self.logger.warning(log_message)
        else:
            self.logger.info(log_message)


class SDKLogger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SDKLogger, cls).__new__(cls)
            cls._instance._initialize_logger()
        return cls._instance

    def _initialize_logger(self):
        self.logger = logging.getLogger("KubiyaSDKLogger")
        self.logger.setLevel(logging.INFO)
        handler = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # Initialize Sentry if SENTRY_DSN is set
        self.sentry_dsn = os.environ.get("SENTRY_DSN")
        if self.sentry_dsn:
            self._initialize_sentry()

    def _initialize_sentry(self):
        sentry_logging = LoggingIntegration(
            level=logging.INFO, event_level=logging.ERROR
        )
        sentry_sdk.init(
            dsn=self.sentry_dsn,
            integrations=[sentry_logging],
            traces_sample_rate=1.0,
            enable_tracing=True,
        )

    def log(self, message: str, component: str = None, level: str = "INFO", **kwargs):
        log_message = f"Component: {component} - {message}" if component else message

        with sentry_sdk.start_span(op="log", description=f"log_{level.lower()}"):
            sentry_sdk.set_tag("component", component)
            sentry_sdk.set_context("log_details", {"message": message, **kwargs})

            if level == "ERROR":
                self.logger.error(log_message, extra=kwargs)
                sentry_sdk.capture_exception()
            elif level == "WARNING":
                self.logger.warning(log_message, extra=kwargs)
            elif level == "DEBUG":
                self.logger.debug(log_message, extra=kwargs)
            else:
                self.logger.info(log_message, extra=kwargs)

    def set_level(self, level: str):
        self.logger.setLevel(getattr(logging, level.upper()))

    def span(self, name):
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                with sentry_sdk.start_span(op=name):
                    return func(*args, **kwargs)

            return wrapper

        return decorator


sdk_logger = SDKLogger()


def configure_logger(level="INFO", json_mode=False):
    sdk_logger.set_level(level)
    if json_mode or os.environ.get("KUBIYA_LOG_OUTPUT_FORMAT", "").lower() == "json":

        class JsonFormatter(logging.Formatter):
            def format(self, record):
                log_data = {
                    "timestamp": self.formatTime(record, self.datefmt),
                    "name": record.name,
                    "level": record.levelname,
                    "message": record.getMessage(),
                }
                if hasattr(record, "component"):
                    log_data["component"] = record.component
                if record.exc_info:
                    log_data["exception"] = self.formatException(record.exc_info)
                return json.dumps(log_data)

        for handler in sdk_logger.logger.handlers:
            handler.setFormatter(JsonFormatter())


def span(name):
    return sdk_logger.span(name)
