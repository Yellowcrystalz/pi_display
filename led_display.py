#import RPi.GPIO as GPIO
import time

# GPIO.setwarnings(False)
# GPIO.setmod(GPIO.BCM)
# GPIO.setup()

def main():
    pins = {
        22, # db0
        23, # db1
        24, # db2
        25, # db3
        5,  # db4
        6,  # db5
        12, # db6
        13,  # db7

        17, # RS
        27 # RW
    }

    # setup_display(pins)

# def setup_display(pins):
#     for pin in pins:
#         GPIO.setup(pin, GPIO.OUT)

# def clear_display(pins):
#     for pin in pins:
#         if pin != 22:
#             GPIO.output(pin, False)
#         else:
#             GPIO.output(pin, True)

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