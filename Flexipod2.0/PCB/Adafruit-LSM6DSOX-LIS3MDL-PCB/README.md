## Adafruit LSM6DSOX + LIS3MDL Precision 9-DoF IMU PCBs

<a href="http://www.adafruit.com/products/4517"><img src="assets/4517.jpg?raw=true" width="500px"><br/>
<a href="http://www.adafruit.com/products/4565"><img src="assets/4565.jpg?raw=true" width="500px"><br/>
Click here to purchase one from the Adafruit shop</a>

PCB files for the Adafruit LSM6DSOX + LIS3MDL Precision 9-DoF IMU breakout and FeatherWing.

Format is EagleCAD schematic and board layout
* https://www.adafruit.com/product/4517

### Description

Add high quality motion, direction and orientation sensing to your Arduino project with this all-in-one 9 Degree of Freedom (9-DoF) sensor with sensors from ST. This little breakout contains two chips that sit side-by-side to provide 9 degrees of full-motion data.

The board includes an LSM6DSOX, a 6-DoF IMU accelerometer + gyro. The 3-axis accelerometer can tell you which direction is down towards the Earth (by measuring gravity) or how fast the board is accelerating in 3D space. The 3-axis gyroscope can measure spin and twist. This new sensor from ST has very low gyro zero rate and noise, compared to the MPU6050 or even LSM6DS33 so it's excellent for orientation fusion usage: you'll get less drift and faster responses.

The LSM6DSOX has flexible data rates and ranges. For the accelerometer: ±2/±4/±8/±16 g at 1.6 Hz to 6.7KHz update rate. For the gyroscope: ±125/±250/±500/±1000/±2000 dps at 12.5 Hz to 6.7 KHz. There's also some nice extras, such as built in tap detection, activity detection, pedometer/step counter and a programmable finite state machine / machine learning core that can perform some basic gesture recognition.

It also includes a LIS3MDL 3-axis magnetometer that can sense where the strongest magnetic force is coming from, generally used to detect magnetic north. The three triple-axis sensors add up to 9 degrees of freedom, by combining this data you can orient the board. Check out our guide on how to do that!

To make getting started fast and easy, we placed the sensors on a compact breakout board with voltage regulation and level-shifted inputs. That way you can use them with 3V or 5V power/logic devices without worry. To make usage simple, we expose only the I2C interface and some interrupt pins from each chip. The breakout comes fully assembled and tested, with some extra header so you can use it on a breadboard. Four mounting holes make for a secure connection.

Additionally, since it speaks I2C you can easily connect it up with two wires (plus power and ground!).  We've even included SparkFun qwiic compatible STEMMA QT connectors for the I2C bus so you don't even need to solder! Just wire up to your favorite micro like the STM32F405 Feather with a plug-and-play cable to get 9 DoF data ASAP. You can change the I2C addresses on the back using the solder jumpers, to have two of these sensor boards on one bus.

We also wrote libraries to help you get these sensors integrated with your Arduino/C++. This library covers the accel/gyro and this library is for the magnetometer. For advanced Arduino usage, ST has their own fully-featured library that includes extras such as FIFO management and tap detection for the LSM6DSOX and also for the LIS3MDL magnetometer.

### License

Adafruit invests time and resources providing this open source design, please support Adafruit and open-source hardware by purchasing products from [Adafruit](https://www.adafruit.com)!

Designed by Limor Fried/Ladyada for Adafruit Industries.

Creative Commons Attribution/Share-Alike, all text above must be included in any redistribution.
See license.txt for additional details.
