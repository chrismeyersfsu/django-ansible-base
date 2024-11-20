import logging

from . import BaseJsonHandler

from ansible_base.lib.logging.filters.otlp import JSONNLFormatter


class OTLPStreamHandler(BaseJsonHandler):
    def __init__(self):
        handler = logging.StreamHandler()
        handler.setFormatter(JSONNLFormatter())
        super().__init__(handler)
