import logging
import sys

import orjson
import structlog

shared_log_processors = [
    structlog.contextvars.merge_contextvars,
    structlog.processors.add_log_level,
    structlog.processors.format_exc_info,
    structlog.processors.StackInfoRenderer(),
    structlog.processors.TimeStamper(fmt='iso', utc=True),
]


if not sys.stderr.isatty() and hasattr(sys.stderr, 'buffer'):
    processors = shared_log_processors + [
        structlog.processors.dict_tracebacks,
        structlog.processors.JSONRenderer(serializer=orjson.dumps),
    ]
    logger_factory = structlog.BytesLoggerFactory()
else:
    processors = shared_log_processors + [structlog.dev.ConsoleRenderer()]
    logger_factory = structlog.PrintLoggerFactory()

structlog.configure(
    processors=processors,
    logger_factory=logger_factory,
    wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
    context_class=dict,
    cache_logger_on_first_use=False,
)
