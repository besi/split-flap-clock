![](assets/logo.png)

Split Flap driver board for four 28BYJ-48 stepper motors.


## Bill of materials

What is needed for one digit.

| Count | Item                 | Description                       |
|-------|----------------------|-----------------------------------|
| 1     | PCB v2.0             |                                   |
| 1     | Supporting Plate     | Same shape and holes like the PCB |
| 1     | Spacer 2mm           | Spacer for cogwheels              |
| 1     | Hall Sensor AH1815-W7| For the unpopulated PCBs only     |
| 1     | 10k Resistor 0306    | For the unpopulated PCBS          |
| 1     | Spool                | 3-D Print with M3 heat insert     |
| 1     | Spool lid            | 3-D Print                         |
| 1     | Cog Stepper          | 3-D Print / Laser cut             |
| 1     | Cog M3               | 3-D Print / Laser cut             |
| 1     | Cog M3 Nut           | 3-D Print / Laser cut             |
| 1     | Magnet 2x1mm         | For spool                         |
| 1     | Motor 28BYJ-48       | 5V Version                        |
| 1     | Motor gasket         | Laser cut                         |
| 12    | Flaps                | Laser cut Flaps                   |
| 1     | 3 Pos JST 2mm Socket | Hall Sensor Connection            |
| 1     | 3 Pos JST 2mm Cable  | Hall Sensor Connection            |
| 4     | M3 Nuts              | 2 Cogs, 2 Motor                   |
| 5     | M3x8mm Bolt          | 2 Cogs,2 Motor, Spindle,          |
| 3     | M3x5mm Bolt          | 3 Spindle                         |
| 4     | M3 Standoffs 50mm    | Male-Female 6mm thread            |
| 4     | M2.5 Screws          | For Standoffs                     |
| 1     | Washer 5mm 1mm thick | For Driver cogwheel               |
| 2     | Washer 3mm 1mm thick | For cogwheels                     |
| 1     | Zip tie for motor    |                                   |

The driving cog wheel is assembled as follows:

    M3x16 + 5 washers + m3-nut-cog + 3 washers

Please note that one assembled PCB can drive four digits. Those "passive" digits only need to have the hall sensor soldered onto it.

## Pinout

Motors: 

| Pins        | 1  | 2  | 3  | 4  | Hall  |
|-------------|----|----|----|----|-------|
| **Motor A** | 10 | 9  | 3  | 8  | 18 (7)|
| **Motor B** | 13 | 14 | 21 | 11 | 12    |
| **Motor C** | 40 | 39 | 38 | 6  | 47    |
| **Motor D** | 1  | 2  | 42 | 41 | 48    |

Other GPIOs

| Function       | Pin |
|----------------|-----|
| DCF-77         | 4   |
| SDA / Switch B | 16  |
| SCL / Switch A | 17  |
| Mode           | 0   |
| Neopixel       | 15  |
| Temperature    | 5   |

## The PCB

![](assets/v2-splitflap-pcb.png)


## Version 1.0

![](assets/v1-prototype.png)
![](assets/v1-splitflap-pcb.png)


## Credits

### Manufacturing

[PCBWay](https://pcbway.com/g/2jc702) kindly offered to sponsor the manufacturing and assembly of the second iteration of this pcb.

![PCBWay](assets/pcbway.png) 

### 3d models
- Credits for the [ESP32 Devkit 3d model](https://grabcad.com/library/esp32-devkitc-v4-1) by [Andrei Golyakov](https://grabcad.com/andrei.golyakov-1)
- Credits for the [SK6814mini 3d model](https://grabcad.com/library/sk6812-mini-sk6814-smd3535-1) by [Laur V](https://grabcad.com/laur.v-1)


### Markdown tables

The Markdown tables were generated using the fabulous tool called [tableconvert](https://tableconvert.com/markdown-generator).
