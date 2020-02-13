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

# Initialise pygame mixer with parameters to minimise latency
pygame.mixer.pre_init(48000,-16,2,1024)

# Initialise pygame module
pygame.init()

# Load samples
amen_1_4 = pygame.mixer.Sound("/home/pi/touch_dnb/amen/amen_1_4.wav")
amen_2_4 = pygame.mixer.Sound("/home/pi/touch_dnb/amen/amen_2_4.wav")
amen_3_4 = pygame.mixer.Sound("/home/pi/touch_dnb/amen/amen_3_4.wav")
amen_4_4 = pygame.mixer.Sound("/home/pi/touch_dnb/amen/amen_4_4.wav")
last_touched = mpr121.touched()


breaks = [amen_1_4, amen_2_4, amen_3_4, amen_4_4]

while True:
    current_touched = mpr121.touched()
    # Check each pin's last and current state to see if it was pressed or released.
    for i in range (4):
        # Each pin is represented by a bit in the touched value. A value of 1
        # means the pin is being touched, and 0 means it is not being touched.
        pin_bit = 1 << i
        # First check if transitioned from not touched to touched.
        if current_touched & pin_bit and not last_touched & pin_bit:
            print ('{0} touched!'.format(i))

            # stop any other playback to keep things monophonic
            pygame.mixer.stop()

            # sound playback here
            breaks[i].play()

        if not current_touched & pin_bit and last_touched & pin_bit:
            print ('{0} released!'.format(i))
    last_touched = current_touched
    # time.sleep(0.01)
