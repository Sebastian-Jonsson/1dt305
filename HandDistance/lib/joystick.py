import machine
from machine import ADC
import utime
import pycom

adc = machine.ADC()
midHigh = 1250
midLow = 800

def disco_Stick():
    xAxis = adc.channel(pin='P13')
    yAxis = adc.channel(pin='P14')
    xVal = xAxis()
    yVal = yAxis()

    if (xVal > midHigh or yVal > midHigh) or (xVal < midLow or yVal < midLow):
        xVal = xAxis()
        yVal = yAxis()
        xyVal = str(xVal) + ',' + str(yVal)
        #pybytes.send_signal(0, xyVal)
        return xyVal
    else:
        xVal = xAxis()
        yVal = yAxis()
        return ""
