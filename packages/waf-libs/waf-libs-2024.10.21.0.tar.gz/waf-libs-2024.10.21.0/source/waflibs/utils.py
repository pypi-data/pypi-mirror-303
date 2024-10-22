"""
general utils
"""

import json
import os
import subprocess

from waflibs import log

logger = log.logger().get_logger()


def get_env_var(var, default=None):
    env_var = os.environ.get(var, default)
    logger.debug(f"env var: {env_var}")

    return env_var


get_env = get_env_var


def shell_command(
    cmd,
    cwd=None,
    dry_run=False,
    shell=False,
    check=False,
    capture_output=True,
    pipe=False,
    input=None,
    split=True,
    env=None,
):
    """execute shell command"""

    logger.debug(f"original shell command: {cmd}")
    command = cmd
    if split and type(command) is str:
        logger.debug("command is of type string... splitting")

        command = command.split(" ")

        logger.debug(f"shell command arr: {command}")
        logger.debug(f"shell command to execute: {' '.join(command)}")
    else:
        logger.debug(f"split is false and/or command type is not a string")

    if dry_run:
        return (
            "would return stdout",
            "would return stderr",
            "would return process",
        )
    else:
        logger.debug(f"env: {env}")
        logger.debug(f"input: {input}")

        stdout = None
        stderr = None
        if pipe:
            stdout = subprocess.PIPE
            capture_output = False

        process = subprocess.run(
            command,
            text=True,
            cwd=cwd,
            shell=shell,
            capture_output=capture_output,
            check=check,
            input=input,
            stdout=stdout,
            stderr=stderr,
            env=env,
        )
        if capture_output:
            return (process.stdout.strip(), process.stderr.strip(), process)
        else:
            return process


run_command = shell_command


def write_json_file(contents, filename):
    """write json file to disk"""

    if type(filename) == str:
        f = open(filename, "w")
    else:
        f = filename
    f.write(json.dumps(contents, indent=2))
    f.close()
