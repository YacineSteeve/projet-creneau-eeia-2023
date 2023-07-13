import sys
from os import system

from .logger import logger


def syscall(command: str, required: bool = False, retry: bool = True):
    max_calls_before_cancel: int = 3

    for _ in range(max_calls_before_cancel):
        try:
            if system(command) == 0:
                return

            if not retry:
                logger.warning(f"Command '{command}' failed")
                break

        except KeyboardInterrupt:
            logger.warning(f"Command '{command}' cancelled")

        except Exception:
            logger.exception(f"Command '{command}' failed")

        if required:
            logger.error(f"Unable to execute '{command}'. Try to run it manually.")
            sys.exit(1)


if __name__ == "__main__":
    syscall("ls -l")
    syscall("clear")
