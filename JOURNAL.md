---
title: "The Zero Pi"
author: "AVSC"
description: "Offline GPS Navigation & Logger using RPI"
created_at: "2024-05-25"
---
<h1>May 27 : Planning</h1>

(A rugged, offline GPS device for hikers, bikers, and adventurers.)

So the thing was I needed a GPS logger for my cycling expeditions (I go like 50kms) and I didn't have a personal phone...so I decided to build the PiTracker

*Sat down and decided on the key features:*

Real-time location from USB GPS module.

Offline maps displayed on the touchscreen.

Log and export routes as GPX files.

Fully portable with battery power.

*Also first list of components:*

USB GPS module (U-blox Neo-6M).

MicroSD card for storing map tiles.

RPI 5 (4gb) / RPI 4 (4gb)

3.5in TFT Touchscreen for RPI

**Time Spent ~ 2hrs** 

## May 26: Modeled the First PiTracker Enclosure

Finished the first version of the 3D enclosure for the PiTracker today!

Designed it in *TinkerCAD*(lol), and exported the STL (attached below). The enclosure is made to fit the Raspberry Pi 3B+ along with the 3.5" TFT screen on top.

###  Design Highlights:
- Cutouts for USB, HDMI, audio jack, and SD card  
- Slots for airflow (still might need more)  
- Mounting space for GPS module and battery (will do that next) 
- Simple slide or screw-together design (haven’t finalized yet)

**3D Model preview**

<img width="463" alt="image" src="https://github.com/user-attachments/assets/0910d30a-83c3-4fb1-a8bc-5f29a89ad79d" />

**Attached:**  
[`rpi 3b+ case.stl`](./rpi%203b%2B%20case.stl)

**Next up:**  
Modify to fit extra parts and airflow — might tweak the tolerances and screen angle after that.

Super hyped to see it come together physically (virtually) soon!

**Time Spent ~ 2.5hrs** 


## May 28: Wiring Diagram in Fritzing 

*Session 2*

Used Fritzing today to map out all the wiring for the PiTracker. Super helpful to have everything visual before starting to connect real hardware.

**Wiring (will add Fritzig or smthing later)**:
- Power:

Raspberry Pi powered via micro USB

TFT and GPS powered from Pi's 5V and GND

- 3.5" SPI TFT Display (Waveshare):

MOSI → GPIO10 (Physical Pin 19)

MISO → GPIO9 (Pin 21) (not always used for display only)

SCLK → GPIO11 (Pin 23)

CS → Any free GPIO (e.g. GPIO8, Pin 24)

DC (D/C) → Any GPIO (e.g. GPIO25, Pin 22)

RESET → Any GPIO (e.g. GPIO27, Pin 13)

VCC → 5V (Pin 2 or 4)

GND → GND (Pin 6 or any GND)

- NEO-6M GPS Module:

VCC → 5V (Pin 2 or 4)

GND → GND (Pin 6 or any GND)

TX → GPIO15 (UART RX, Pin 10)

RX → GPIO14 (UART TX, Pin 8)

**Next step:** Fritziggg!.

**Time Spent ~ 1.5hrs** 

 ## May 27: Finalized the PiTracker Enclosure for Pi 4B**
  
**Session 1** 

Big session today — I scrapped the original Pi 3B+ design and rebuilt the entire enclosure from scratch to support the **Raspberry Pi 4B**. 

The new layout took a while to get right, but I’m finally happy with the design!

### Final Design Features:
- Custom fit for the **Pi 4B**, accounting for changes in port positions (USB-C, dual micro HDMI, etc.)
- Adjusted dimensions and internal supports to fit the new board layout
- Cutouts for:
  - USB-C power
  - Dual micro HDMI
  - Audio jack
  - USB ports + Ethernet
  - microSD card
- Top shell redesigned to hold the **3.5" TFT screen** securely and flush
- Side vent slots for airflow (might add fan mount in v2)
- GPS module mount added inside with wire clearance
- Snap-fit design for flexibility during assembly
- Routed space internally for jumper wire clearance and powerbank mount

  **3D Model preview**
![image](https://github.com/user-attachments/assets/8bcbb95b-25e6-4734-827f-968d2745546c)

**Attached**
[https://csg.tinkercad.com/downloadExport?id=68dd55a4-21b2-4f8c-a2d9-896e78c4fcb8.stl&fileName=rpi%204b%20case.stl](url)

### Challenges:
- The Pi 4B’s dual HDMI and USB-C port placement forced a full layout rethink
- Making sure the screen didn’t block access to ports or GPIO pins took multiple test alignments
- Had to recheck all mounting holes and tolerances — this version should be **print-ready**
 
This should be the **final enclosure v1** unless the print throws surprises.

**Time Spent ~ 4 hrs** 


