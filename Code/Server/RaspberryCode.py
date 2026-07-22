from motor import Ordinary_Car
from buzzer import Buzzer
from pca9685 import PCA9685
from ultrasonic import Ultrasonic
from infrared import Infrared
from servo import Servo
import time

speaker = Buzzer()

PWM = Ordinary_Car()
line = Infrared()

mode = input("M for Manuel and I for Infrared: ")

if mode == "m" or mode == "M":   
    print("Manual mode")       
    try:
        while True:
            direction = input("Enter direction (w/a/s/d/e): ")
            if direction == "w":
                PWM.set_motor_model(-750, -750, -750, -750)  # Forward
            elif direction == "s":
                PWM.set_motor_model(750, 750, 750, 750)      # Back
            elif direction == "a":
                PWM.set_motor_model(750, 750, -750, -750)    # Left
            elif direction == "d":
                PWM.set_motor_model(-750, -750, 750, 750)   # Right
            elif direction == "e":
                PWM.set_motor_model(0, 0, 0, 0) 
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print ("\nEnd of program")
    finally:
        PWM.close()

elif mode == "i" or mode == "I":
    print("Infrared Mode")
    try:
        while True:
            raw_state = line.read_all_infrared()
            white_state = 7 - raw_state
            left = line.read_one_infrared(1)
            center = line.read_one_infrared(2)
            right = line.read_one_infrared(3)

            print(f"[({left})({center})({right})] - Raw State: {raw_state} | White Logic State: {white_state}")

            # Check if all sensors detect BLACK (raw_state == 7 or white_state == 0)
            if raw_state == 7:
                PWM.set_motor_model(0, 0, 0, 0)  
                
            elif white_state == 2:               
                PWM.set_motor_model(-500, -500, -500, -500)
            elif white_state in (4, 6):          
                PWM.set_motor_model(750, 750, -750, -750)
                
            elif white_state in (1, 3):         
                PWM.set_motor_model(-750, -750, 750, 750)
            else:               
                PWM.set_motor_model(-500, -500, -500, -500)
                
            time.sleep(0.01)
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        print ("\nEnd of program")
    finally:
        PWM.set_motor_model(0, 0, 0, 0)
        if hasattr(line, 'close'): 
            line.close()
        PWM.close()

elif mode == "C" or mode == "c":


