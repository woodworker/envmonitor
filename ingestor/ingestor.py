#!/usr/bin/env python
import paho.mqtt.client as mqtt
import json
import time
import requests

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("flat/env")

def on_message(client, userdata, msg):
    data = json.loads(str(msg.payload))
    timestamp = int(time.time())
    type = data["type"]
    value = data["value"]
    node = data["node"]
    # adding so many zeros after 3rd parameter because influxdb needs nanosecond timestamps
    send = '{0},node={1} value={2} {3}000000000'.format(type, node, value, timestamp)
    requests.post('http://localhost:8086/write?db=environment', data = send)
    print send

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("localhost", 1883, 60)

client.loop_forever()