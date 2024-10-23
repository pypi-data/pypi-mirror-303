import logging
import os

log = logging.getLogger(__name__)
console = logging.StreamHandler()

if os.environ.get("foresight_log_level"):
    level = os.environ.get("foresight_log_level")
else:
    level = logging.INFO

log.setLevel(level) # set logger level
console.setLevel(level) # set console handler level

fmt = "%(asctime)s.%(msecs)03d\t%(name)-29s\t%(levelname)-8s\t%(funcName)s\t\t %(message)s"

# 2020-06-25 15:04:59
date_fmt = "%Y-%m-%d %H:%M:%S"

log_formatter = logging.Formatter(fmt, date_fmt)

console.setFormatter(log_formatter)

log.addHandler(console)


class GwReturnObj:
    """ An object intended mostly for internal use that has different
    attributes depending on which library and functionality utilises it, such
    as `status`, `buffer`, and `buffer_bytes`
    """

    def __init__(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items()]