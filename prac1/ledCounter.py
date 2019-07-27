#!/usr/bin/python3
"""
Names: Georg Janowski
Student Number: jnwgeo001
Prac: 1
Date: 27/07/2019
"""

# import Relevant Librares
import time
import RPi.GPIO as GPIO


# keeps track of the current LED state
state = 0

# define LED and pushbutton pins
LED1 = 12
LED2 = 0
LED3 = 0
BTN_DOWN = 0
BTN_UP = 16

def main():
    setup()
    print("press button to toggle LED")


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(BTN_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BTN_UP, GPIO.FALLING, callback=intDetect, bouncetime=300)

def intDetect(channel1):
    print("Interrupt detected")
    toggleLED()

def toggleLED():
    global state
    if state == 0:
        state = 1
    elif state == 1:
	state = 0
    else:
	print("Illegal state!")
    GPIO.output(LED1, state)


# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
	# main takes care of setup
        main()
	# infinite loop to keep program from terminating
	while(1):
	    time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
