## BrickPi3 Library
This is a wrapper for the brickpi3 library. Designed to simplify the use of Motors and Sensors.

## Motivation
Created this project to help me manage sensors and motors easier for a class I was taking using BrickPi3's and Lego Mindstorm motors and sensors.

## Code style
[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/kengz/python)
 

## Code Example
```python
import BrickPi3Lib

left_motor = Motor("ma")
right_motor = Motor("mb")

gyro_sensor = Sensor("S1", "gyro")
ultrasonic_sensor = Sensor("S2", "ultrasonic")
ir_sensor = Sensor("S3", "ir")
ir_proximity_sensor = Sensor("S4", "irp")
color_sensor = Sensor("S4", "color")

left_motor.setSpeed(50)
right_motor.setSpeed(50)

running = True
while running:
  print(gyro_sensor.getReading())
  
```

## Credits
https://github.com/DexterInd/BrickPi3

## License
MIT © [Basketcaisse21]()
