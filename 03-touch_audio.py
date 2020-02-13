# Simple test of the MPR121 capacitive touch sensor library.
# Will print out a message when any of the 12 capacitive touch inputs of the
# board are touched.  Open the serial REPL after running to see the output.
# Author: Tony DiCola
import time
import board
import busio
import pygame
# Import MPR121 module.
import adafruit_mpr121

# Create I2C bus.
i2c = busio.I2C(board.SCL, board.SDA)

# Create MPR121 object.
mpr121 = adafruit_mpr121.MPR121(i2c)

# Note you can optionally change the address of the device:
#mpr121 = adafruit_mpr121.MPR121(i2c, address=0x91)

# Initialise pygame mixer with parameters to minimise latency
pygame.mixer.pre_init(48000,-16,2,1024)

# Initialise pygame module
pygame.init()

# Load samples
amen_1_4 = pygame.mixer.Sound("/home/pi/touch_dnb/amen/amen_1_4.wav")
amen_2_4 = pygame.mixer.Sound("/home/pi/touch_dnb/amen/amen_2_4.wav")
amen_3_4 = pygame.mixer.Sound("/home/pi/touch_dnb/amen/amen_3_4.wav")
amen_4_4 = pygame.mixer.Sound("/home/pi/touch_dnb/amen/amen_4_4.wav")

# Loop forever testing each input and printing when they're touched.
while True:
	if mpr121[0].value:
		print ('input 0 touched')
		amen_1_4.play()

	if mpr121[1].value:
                print ('input 0 touched')
                amen_2_4.play()
	if mpr121[2].value:
                print ('input 0 touched')
                amen_3_4.play()
	if mpr121[3].value:
                print ('input 0 touched')
                amen_4_4.play()
