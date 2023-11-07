import wiringpi
from wiringpi import GPIO; wiringpi.wiringPiSetup()
import time

wiringpi.pinMode(8, GPIO.OUTPUT)
wiringpi.pinMode(11, GPIO.OUTPUT)
wiringpi.pinMode(12, GPIO.OUTPUT)
wiringpi.pinMode(14, GPIO.OUTPUT)


def move_back():
    wiringpi.digitalWrite(8, GPIO.HIGH)
    wiringpi.digitalWrite(11, GPIO.LOW)
    wiringpi.digitalWrite(12, GPIO.HIGH)
    wiringpi.digitalWrite(14, GPIO.LOW)


def move_forword():
    wiringpi.digitalWrite(8, GPIO.LOW)
    wiringpi.digitalWrite(11, GPIO.HIGH)
    wiringpi.digitalWrite(12, GPIO.LOW)
    wiringpi.digitalWrite(14, GPIO.HIGH)

def turn_left():
    wiringpi.digitalWrite(8, GPIO.HIGH)
    wiringpi.digitalWrite(11, GPIO.LOW)
    wiringpi.digitalWrite(12, GPIO.LOW)
    wiringpi.digitalWrite(14, GPIO.HIGH)

def turn_right():
    wiringpi.digitalWrite(8, GPIO.LOW)
    wiringpi.digitalWrite(11, GPIO.HIGH)
    wiringpi.digitalWrite(12, GPIO.HIGH)
    wiringpi.digitalWrite(14, GPIO.LOW)

def stop():
    wiringpi.digitalWrite(8, GPIO.LOW)
    wiringpi.digitalWrite(11, GPIO.LOW)
    wiringpi.digitalWrite(12, GPIO.LOW)
    wiringpi.digitalWrite(14, GPIO.LOW)

# move_forword()

# time.sleep(2)

# move_back()

# time.sleep(2)

# turn_left()

# time.sleep(2)

# turn_right()

# time.sleep(2)

# stop()