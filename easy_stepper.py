#Step 0: Preamble
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#Program Title    : easy_stepper.py
#Code Written by  : Salty Scott
#Code Modified by : Matteo Perini
#This python script use 3 Raspberry Pins to drive a stepper motor thanks 
#to a Pololu A4988 driver.
#This code use:
#Pin 24 -> STEP (when the signal rise up)
#Pin 23 -> DIRECTION (left/right)
#Pin 25 -> ENABLE/DISABLE the driver
#
#Whit this script you can choose to do some steps in one direction.
#
#CODE EXAMPLE:
#
#python easy_stepper.py right 100 (do 100 steps in the right direction)
#
#python easy_stepper.py left 15 (do 15 steps in the left direction)
#
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
#Step 1: Import necessary libraries
#------------------------------------------------------------------------
#------------------------------------------------------------------------
import sys
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO more info
import time
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
#Step 2: Read arguements https://www.youtube.com/watch?v=kQFKtI6gn9Y
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#read the direction and number of steps; if steps are 0 exit
try:
    direction = sys.argv[1]
    steps = int(float(sys.argv[2]))
except:
    steps = 0
 
#print which direction and how many steps
print("You told me to turn %s %s steps.") % (direction, steps)
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
 
#Step 3: Setup the raspberry pi's GPIOs
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#use the broadcom layout for the gpio
gpio.setmode(gpio.BCM)
#GPIO23 = Direction
#GPIO24 = Step
#GPIO25 = Enable/Disable
gpio.setup(23, gpio.OUT)
gpio.setup(24, gpio.OUT)
gpio.setup(25, gpio.OUT)
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
 
#Step 4: Set direction of rotation
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#set the output to true for left and false for right
if direction == 'left':
    gpio.output(23, True)
elif direction == 'right':
    gpio.output(23, False)
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
 
#Step 5: Setup step counter and speed control variables
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#track the numebr of steps taken
StepCounter = 0
 
#waittime controls speed
WaitTime = 0.003
#------------------------------------------------------------------------
#------------------------------------------------------------------------
 
 
#Step 6: Let the magic happen
#------------------------------------------------------------------------
#------------------------------------------------------------------------
# Start main loop
while StepCounter < steps:
    
    #Enable the stepper driver
    gpio.output(25, False)
    #turning the gpio on and off tells the easy driver to take one step
    gpio.output(24, True)
    gpio.output(24, False)
    #time.sleep(WaitTime)
    StepCounter += 1
 
    #Wait before taking the next step...this controls rotation speed
    time.sleep(WaitTime)
#------------------------------------------------------------------------
#------------------------------------------------------------------------
gpio.output(25, True)
 
 
#Step 7: Clear the GPIOs so that some other program might enjoy them
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#relase the GPIO
gpio.cleanup()
#------------------------------------------------------------------------
#------------------------------------------------------------------------
