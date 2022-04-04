#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time

mqttBroker = "localhost"
client = mqtt.Client()
#client.username_pw_set("user","password")
client.connect(mqttBroker,1883)

counter = 0

while True:
		client.publish("test/topic",str(counter))
		print("sent "+str(counter))
		time.sleep(1)
		counter +=1
