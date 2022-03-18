import utime
import pycom
import machine
from machine import Pin

# Credit to https://github.com/iot-lnu/applied-iot/blob/master/sensor-examples/HC-SR04%20-%20Ultrasonic%20Sensor/main.py
def distance_measure():
    # initialise Ultrasonic Sensor pins.
    echo = Pin('P20', mode=Pin.IN)
    trigger = Pin('P19', mode=Pin.OUT)
    trigger(0)

    # trigger pulse LOW for 2us (just in case).
    utime.sleep_us(2)
    # trigger HIGH for a 10us pulse.
    trigger(1)
    utime.sleep_us(10)
    trigger(0)

    # wait for the rising edge of the echo then start timer.
    while echo() == 0:
        pass
    start = utime.ticks_us()

    # wait for end of echo pulse then stop timer.
    while echo() == 1:
        pass
    finish = utime.ticks_us()

    # pause for 20ms to prevent overlapping echos.
    utime.sleep_ms(20)

    # calculate the distance by using time difference between start and stop.
    # speed of sound in this context being .034 divided by two for the distance to object detected.
    distance = ((utime.ticks_diff(start, finish)) * .034)/2

    return distance

# Runs distance_measure multiple times to get a more accurate measurement.
def average_distance():
        # declares the variables to a standard value, pre-measurement.
        average_distance = 0
        average_list = []

        # loops through the distance_measure function to gather ten values in an array.
        for i in range(10):
            average_list.append(distance_measure())

        # calculates the average value based on the values in the average_list.
        average_distance = (sum(average_list)/len(average_list))

        # returns the average distance calculated for usage.
        return average_distance
