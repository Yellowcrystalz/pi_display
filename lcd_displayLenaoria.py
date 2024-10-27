import RPi.GPIO as GPIO
import time
from functools import wraps

class LCDDisplay():
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        self.pins: list = [25,26,17,27,22,24]
	#RS, E, db0, db1, db2, db3

        [GPIO.setup(pin, GPIO.OUT) for pin in self.pins]
        self.clear_display()
 
    def clear_display(self):
        for pin in self.pins:
            GPIO.output(pin, False)   

    def set_write(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            GPIO.output(self.pins[1], True)
            func(self, *args, **kwargs)
            GPIO.output(self.pins[1], False)

        return wrapper

    
    def write_message(self, binary_list: list) -> None:
        for binary in binary_list:
            self.write(binary[3:])        
            self.write(binary[:3])        

    
    @set_write
    def write(self, binary: str) -> None:
        for i in self.pins:
                if i < 6: #
                        GPIO.output(self.pins[i], binary[i] == "1")
    
    def string_to_binary(self, string):
        binary_list = list()

        for char in string:
            binary_list.append(self.char_to_binary(char))
        
        return binary_list

    def char_to_binary(self, char):
        binary = bin(ord(char))[2:].zfill(8)
        return binary
