#!/bin/bash

SENSORS=(dht22 bmp180)

DIR="$( cd -P "$( dirname "$0" )" && pwd )"

for sensor in "${SENSORS[@]}"
do
    /usr/bin/python $DIR/{$sensor}/read_sensor.py &
done

