import paho.mqtt.publish as publish
import json
import platform
import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()
pressure = sensor.read_pressure()

node = platform.node()
publish.single("flat/env", json.dumps({"type":"pressure","value": pressure, "node": node}, sort_keys=True), hostname="flatmaster")