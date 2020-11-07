# FlexipodHardware

## 3D rendering and dimension of Flexipod
<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/flexipod.png" width="60%" height="60%">
CAD model for the Flexipod
<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/flexipod.jpg" width="40%" height="40%">
Flexipod stand on sand

## Mechiancl parts
<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/flexipod_printed_parts_DSC1694.png" width="40%" height="40%">
All the printed parts are printed by a FDM 3D printer(Troodon Core-XY printer, VIVEDINO) with a standard 0.4 mm nozzle at 0.2 mm layer height. For soft print, skins are only printed at mating surfaces, since the outer skins of the printed parts will greatly reduce the flexibility.

1. leg: print with 16% infill density(Gyroid pattern) and 80% flow using flexible TPU (Cheetah flexible filament, Ninjatek).
<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/leg.png" width="40%" height="40%">

2. leg adaptor: rigid filament (PolyMax™ PC, Playmaker)
<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/leg_coupler.png" width="40%" height="40%">

3. motor mount outer part: print with 20% infill density(Gyroid pattern) and 90% flow using flexible TPU (Cheetah flexible filament, Ninjatek).
<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/motor_mount_out.png" width="40%" height="40%">

4. [bearing: ](https://www.amazon.com/6806-Ceramic-Cartridge-Bearing-30x42x7mm/dp/B01MU6Z46A/ref=sr_1_3?dchild=1&keywords=6806-2RS&qid=1604034211&sr=8-3)
<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/Bearing.jpg" width="20%" height="20%">

5. motor mount inner part: print with 20% infill density(Gyroid pattern) and 90% flow using flexible TPU (Cheetah flexible filament, Ninjatek).
<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/motor_mount_in.png" width="40%" height="40%">

6. motor shell: rigid filament (PolyMax™ PC, Playmaker)
<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/motor_shell.png" width="40%" height="40%">

7. body cover: print with 20% infill density(Gyroid pattern) and 90% flow using flexible TPU (Cheetah flexible filament, Ninjatek).
<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/body_cover.png" width="40%" height="40%">

8. upper body: print with 20% infill density(Gyroid pattern) and 90% flow using flexible TPU (Cheetah flexible filament, Ninjatek).
<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/upper_body.png" width="40%" height="40%">

9. lower body: print with 20% infill density(Gyroid pattern) and 90% flow using flexible TPU (Cheetah flexible filament, Ninjatek).
<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/lower_body.png" width="40%" height="40%">

## Electrical parts
electrical system of the Flexipod  

<img src="https://github.com/boxiXia/FlexipodHardware/blob/master/images/schematics.png" width="80%" height="80%">

1. [Raspberry Pi 4B](https://www.amazon.com/Raspberry-Model-2019-Quad-Bluetooth/dp/B07TC2BK1X/ref=sr_1_5?crid=2TAFP75A787CM&dchild=1&keywords=raspberry+pi+4&sprefix=raspberr%2Caps%2C187&sr=8-5)

2. [5V Voltage Regulator](https://www.pololu.com/product/4091)

3. [5S Battery](https://www.amazon.com/Ovonic-1300mAh-Battery-Professional-Competitions/dp/B07JXZCHWM/ref=sr_1_4?dchild=1&keywords=Ovonic+5S+battery&qid=1598477273&sr=8-4)

4. [CAN Transceivez](https://www.amazon.com/dp/B07V5LGBC8/?coliid=I3FNNXJG3YL6HU&colid=34AXXXH87PSUB&psc=1&ref_=lv_ov_lig_dp_it)

5. [Teensy 4.0](https://www.amazon.com/Teensy-4-0-With-Pins/dp/B08259KDHY/ref=sr_1_3?crid=29SHX3YSS7XUC&dchild=1&keywords=teensy+4.0&sprefix=teensy+%2Caps%2C167&sr=8-3)

6. [IMU](https://www.adafruit.com/product/4517)

7. [Voltage Sensor](https://www.adafruit.com/product/4226)

8. [ESC](https://store.dji.com/product/rm-c620-brushless-dc-motor-speed-controller?set_country=US&gclid=EAIaIQobChMI2s7r6Oi56wIVDsDICh1QPgAQEAYYASABEgI1tvD_BwE)

9. [Motor](https://store.dji.com/product/rm-m3508-p19-brushless-dc-gear-motor?set_country=US&gclid=EAIaIQobChMI_8WYiem56wIVluSzCh2VIABiEAYYASABEgJY_vD_BwE)

10. [Custom PCB](https://github.com/boxiXia/FlexipodHardware/tree/master/mechanical_model/PCB/Gerber%20%26%20drill)
