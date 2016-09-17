# RaspberryPi3_stepper_shield_converter
###This repository contains schematics to build a RaspBerryPi3 / Arduino_steppr_shield  converter.


***

This project is under GPL V3 license (see the LICENSE file for more informations)

***

**Shematics are fzz file that you can open with [Fritzing](http://fritzing.org/home/)** 

>"Fritzing is an open-source hardware initiative that makes electronics accessible as a creative material for anyone" 


This RaspBerryPi3 shield was built to use a ready-to-use Arduino shield.

You can find it at this [link](https://github.com/PeriniMatteo/single_stepper_Arduino_Shield)
 
You need this shield to manage a Pololu A4988 stepper driver that normally works with 5V where RaspBerryPi3 has 3,3V PinOut.

**Technical notes:**

* **All the used resistors are 2.2KOhm**
* **All the used N-Ch Mosfet are BF170 or the equivalent 2N7000** (see dasheets attached) 
