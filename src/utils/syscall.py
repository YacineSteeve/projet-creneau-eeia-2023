import sys
from os import system

from .logger import logger

MAX_CALLS_BEFORE_CANCEL = 3


def syscall(command: str, required: bool = False) -> None:
    for _ in range(MAX_CALLS_BEFORE_CANCEL):
        try:
            if system(command) == 0:
                return
            logger.error(f"Unable to execute '{command}'. Try to run it manually.")

            if required:
                sys.exit(1)
        except KeyboardInterrupt:
            logger.warn(f"Command '{command}' cancelled")


if __name__ == "__main__":
    syscall("ls -l")
    syscall("clear")
