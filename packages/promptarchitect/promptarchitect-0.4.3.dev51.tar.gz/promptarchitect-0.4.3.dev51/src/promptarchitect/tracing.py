"""Specialized logging handlers for promptarchitect.

We allow promptarchitect to use logger instances from the logging module to write out
important messages during validation. We want to link these messages to the current
test session. We do this by forwarding the log messages as an event in the context
of a OpenTelemetry span.

The log processor in this module takes care of the forwarding. The trace exporter
in this module then links the log messages to the current test case.
"""

import logging
from opentelemetry import trace
import coloredlogs


class LogProcessor(logging.Handler):
    """A logging handler that forwards log messages to the current OpenTelemetry span.

    This handler is used to link log messages to the current test case. It forwards
    log messages as events in the context of the current OpenTelemetry span.

    """

    def emit(self, record: logging.LogRecord) -> None:
        """Emit a log record to the current OpenTelemetry span.

        Arguments
        ---------
        record : logging.LogRecord
            The log record to emit.
        """
        current_span = trace.get_current_span()

        current_span.add_event(
            name="promptarchitect.log.message",
            attributes={
                "source": record.name,
                "level": record.levelname,
                "message": record.getMessage(),
            },
        )


def setup_tracing() -> None:
    """Configure tracing for the CLI."""
    root_logger = logging.getLogger()

    # Log only errors for the HTTP communication
    logging.getLogger("httpx").setLevel(logging.ERROR)

    # Log the rest in pretty colors to the terminal.
    coloredlogs.install(level="INFO", logger=root_logger)
