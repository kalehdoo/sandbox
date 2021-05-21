from paho.mqtt import client as mqtt
from random import randrange, uniform
import time

def on_log(client, userdata, level, buf):
    print("Log: "+buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print('Connected OK')
        
    else:
        print("Bad Connection Return Code:" + str(rc))

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected Return Code:" + str(rc))


#free broker is available. or need to install your own broker
mqttBroker = "mqtt.eclipseprojects.io"


#creates a client with the name Temperature_Inside. has to be unique
mqttClient = mqtt.Client("Temperature_Inside")
mqttClient.connect(mqttBroker)

print("Connecting to Broker: "+mqttBroker)

mqttClient.on_log = on_log
mqttClient.on_connect = on_connect
mqttClient.on_disconnect = on_disconnect

mqttClient.loop_start()
while True:
    random_number = uniform(30.0,40.0)
    #CLINIC_1/PATIENT_1001 is the name of the topic
    mqttClient.publish("CLINIC_1/PATIENT_1001", random_number)
    print("Temperature: " + str(random_number))
    time.sleep(2)
mqttClient.loop_stop()
mqttClient.disconnect()