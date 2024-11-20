import logging
import os

from . import BaseJsonHandler
from ansible_base.lib.logging.filters.otlp import JSONNLFormatter


class WatchedFileHandler(BaseJsonHandler):
    def __init__(self, filename=None, instance_id=None):
        if not filename:
            raise ValueError("Expected filename, got None")
        service_name = self.generate_service_name()
        handler = logging.handlers.WatchedFileHandler(filename)
        handler.setFormatter(JSONNLFormatter())
        super().__init__(handler, service_name=service_name)
