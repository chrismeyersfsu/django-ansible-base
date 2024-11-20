import sys
import os
import logging

from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk.resources import Resource

from opentelemetry._logs import set_logger_provider


class BaseOTLPHandler(LoggingHandler):
    def __init__(self, service_name=None, instance_id=None):
        self.service_name = service_name or self.generate_service_name()
        self.instance_id = instance_id or os.uname().nodename

        logger_provider = LoggerProvider(
            resource=Resource.create(
                {
                    "service.name": self.service_name,
                    "service.instance.id": self.instance_id,
                }
            ),
        )
        set_logger_provider(logger_provider)

        # trace_provider = TracerProvider()

        super().__init__(level=logging.NOTSET, logger_provider=logger_provider)

    def get_service_name(self):
        self.service_name

    def generate_service_name(self):
        # TODO: Push the service name down
        return sys.argv[1] if len(sys.argv) > 1 else (sys.argv[0] or 'unknown_service')

    def emit(self, record: logging.LogRecord) -> None:
        # Calls provider exporters.export()
        return super().emit(record)