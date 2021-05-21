import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))

mqttBroker = "mqtt.eclipseprojects.io"
mqttClient = mqtt.Client("Smartphone")
mqttClient.connect(mqttBroker)

mqttClient.loop_start()
while True:    
    mqttClient.subscribe("CLINIC_1/PATIENT_1001")
    mqttClient.on_message = on_message
    time.sleep(2)
mqttClient.loop_stop()