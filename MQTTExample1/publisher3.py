from paho.mqtt import client as mqtt
from random import randrange, uniform
import time
import json
from datetime import datetime as dt

def on_log(client, userdata, level, buf):
    print("Log: "+buf)

def on_connect(client, userdata, flags, rc):
    if rc==0:
        print('Connected OK')
        
    else:
        print("Bad Connection Return Code:" + str(rc))

def on_disconnect(client, userdata, flags, rc=0):
    print("Disconnected Return Code:" + str(rc))

def on_message(client, userdata, message):
    print(str(message.payload.decode("utf-8")))



mqttBroker = "08fc75118b904d848ec85c81215fec78.s1.eu.hivemq.cloud"
mqttBroker_port = 8883

#mqttBroker = "mqtt.eclipseprojects.io"
#creates a client with the name Temperature_Outside
#let's say a unique channel for a unique sensor device publishing data
mqttClient = mqtt.Client("D1001_Publisher")
mqttClient.on_log = on_log
mqttClient.on_connect = on_connect
mqttClient.on_disconnect = on_disconnect

# enable TLS
mqttClient.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)

# set username and password
mqttClient.username_pw_set("msrbroker", "Msr@Broker@1313")


def get_device_data():    
    return {
        "device_id": "D1001",
        "obs_name": "high blood pressure", 
        "obs_value": randrange(40, 60),
        "obs_timestamp": dt.now()
    }


mqttClient.connect(mqttBroker, mqttBroker_port)
print("Connecting to Broker: "+mqttBroker)
mqttClient.loop_start()
while True:
    high_bp = randrange(80,130)
    low_bp = randrange(50,60)
    json_payload = json.dumps(get_device_data(), default=str)    
    mqttClient.publish("P1001/D1001", json_payload)
    print("json_payload: " + str(json_payload))
    time.sleep(2)
mqttClient.loop_stop()
mqttClient.disconnect()
print("MQTT Client disconnected. exit now.")
