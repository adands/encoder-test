import RPi.GPIO as GPIO
import time

clk = 17
dt = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(dt,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
counter =0
rotate_counter =0

def encoder_callback(channel):
    global rotate_counter , counter
    counter +=1
    if counter >= ppr:
        rotate_counter +=1
        counter =0
    print(rotate_counter)

GPIO.add_event_detect(clk, GPIO.BOTH, callback=encoder_callback)
# GPIO.add_event_detect(dt, GPIO.BOTH, callback=encoder_callback)

angle = 360

pp =12000
ppr=pp/angle

try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()