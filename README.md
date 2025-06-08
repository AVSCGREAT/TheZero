*One thing to note - I have to create a PCB for 5V 3A Buck Converter for the RPi so yeah that's the last thing I'll do. (: Its optional but I plan to do it just for the expirience [See Journal bottom note]*

---
# The Zero PiTracker
---

# PiTracker — Offline GPS Navigation & Logger

![92cb42b8-32b3-486b-885b-21562abaaab7](https://github.com/user-attachments/assets/11650be9-71b7-41f9-9214-9fffb1c25df0)
*Portable GPS tracker with offline map display, route logging, and touchscreen UI.*

---

## Overview

PiTracker is a portable GPS navigation and logging device built on the Raspberry Pi 4. It combines a Neo-6M GPS module, a 3.5" TFT touchscreen, and a power bank to provide real-time offline navigation and route tracking. The whole system fits neatly inside a custom 3D-printed enclosure, making it ideal for hiking, biking, or outdoor adventures where internet is unavailable.

![0](https://github.com/user-attachments/assets/8a0d5888-3d48-40b7-9e9b-2edd6770722a)

**V2 --->**

<img width="519" alt="image" src="https://github.com/user-attachments/assets/0b8dcf89-b5a9-4b8a-8886-8a651e727060" />
[https://www.tinkercad.com/things/7ml9naQlg1D-rpi-4b-case?sharecode=82QmYhvzEoeTG61scX8_8p--__eQaEcsFCr23i5QqRg](url)

---

## Features

* Real-time GPS location tracking using Neo-6M GPS module
* Offline map display using OpenStreetMap (OSM) tiles on 3.5" TFT touchscreen
* Route tracking and logging to GPX files for later analysis
* Portable and battery-powered with a standard USB power bank
* Compact, durable 3D-printed case with custom mounting for all components
* Simple touchscreen interface to start/stop logging, zoom maps, and export data

---

## Hardware Components

| Part                 | Description                                      | Notes                             |
| -------------------- | ------------------------------------------------ | --------------------------------- |
| Raspberry Pi 4       | Main computing unit                              | 2GB or 4GB recommended            |
| Neo-6M GPS Module    | USB or UART GPS receiver                         | Provides accurate GPS coordinates |
| 3.5" TFT Touchscreen | SPI interface with touch control (e.g., XPT2046) | For displaying maps and UI        |
| USB Power Bank       | 5V 2A output for portable power                  | Powers the entire device          |
| MicroSD Card         | 32GB or higher for OS and map storage            | Class 10 or better recommended    |
| 3D-Printed Enclosure | Custom-designed case for all components          | Protects and houses the device    |
| Miscellaneous        | Jumper wires, connectors, screws, etc.           | For assembly and wiring           |

---

## Software Requirements

* Raspberry Pi OS (64-bit recommended)
* Python 3.7+
* GPSD and gpsd-clients for GPS data handling
* Python libraries:

  * `gpsd-py3` (to interface with GPSD)
  * `Pillow` (for image handling)
  * `pygame` or `tkinter` (for GUI and touchscreen input)
  * `folium` or custom map rendering tools
* Offline OpenStreetMap tiles stored locally

---

## Installation and Setup

### 1. Prepare the Raspberry Pi

* Flash Raspberry Pi OS onto your MicroSD card (use Raspberry Pi Imager)
* Boot and complete basic setup
* Enable SPI and I2C interfaces:

  ```bash
  sudo raspi-config
  ```

  Navigate to **Interface Options** → **SPI** → Enable
  Also enable **Serial Port** if using UART GPS

### 2. Install GPSD and Required Packages

```bash
sudo apt update
sudo apt install gpsd gpsd-clients python3-pip
pip3 install gpsd-py3 pillow pygame
```

### 3. Connect and Test the GPS Module

* Plug in your Neo-6M GPS (USB or UART)
* Find the device name (e.g., `/dev/ttyUSB0` or `/dev/serial0`)
* Start GPSD manually for testing:

```bash
sudo systemctl stop gpsd.socket
sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock
cgps -s
```

You should see live GPS coordinates and satellite info.

### 4. Set Up the TFT Touchscreen

* Follow your screen's specific driver installation. For common XPT2046-based screens:

```bash
git clone https://github.com/goodtft/LCD-show.git
cd LCD-show
sudo ./LCD35-show
```

* Reboot after installation

### 5. Download Offline Map Tiles

* Download OpenStreetMap tiles for your target area (using `mobac` or online tile downloader tools)
* Store them locally, e.g., `/home/pi/maps/`

### 6. Run the PiTracker Application

* Clone or download the PiTracker source code
* Run the main Python script:

```bash
python3 pitracker.py
```

* Use the touchscreen buttons to start/stop logging and navigate the map

---

## Usage

* **Start GPS logging:** Tap the "Start" button on the touchscreen to begin tracking your route.
* **Stop GPS logging:** Tap "Stop" to finish and save your current track as a GPX file.
* **Map navigation:** Pinch or buttons to zoom in/out; drag to pan map.
* **Export routes:** Save GPX files to USB or cloud storage later.

---

## 3D Printed Case

* The enclosure is designed in TinkerCAD, tailored for all components.
* STL files are included in the main as `rpi 4b case.stl` .
* Features include:

  * Secure mounting points for Pi and screen
  * Cutouts for USB, power, GPS antenna
  * Ventilation slots to prevent overheating
* Print with PETG or PLA at 0.2mm layer height recommended

---

## Troubleshooting

| Issue                      | Solution                                                   |
| -------------------------- | ---------------------------------------------------------- |
| GPS not getting fix        | Ensure GPS antenna has clear sky view; wait longer         |
| Touchscreen not responding | Reinstall drivers, calibrate touchscreen                   |
| Screen shows no image      | Check SPI connections, reboot, test with test pattern      |
| Battery runs out quickly   | Use higher capacity power bank or add power management PCB |

---

## Future Improvements

* Add power management PCB with battery fuel gauge
* Integrate more features into firmware
* Add wireless sync to mobile app
* Improve UI with smoother map interactions

---

## Acknowledgments

* Thanks to the Raspberry Pi Foundation for the amazing hardware
* OpenStreetMap community for freely available maps
* GoodTFT for touchscreen drivers and support
* Hackclub & @alexrnn at Highway to Hardware <p><s>Hell</s>.</p> for the oppurtunity
---

## Contact

For questions or contributions, please open an issue or contact me at \[[avs.chauhan0@gmail.com](mailto:avs.chauhan0@gmail.com)].

---

# Thnx Guys pls approve

