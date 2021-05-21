from paho.mqtt import client as mqtt
from random import randrange, uniform
import time

mqttBroker = "mqtt.eclipseprojects.io"
#creates a client with the name Temperature_Outside
mqttClient = mqtt.Client("Temperature_Outside")
mqttClient.connect(mqttBroker)

while True:
    random_number = randrange(50,60)
    #CLINIC_1/PATIENT_1001 is the name of the topic
    mqttClient.publish("CLINIC_1/PATIENT_1001", random_number)
    print("BloodPressure: " + str(random_number))
    time.sleep(2)