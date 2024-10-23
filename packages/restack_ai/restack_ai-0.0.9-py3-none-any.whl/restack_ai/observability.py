import logging
import os
from temporalio.runtime import LoggingConfig, LogForwardingConfig, TelemetryFilter
from typing import Optional, Dict, Any


formatter = logging.Formatter('[%(levelname)s]:[%(name)s]: %(message)s')

root_logger = logging.getLogger()
root_logger.setLevel(os.getenv('RESTACK_LOG_LEVEL', 'INFO'))

for handler in root_logger.handlers[:]:
    root_logger.removeHandler(handler)

handler = logging.StreamHandler()
handler.setFormatter(formatter)
root_logger.addHandler(handler)
class RestackLogger:
    def __init__(self, name: str = 'restack'):
        self.logger = logging.getLogger(name)
    
    def set_level(self, level: str):
        self.logger.setLevel(getattr(logging, level.upper()))

    def debug(self, message: str, meta: Optional[Dict[str, Any]] = None):
        self._log(logging.DEBUG, message, meta)

    def info(self, message: str, meta: Optional[Dict[str, Any]] = None):
        self._log(logging.INFO, message, meta)

    def error(self, message: str, meta: Optional[Dict[str, Any]] = None):
        self._log(logging.ERROR, message, meta)

    def _log(self, level: int, message: str, meta: Optional[Dict[str, Any]] = None):
        extra = {'meta': meta} if meta else None
        self.logger.log(level, message, extra=extra)

logger = RestackLogger()

def forward_to_default_logger(level: int, target: str, message: str):
    log_method = getattr(logger, logging.getLevelName(level).lower(), logger.info)
    log_method(f"[Temporal:{target}] {message}")

log_level = os.getenv('RESTACK_LOG_LEVEL', 'INFO')

temporal_logging_config = LoggingConfig(
    filter=TelemetryFilter(
        core_level=getattr(logging, log_level),
        other_level=getattr(logging, log_level),
    ),
    forwarding=LogForwardingConfig(
        logger=logger
    ),
)

logging.basicConfig(level=getattr(logging, log_level))

__all__ = ['logger']