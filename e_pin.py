import RPi.GPIO as GPIO
import time

def main():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.OUT)
    
	while(True):
		choice = input()

		if choice == "p":
			print("pulse")
			pulse_e()
		elif choice == "e":
			print("exiting")
			break
		else:
			continue

def pulse_e():
	GPIO.output(17, True)
	time.sleep(1)
	GPIO.output(17, False)

if __name__ == "__main__":
	main()
