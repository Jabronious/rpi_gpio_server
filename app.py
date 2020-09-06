from flask import Flask
app = Flask(__name__)

import time
import os
import sys

import RPi.GPIO as GPIO
from gpiozero import Button, LED

# # LED strip configuration:
# LED_COUNT = 43        # Number of LED pixels.
# LED_PIN = 12          # GPIO pin connected to the pixels (18 uses PWM!).
# # LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
# LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
# LED_DMA = 10          # DMA channel to use for generating signal (try 10)
# LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
# LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
# LED_CHANNEL = 0      # set to '1' for GPIOs 13, 19, 41, 45 or 53

button = Button(25, pull_up=False)
playing_led = LED(18)
activated_led = LED(17)
input_channel_list = [25]
output_channel_list = [18]

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/strip')
def strip_on():
	activated_led.on()
	playing_led.on()
	time.sleep(1)
	playing_led.off()
	activated_led.off()
	return 'Strip On'


#########################
#						#
#						#
#		Private			#
#						#
#						#
#########################
# def rainbowCycle(strip, wait_ms=20, iterations=5):
#     """Draw rainbow that uniformly distributes itself across all pixels."""
#     for j in range(256 * iterations):
#         for i in range(strip.numPixels()):
#             strip.setPixelColor(i, wheel(
#                 (int(i * 256 / strip.numPixels()) + j) & 255))
#         strip.show()
#         time.sleep(wait_ms / 1000.0)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')