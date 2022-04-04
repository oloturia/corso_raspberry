#!/usr/bin/env python3

import paho.mqtt.client as mqtt
mqtt_broker = "localhost"

def on_connect(client, userdate, flags, rc):
	print("Connected, code:"+str(rc))
	client.subscribe("test/topic")
	
def on_message(client,userdata,msg):
	print(msg.topic+" "+str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.username_pw_set("user","password")
client.connect(mqtt_broker,1883)

client.loop_forever()
