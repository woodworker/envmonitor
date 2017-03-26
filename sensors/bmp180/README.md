# Atmospheric pressure (RaspberryPi+BMP180)

https://www.aliexpress.com/item/1PCS-BMP280-Replace-BMP180-Digital-Barometric-Pressure-Sensor-Module-For-Arduino/32651870833.html

*Note: The value send by this Sensor is actual in Pascal so do display hPa you need to divide by 100 to get actual hPa values that are used everywhere.*

## Install software
```
sudo apt-get update
sudo apt-get install build-essential python-dev
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP/
sudo python setup.py install
sudo pip install paho-mqtt
sudo reboot
```

## Connect sensor

| Sensor pin | RaspberryPi Pin |
| ---------- | --------------- |
| SDA        | PIN2/GPIO2/SDA  |
| SCL        | PIN5/GPIO3/SCL  |
| VCC        | PIN1/3v3        |
| GND        | PIN9/GND        |
