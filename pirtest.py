import RPi.GPIO as GPIO
import time
import os
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(11, GPIO.OUT)        #Input for Screen Power
#GPIO.setup(11, GPIO.IN)        #Input for Screen Power
while True:
    i=GPIO.input(7)
    if i==0:                 #When output from motion sensor is LOW
        print("Noone around",i)
        #GPIO.output(11, 0)    #Shutdown the display
        time.sleep(0.1)
    elif i==1:               #When output from motion sensor is HIGH
        print("Hey mate !",i)
        GPIO.output(11, 0)    #Power the display
        GPIO.output(11, 1)    #Power the display
        os.system("export DISPLAY=:0;mplayer ~/drop.avi -zoom -vf expand=656:512")
        time.sleep(5)
""" while True:
    i=GPIO.input(11)
    if i==0:                 #When output from remote is LOW
        print "The screen is off",i
        time.sleep(0.1)
    elif i==1:               #When output from remote is HIGH
        print "The screen is on",i
        time.sleep(0.1) """