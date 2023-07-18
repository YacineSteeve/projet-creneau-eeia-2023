from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)
import pygame
import time
# Initialiser Pygame
pygame.init()
# Initialiser la manette PS3
pygame.joystick.init()

# Vérifier le nombre de manettes connectées
num_joysticks = pygame.joystick.get_count()
if num_joysticks < 1:
    raise ValueError("Manette PS3 non détectée.")

# Obtenir la première manette (indice 0)
joystick = pygame.joystick.Joystick(0)
joystick.init()


# Création d'une fonction qui permet de changer d'intervalle bornée d'appartenance d'une variable à un autre intervalle######
def mape(x, in_min, in_max, out_min, out_max):
    v= ((x - in_min)*(out_max - out_min))/(in_max - in_min) + out_min
    return v

# Lire les données de la manette PS3
while True:
    pygame.event.pump()
    # Lire les axes
    #axis = []
    #for i in range(joystick.get_numaxes()):
    #print(joystick.get_axis(3))
    throttle = mape(joystick.get_axis(0),1,-1,-0.25,0.25)
    steering = int(mape(joystick.get_axis(3),1,-1,0,180))

    kit.continuous_servo[0].throttle = throttle
    kit.servo[1].angle = steering
    print("Throttle: ",throttle,"steering: ",steering)
    #time.sleep(0.01)
    #print("Axes: ", axis)
