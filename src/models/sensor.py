from typing import Dict, Literal, Tuple
from time import sleep, time

from board import I2C
from adafruit_mpu6050 import MPU6050


T_Sensor_Data = Dict[Literal["x", "y", "z"], float]

bus = I2C()
sensor = MPU6050(bus)


class Sensor:
    DEFAULT_SLEEP_TIME: float = 0.1
    SETTLE_TIME: float = 4.0
    CALIBRATION_TIME: float = 10.0
    CALIBRATED: bool = False

    def __init__(self, sleep_time: float = DEFAULT_SLEEP_TIME):
        self.sensor = sensor
        self.sleep_time = sleep_time
        self.__value: T_Sensor_Data = {"x": 0, "y": 0, "z": 0}

    def _get_data(self, data_type: Literal["accel", "gyro"] = None) -> T_Sensor_Data:
        sleep(self.sleep_time)
        value = (0, 0, 0)

        match data_type:
            case "accel": value = self.sensor.acceleration
            case "gyro": value = self.sensor.gyro
            case None: pass
            case _: raise ValueError("Invalid sensor data type")

        return {"x": value[0], "y": value[1], "z": value[2]}

    def __read(self) -> None:
        self.__value = self._get_data()


class Accelerometer(Sensor):
    def __init__(self, sleep_time: float = super().DEFAULT_SLEEP_TIME):
        super().__init__(sleep_time)

    @property
    def accel(self) -> T_Sensor_Data:
        self.__read()
        return self.__value

    def __read(self) -> None:
        self.__value = super()._get_data("accel")


class Gyroscope(Sensor):
    def __init__(self, sleep_time: float = super().DEFAULT_SLEEP_TIME):
        super().__init__(sleep_time)

    @property
    def angle(self) -> T_Sensor_Data:
        self.__read()
        return self.__value

    def __read(self) -> None:
        self.__value = super()._get_data("gyro")

    def __calibrate(self) -> Tuple[float, float, float]:
        sleep(self.SETTLE_TIME)

        offsets = [0, 0, 0]
        # Placeholder for number of calculations we get from the mpu
        num_of_points = 0
        # We get the current time and add the calibration time
        end_loop_time = time() + self.CALIBRATION_TIME

        # We end the loop once the calibration time has passed
        while end_loop_time > time():
            offsets[0] += self.angle["x"]
            offsets[1] += self.angle["y"]
            offsets[2] += self.angle["z"]

            num_of_points += 1

            if num_of_points % 100 == 0:
                print(f"Calibrating Gyro{'.' * (num_of_points % 4)}")

        print(f"Calibration complete!")

        # We divide by the length to get the mean
        offsets = [offset / num_of_points for offset in offsets]

        super().CALIBRATED = True

        return offsets[0], offsets[1], offsets[2]
