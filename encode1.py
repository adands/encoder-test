import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)

encoder_pin_a = 17
encoder_pin_b = 18

gpio.setup(encoder_pin_a,gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(encoder_pin_b,gpio.IN, pull_up_down = gpio.PUD_DOWN)

def encoder_callback(channel):
    time.sleep(1)
    if gpio.input(encoder_pin_a):
        print("A:high")
    else:
        print("A:low")
    if gpio.input(encoder_pin_b):
        print("B:high")
    else:
        print("B:low")

gpio.add_event_detect(encoder_pin_a, gpio.BOTH, callback=encoder_callback)
gpio.add_event_detect(encoder_pin_b, gpio.BOTH, callback=encoder_callback)

try:
    while True:
        pass
except KeyboardInterrupt:
    gpio.cleanup()