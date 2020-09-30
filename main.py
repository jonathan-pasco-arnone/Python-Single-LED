# Creator: Jonathan P-A
# Date: September 30
# This program makes an LED turn on for 1 second and then off for 1 second repetedly
import time
import board
from digitalio import DigitalInOut, Direction

led = DigitalInOut(board.D1)
led.direction = Direction.OUTPUT

while True:
    led.value = True
    time.sleep(1)#wait 1 second
    led.value = False
    time.sleep(1)#wait 1 second