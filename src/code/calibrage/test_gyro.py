import board
import adafruit_mpu6050
import math

i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
mpu = adafruit_mpu6050.MPU6050(i2c)

import time

# Variables pour le calcul de l'angle
angle = 0.0
previous_time = time.time()
#previous_delta_angle = clear
filtered_wz = 0
alpha = 0.45

def low_pass_filter (prev_value, new_value):
    return alpha * prev_value + (1 - alpha) * new_value


while True:
    
    wx, wy, wz = mpu.gyro
    
    #wx = wx + 0.02543184073037816
    #wy = wy + 0.01878396537626835
    wz = wz + 0.036308645462233356
    
    #wz_fil = low_pass_filter (filtered_wz, wz)
    if abs(wz)  >= 0.0088: 
        wz_ =wz
    else:
        wz_ = 0.00001
    
        
    # Calculez le temps écoulé depuis la dernière mesure
    current_time = time.time()
    elapsed_time = current_time - previous_time
    
    # Calculez le changement d'angle
    delta_angle = wz_ * elapsed_time
    
    delta_angle    = math.degrees(delta_angle)
    #print(delta_angle)
    # Mettez à jour l'angle
    if abs(delta_angle) >= 0.001:
        angle += delta_angle
    
    #print(delta_angle,"angle",angle)
    # Affichez l'angle en temps réel
    print("Angle en temps réel : ", angle)
    #print(wz)
    # Mettez à jour le temps précédent pour la prochaine itération
    previous_time = current_time