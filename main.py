import os
import platform
import sys

from src.utils.syscall import syscall
from src.utils.logger import logger
from src.models.main_car import MainCar


def main():
    modes_execs = {
        "1": "./src/versions/rl/main.py",
        "2": "--help"
    }

    car = MainCar()
    logger.info(car)

    logger.info(
        "\nAvailable modes:"
        "\n1. RL"
        "\n2. Trajectory"
    )

    os.system(f'python3 {modes_execs.get(input("Choose mode: "), "--help")}')


if __name__ == "__main__":
    PYTHON_MIN_VERSION: tuple = (3, 10)

    # Clear the console
    syscall("clear")

    logger.info("Start App")

    if platform.system() != "Linux":
        logger.error("The app can only be run on a Linux system.")
        logger.warn("Exit App")
        sys.exit()

    if sys.version_info[0:2] < PYTHON_MIN_VERSION:
        logger.error("Python version too old to run the app.")
        logger.warn("Exit App")
        sys.exit()

    # Install required python3-smbus package
    syscall("sudo apt install python3-smbus", required=True)

    main()
