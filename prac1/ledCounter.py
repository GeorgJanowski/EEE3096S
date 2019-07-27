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


# keeps track of the current count
counter = 0

# define LED and pushbutton pins
LEDs = [11,13,15]
BTN_DOWN = 16
BTN_UP = 18

def main():
    setup()

def setup():
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(LEDs, GPIO.OUT)
    GPIO.output(LEDs, 0)	# LEDs initially off

    GPIO.setup(BTN_DOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(BTN_UP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BTN_DOWN, GPIO.FALLING, callback=countDown, bouncetime=300)
    GPIO.add_event_detect(BTN_UP, GPIO.FALLING, callback=countUp, bouncetime=300)

def countDown(channel1):
    updateCount(-1)

def countUp(channel2):
    updateCount(1)

def updateCount(a):
    global counter
    counter = (counter + a) % 8				# update counter, wrap if needed
    state = [counter%2,(counter//2)%2,(counter//4)%2]	# update state
    GPIO.output(LEDs, (state[0],state[1],state[2]))


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
