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
state = [0,0,0]

# define LED and pushbutton pins
LED0 = 11
LED1 = 13
LED2 = 15
BTN_DOWN = 16
BTN_UP = 18

def main():
    setup()
    print("press button to toggle LED")


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(LED0, GPIO.OUT)
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.setup(LED2, GPIO.OUT)
    GPIO.setup(BTN_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BTN_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BTN_DOWN, GPIO.FALLING, callback=countDown, bouncetime=300)
    GPIO.add_event_detect(BTN_UP, GPIO.FALLING, callback=countUp, bouncetime=300)

def countDown(channel1):
    print("countDown")
    global state
    state = [0,0,0]
    updateLEDs()

def countUp(channel2):
    print("countUp")
    global state
    state = [1,1,1]
    updateLEDs()

def updateLEDs():
    GPIO.output(LED0, state[0])
    GPIO.output(LED1, state[1])
    GPIO.output(LED2, state[2])


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
