# Write your code here :-)
from microbit import *

pins = [0, 0, 0]

uart.init(115200)

while True:
    display.set_pixel(4, 4, 9)
    if pin0.is_touched():
        pins[0] = 1
        display.set_pixel(1, 0, 9)
    if pin1.is_touched():
        pins[1] = 1
        display.set_pixel(2, 0, 9)
    if pin2.is_touched():
        pins[2] = 1
        display.set_pixel(3, 0, 9)
    burffer = str(pins) + "\n"
    uart.write(burffer)
    sleep(100)
    display.set_pixel(4, 4, 0)
    pins = [0, 0, 0]
    display.set_pixel(1, 0, 0)
    display.set_pixel(2, 0, 0)
    display.set_pixel(3, 0, 0)