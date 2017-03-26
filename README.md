# Home Environment Monitor

This is a simple home monitoring solution based on, at least one, raspberry pi.
Data transfer is done via mqtt (mosquitto), for storage is influxdb used,
and displayed via a Grafana frontend. 

At the moment this is only based on Python scripts on RaspberryPi nodes.
I want to add nodes based on ESP8266 and/or ESP32.
Maybe also a NRF24 based sensor network.

Packet format:
```
{"type":"<meassurement type>","value": <meassured value>, "node": <node name>}
```


# TODO
* simple installer script

## ESP8266 Node
* create ESP8266 Node with DHT22

## Raspberry Pi Node
* config file for available sensors
* auto discovery of mqtt node?
* create single crontab based on sensor config

## Ingestor Node
* make ingestor a real demonized server instead of a python script in a screen

## Sensors
* Simple LDR based light sensor
  * https://www.aliexpress.com/item/20PCS-x-5528-Light-Dependent-Resistor-LDR-5MM-Photoresistor-wholesale-and-retail-Photoconductive-resistance-for-arduino/32623615207.html
* IR movment sensor
  * https://www.aliexpress.com/item/Free-Shipping-HC-SR501-Adjust-Infrared-IR-Pyroelectric-Infrared-PIR-module-Motion-Sensor-Detector-Module-We/32519303005.html
* clamp ammeter
  * https://www.aliexpress.com/item/5A-SCT-013-005-Non-invasive-AC-current-sensor-Split-Core-Current-Transformer/32637361693.html

# Installation

Connect to your pi and git clone this repo
```
git clone https://github.com/woodworker/envmonitor.git
```

## Ingestor node

See: http://engineer.john-whittington.co.uk/2016/11/raspberry-pi-data-logger-influxdb-grafana/

Install influxdb and grafana
```
sudo apt-get update
sudo apt-get upgrade
wget http://ftp.us.debian.org/debian/pool/main/i/influxdb/influxdb_1.1.1+dfsg1-4_armhf.deb
sudo dpkg -i influxdb_1.1.1+dfsg1-4_armhf.deb
wget http://ftp.us.debian.org/debian/pool/main/g/grafana/grafana-data_2.6.0+dfsg-3_all.deb # grafana data is a dependancy for grafana
sudo dpkg -i grafana-data_2.6.0+dfsg-3_all.deb
sudo apt-get install -f
wget http://ftp.us.debian.org/debian/pool/main/g/grafana/grafana_2.6.0+dfsg-3_armhf.deb
sudo dpkg -i grafana_2.6.0+dfsg-3_armhf.deb
sudo apt-get install -f
```

Enable grafana by default
```
sudo systemctl enable grafana-server
sudo systemctl start grafana-server
```

Install the mqtt server
```
sudo apt-get install -y mosquitto mosquitto-clients
```

add `/home/pi/envmonitor/ingestor/ingestor.sh` to `/etc/rc.local`

## Sensor node

### Temperature / Humidity (RaspberryPi+DHT22)

https://www.aliexpress.com/item/Free-shipping-DHT22-digital-temperature-and-humidity-sensor-Temperature-and-humidity-module-AM2302-replace-SHT11-SHT15/632552670.html

Install software
```
sudo apt-get update
sudo apt-get install build-essential python-dev
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT/
sudo python setup.py install
sudo pip install paho-mqtt
sudo reboot
```

Install crontab
```
crontab -e
* * * * *   /usr/bin/python /home/pi/envmonitor/dht/read_dht.py
```

### Atmospheric pressure (RaspberryPi+BMP180)

https://www.aliexpress.com/item/1PCS-BMP280-Replace-BMP180-Digital-Barometric-Pressure-Sensor-Module-For-Arduino/32651870833.html

*Note: The value send by this Sensor is actual in Pascal so do display hPa you need to divide by 100 to get actual hPa values that are used everywhere.*

Install software
```
sudo apt-get update
sudo apt-get install build-essential python-dev
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP/
sudo python setup.py install
sudo pip install paho-mqtt
sudo reboot
```

Install crontab
```
crontab -e
* * * * *   /usr/bin/python /home/pi/envmonitor/bmp180/read_bmp.py
```