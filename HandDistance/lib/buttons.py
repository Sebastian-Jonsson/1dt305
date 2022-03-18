from machine import Pin
import ultrasonicDistance
import utime
import pycom

def shiny_Buttons():
    # initialise Button pins.
    blue_p_in = Pin('P16', mode = Pin.IN)

    # sets the color of the button to the correct pin for sensing push.
    blue = blue_p_in()

    # 0 means that a button is pushed, 1 means that it is not.
    if blue == 0:
        bluePress = str(ultrasonicDistance.average_distance())
        # returning the value from the ultrasonic distance measurement as a string.
        return bluePress
    else:
        # else we return a string which is shorter than two.
        # this is checked in main.py before sending it via MQTT to Adafruit.io.
        return ""
