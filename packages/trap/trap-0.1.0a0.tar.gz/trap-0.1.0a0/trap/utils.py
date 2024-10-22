# Copyright (C) 2024 ASTRON (Netherlands Institute for Radio Astronomy)
# SPDX-License-Identifier: Apache-2.0

from time import monotonic

from .log import logger


def log_time(log_level="info"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = monotonic()
            result = func(*args, **kwargs)
            end_time = monotonic()
            getattr(logger, log_level)(
                f"Function `{func.__name__}` took {end_time-start_time} seconds"
            )
            return result

        return wrapper

    return decorator
