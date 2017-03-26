


git clone https://github.com/adafruit/Adafruit_Python_DHT.git
sudo apt-get update
sudo apt-get install build-essential python-dev
cd Adafruit_Python_DHT/
sudo python setup.py install
sudo pip install paho-mqtt
sudo reboot


crontab -e

* * * * *   /usr/bin/python /home/pi/envmonitor/dht/read_dht.py