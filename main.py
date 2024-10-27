import time
import RPi.GPIO as GPIO

from lcd_display import LCDDisplay

def main():
    lcd = LCDDisplay()

    message = "hello"
    binary_list = lcd.string_to_binary(message)
    lcd.write_message(binary_list)

    while(True):
        pass

if __name__ == "__main__":
    main()
