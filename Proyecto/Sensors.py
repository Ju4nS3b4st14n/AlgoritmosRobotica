from gpiozero import *
import time  


pin_number = 21 
pin_number2 = 20 
pin_number3 = 26 
button = Button(pin_number)
button2 = Button(pin_number2)
button3 = Button(pin_number3)

def sensor():
    
    if button.is_pressed:
        value = 1
    else:
        value = 0

    if button2.is_pressed:
        value1 = 1
        
    else:
        value1 = 0

    if button3.is_pressed:
        return value, value1
    else:
        time.sleep(1)
        return value, value1                                                                                                                                        

