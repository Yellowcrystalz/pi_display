import RPi.GPIO as GPIO
import time

pins = [
    17, # db0
    27, # db1
    22, # db2
    23, # db3
    24, # db4
    25, # db5
    5,  # db6
    6,  # db7

    13, # RS
]

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    setup_display(pins)
    turn_on_display(pins)

    while(True):
        pass


def setup_display(pins: list) -> None:
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

def turn_on_display(pins: list) -> None:
    for i in range(len(pins)):
        if i > 3:
            GPIO.output(pins[i], False) 
        else:
            GPIO.output(pins[i], True)

def clear_display(pins):
    for pin in pins:
        if pin != 22:
            GPIO.output(pin, False)
        else:
            GPIO.output(pin, True)

def string_to_char_list(string):
    string_list = string.split()
    return string_list

def char_to_binary(char):
    binary = bin(ord(char))[2:].zfill(8)
    return binary

def write_char_display(ascii):
    pass

if __name__ == "__main__":
    main()