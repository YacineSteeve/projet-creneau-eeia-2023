#[ 0.1014398 , -0.03564281]), array([0.10158851, 0.0245431 ]), array([0.09945352, 0.02054024])]
#[ 0.10145212, -0.04234963]), array([0.10158047, 0.03143559]), array([0.09941305, 0.00589396]

import time
import board
import adafruit_mpu6050

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
mpu = adafruit_mpu6050.MPU6050(i2c)

while True:
    ax, ay, az = mpu.acceleration
    az_offset = az*0.10145212  -  0.04234963
    ay_offset = ay*0.10158047  +  0.03143559
    ax_offset = ax*0.09941305  +  0.00589396
     
    ax = ax - ax_offset
    ay = ay - ay_offset
    az = az - az_offset
    #print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration), end = "\r")
    #print("Z: %.2f m/s^2" % (az))
    #print("Temperature: %.2f C" % mpu.temperature)
    print(ay)
    #time.sleep(0.1)
    
