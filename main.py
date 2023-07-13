import platform
import sys
from typing import Dict

from src.utils.syscall import syscall
from src.utils.logger import logger
from src.models.main_car import MainCar


def main():
    modes_execs: Dict[int, str] = {
        1: "./src/versions/manual/main.py",
        2: "./src/versions/trajectory/main.py",
        3: "./src/versions/rl/main.py",
    }
    default_mode: int = 1

    car = MainCar()
    logger.info(car)

    logger.debug(
        "Available modes:"
        "\n1. Manual"
        "\n2. Trajectory"
        "\n3. Reinforcement Learning"
        "\n4. Exit"
        "\n\n --> Choose a mode (1-4): "
    )

    try:
        mode: int = int(input())

        if mode == 4:
            logger.warning("Exit App")
            sys.exit()

        syscall(f'python3 {modes_execs.get(mode, default_mode)}', retry=False)

    except KeyboardInterrupt:
        logger.warning("Exit App")
        sys.exit()

    except Exception:
        logger.error("Something went wrong.")


if __name__ == "__main__":
    PYTHON_MIN_VERSION: tuple = (3, 10)
    OS_TO_RUN: str = "Linux"

    # Clear the console
    syscall("clear")

    logger.info("Start App")

    if platform.system() != OS_TO_RUN:
        logger.error(f"The app can only be run on a {OS_TO_RUN} system.")
        logger.warning("Exit App")
        sys.exit()

    if sys.version_info[0:2] < PYTHON_MIN_VERSION:
        logger.error(
            f"Python version too old to run the app. "
            f"Minimum required version: {PYTHON_MIN_VERSION}"
        )
        logger.warning("Exit App")
        sys.exit()

    # Install required python3-smbus package
    syscall("sudo apt install python3-smbus", required=True)

    main()
