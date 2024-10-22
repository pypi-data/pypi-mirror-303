import logging

from waflibs import (
    arg_parse,
    config,
    constants,
    database,
    dns,
    error,
    filedir,
    git,
    log,
    secrets,
    text,
    uri,
    utils,
)

program_name = constants.PROGRAM_NAME

logger = logging.getLogger(program_name)
logger.debug(f"program name: {program_name}")
logger.debug(f"logger name: {logger.name}")
logger.debug(f"logger level: {logger.level}")
