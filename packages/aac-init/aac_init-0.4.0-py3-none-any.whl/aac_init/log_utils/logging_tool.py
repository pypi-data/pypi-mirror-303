# -*- coding: utf-8 -*-

# Copyright: (c) 2024, Rudy Lei <shlei@cisco.com>, Yang Bian <yabian@cisco.com>

import os
import logging
import threading

from logging.handlers import RotatingFileHandler

from aac_init.conf import settings


class StreamThreadFilter(logging.StreamHandler):
    def filter(self, record: logging.LogRecord) -> bool:
        return threading.current_thread() == threading.main_thread()


def setup_logger(
    log_file,
    log_level=None,
    console_stream=True,
    max_size=5 * 1024 * 1024,
    backup_count=1000,
):
    if not log_level:
        log_level = settings.DEFAULT_LOG_LEVEL

    log_levels = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
        "critical": logging.CRITICAL,
    }

    logger_name = log_file[:-4] if log_file.endswith(".log") else log_file
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s"
    )

    log_dir = os.path.join(settings.OUTPUT_BASE_DIR, "aac_init_log")
    if not os.path.exists(log_dir):
        os.makedirs(log_dir, exist_ok=True)
    log_file_path = os.path.join(log_dir, log_file)
    level = log_levels.get(log_level.lower(), logging.DEBUG)

    if console_stream and not any(
        isinstance(h, logging.StreamHandler) for h in logger.handlers
    ):
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if not any(
        isinstance(h, RotatingFileHandler) and h.baseFilename == log_file_path
        for h in logger.handlers
    ):
        file_handler = RotatingFileHandler(
            log_file_path, maxBytes=max_size, backupCount=backup_count, mode="a"
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


def netmiko_session_logger(log_file):
    """
    Setup netmiko session_log path.

    :param log_file: log file name
    """
    log_file_path = os.path.join(settings.OUTPUT_BASE_DIR, "aac_init_log", log_file)

    return log_file_path
