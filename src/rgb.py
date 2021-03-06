#!/usr/bin/env python

### Class to control the RGB LED Indicator ###

import Adafruit_BBIO.GPIO as GPIO
import time

class RGBController(object):
    def __init__(self, red_pin = "P8_10", green_pin = "P8_12", blue_pin =  "P8_14"):

        self.red_pin = red_pin
        self.green_pin = green_pin
        self.blue_pin = blue_pin
        self.blink_time = 0.5

        GPIO.setup(self.red_pin, GPIO.OUT)
        GPIO.output(self.red_pin, GPIO.LOW)

        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.output(self.green_pin, GPIO.LOW)

        GPIO.setup(self.blue_pin, GPIO.OUT)
        GPIO.output(self.blue_pin, GPIO.LOW)

    def turnOn(self, color):
        if color == "red":
            GPIO.output(self.red_pin, GPIO.HIGH)
        elif color == "green":
            GPIO.output(self.green_pin, GPIO.HIGH)
        elif color == "blue":
            GPIO.output(self.blue_pin, GPIO.HIGH)
        elif color == "yellow":
            GPIO.output(self.red_pin, GPIO.HIGH)
            GPIO.output(self.green_pin, GPIO.HIGH)
        elif color == "purple":
            GPIO.output(self.red_pin, GPIO.HIGH)
            GPIO.output(self.blue_pin, GPIO.HIGH)
        elif color == "teal":
            GPIO.output(self.green_pin, GPIO.HIGH)
            GPIO.output(self.blue_pin, GPIO.HIGH)
        else:
            pass

    def turnOff(self, color):
        if color == "red":
            GPIO.output(self.red_pin, GPIO.LOW)
        elif color == "green":
            GPIO.output(self.green_pin, GPIO.LOW)
        elif color == "blue":
            GPIO.output(self.blue_pin, GPIO.LOW)
        elif color == "yellow":
            GPIO.output(self.red_pin, GPIO.LOW)
            GPIO.output(self.green_pin, GPIO.LOW)
        elif color == "purple":
            GPIO.output(self.red_pin, GPIO.LOW)
            GPIO.output(self.blue_pin, GPIO.LOW)
        elif color == "teal":
            GPIO.output(self.green_pin, GPIO.LOW)
            GPIO.output(self.blue_pin, GPIO.LOW)
        else:
            pass

    def blink(self, color, iterations=5):
        for i in xrange(0, iterations):
            if color == "red":
                self.turnOn("red")
                time.sleep(self.blink_time)
                self.turnOff("red")
                time.sleep(self.blink_time)
            elif color == "green":
                self.turnOn("green")
                time.sleep(self.blink_time)
                self.turnOff("green")
                time.sleep(self.blink_time)
            elif color == "blue":
                self.turnOn("blue")
                time.sleep(self.blink_time)
                self.turnOff("blue")
                time.sleep(self.blink_time)
            elif color == "yellow":
                self.turnOn("yellow")
                time.sleep(self.blink_time)
                self.turnOff("yellow")
                time.sleep(self.blink_time)
            elif color == "purple":
                self.turnOn("purple")
                time.sleep(self.blink_time)
                self.turnOff("purple")
                time.sleep(self.blink_time)
            elif color == "teal":
                self.turnOn("teal")
                time.sleep(self.blink_time)
                self.turnOff("teal")
                time.sleep(self.blink_time)
            else:
                pass

    def allOff(self):
        GPIO.output(self.red_pin, GPIO.LOW)
        GPIO.output(self.green_pin, GPIO.LOW)
        GPIO.output(self.blue_pin, GPIO.LOW)
