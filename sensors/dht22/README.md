# Temperature / Humidity (RaspberryPi+DHT22)

![DHT22 Sensor](DHT22-PinOut.png)

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

## Connect sensor

Remember to solder a 10k Resistor between sensor pin 1 (VCC) and pin 2 (DATA) 

| Sensor pin | RaspberryPi Pin |
| ---------- | --------------- |
| Data       | PIN7/GPIO4      |
| VCC        | PIN1/3v3        |
| GND        | PIN9/GND        |
