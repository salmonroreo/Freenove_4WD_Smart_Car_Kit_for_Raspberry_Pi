from motor import Ordinary_Car
from buzzer import Buzzer
from pca9685 import PCA9685
from ultrasonic import Ultrasonic
from infrared import Infrared
speaker = Buzzer()


PWM = Ordinary_Car()          
try:
    while True:
        direction = input("Enter direction (w/a/s/d/e): ")
        if direction == "w":
            PWM.set_motor_model(-2000, -2000, -2000, -2000)  # Forward
        elif direction == "s":
            PWM.set_motor_model(2000, 2000, 2000, 2000)      # Back
        elif direction == "a":
            PWM.set_motor_model(2000, 2000, -2000, -2000)    # Left
        elif direction == "d":
             PWM.set_motor_model(-2000, -2000, 2000, 2000)    # Right
        elif direction == "e":
            PWM.set_motor_model(0, 0, 0, 0) 
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    print ("\nEnd of program")
finally:
    PWM.close()

#Infrared code

line = Infrared()

line.read_one_infrared(self, channel: int)
