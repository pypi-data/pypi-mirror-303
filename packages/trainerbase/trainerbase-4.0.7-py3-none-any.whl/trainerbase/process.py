from contextlib import suppress
from itertools import cycle
from os import _exit as force_exit
from typing import cast

from psutil import Process, pid_exists
from pymem import Pymem
from pymem.exception import ProcessNotFound

from trainerbase.config import pymem_config
from trainerbase.logger import logger


def attach_to_process() -> Pymem:
    process_names = pymem_config["process_names"]

    if not process_names:
        raise ValueError("Empty process name list")

    logger.info(f"Waiting for process in: {process_names}")

    with suppress(KeyboardInterrupt):
        for process_name in cycle(process_names):
            try:
                pm = Pymem(
                    process_name,
                    exact_match=pymem_config["exact_match"],
                    ignore_case=pymem_config["ignore_case"],
                )
            except ProcessNotFound:
                continue

            logger.info(f"Found {process_name}, pid: {pm.process_id}")

            return pm

    force_exit(0)


def shutdown_if_process_exited():
    if not pid_exists(cast(int, _pm.process_id)):
        logger.info("Game process exited. Shutting down.")
        force_exit(0)


def kill_game_process():
    logger.info("Killing game process.")
    Process(_pm.process_id).kill()


_pm = attach_to_process()
