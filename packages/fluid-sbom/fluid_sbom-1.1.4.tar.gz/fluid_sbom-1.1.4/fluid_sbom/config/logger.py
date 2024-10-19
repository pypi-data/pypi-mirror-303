from bugsnag.handlers import (
    BugsnagHandler,
)
import logging

LOGGER = logging.getLogger()


def configure_logger() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s",
    )
    handler = BugsnagHandler(extra_fields={"extra": ["extra"]})
    handler.setLevel(logging.WARNING)
    LOGGER.addFilter(handler.leave_breadcrumbs)
    LOGGER.addHandler(handler)
