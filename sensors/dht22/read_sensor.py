import Adafruit_DHT as dht
import paho.mqtt.publish as publish
import json
import platform

h,t = dht.read_retry(dht.DHT22, 4)
node = platform.node()

publish.single("flat/env", json.dumps({"type":"temperature","value": t, "node": node}, sort_keys=True), hostname="flatmaster")
publish.single("flat/env", json.dumps({"type":"humidity","value": h, "node": node}, sort_keys=True), hostname="flatmaster")