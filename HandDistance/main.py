import buttons
import utime
from mqtt import MQTTClient
import machine

# Credit to https://docs.pycom.io/tutorials/networkprotocols/mqtt/ #app for the MQTT connection.
# sets the callback message based on topic.
def sub_cb(topic, msg):
   print(msg)

# sets which client on adafruit should receive the sensordata.
client = MQTTClient("placeholder", "io.adafruit.com",user="placeholder", password="placeholder", port=1883)
client.set_callback(sub_cb)
client.connect()
client.subscribe(topic="placeholder")

while True:
    # if the value from a button push is less than 1, we will not send any blank data to io.adafruit.
    if len(buttons.shiny_Buttons()) > 2:
        print (buttons.shiny_Buttons())

        # determines which topic on the users adafruit account receives the data and which data is sent.
        client.publish(topic="placeholder", msg=buttons.shiny_Buttons())
        client.check_msg()
        # sleeps for a minimal time before anything else can happen, avoiding overlaps.
        utime.sleep_ms(200)
    else:
        pass
