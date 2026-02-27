import logging
import structlog
from packages.core.config import get_settings


def configure_logging() -> None:
    s = get_settings()

    # Base stdlib logging
    logging.basicConfig(level=getattr(logging, s.log_level, logging.INFO), format="%(message)s")

    # Structlog JSON output (good for ELK/Grafana/Loki later)
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, s.log_level, logging.INFO)
        ),
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.add_log_level,
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.JSONRenderer(),
        ],
    )


def get_logger(name: str = "ai_platform"):
    return structlog.get_logger(name)