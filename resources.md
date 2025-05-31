## Any extra resources I come across when building will be put here
### WIRING : 
Power:
Raspberry Pi powered via micro USB

TFT and GPS powered from Pi's 5V and GND

3.5" SPI TFT Display (Waveshare):
MOSI → GPIO10 (Physical Pin 19)

MISO → GPIO9 (Pin 21) (not always used for display only)

SCLK → GPIO11 (Pin 23)

CS → Any free GPIO (e.g. GPIO8, Pin 24)

DC (D/C) → Any GPIO (e.g. GPIO25, Pin 22)

RESET → Any GPIO (e.g. GPIO27, Pin 13)

VCC → 5V (Pin 2 or 4)

GND → GND (Pin 6 or any GND)

NEO-6M GPS Module:
VCC → 5V (Pin 2 or 4)

GND → GND (Pin 6 or any GND)

TX → GPIO15 (UART RX, Pin 10)

RX → GPIO14 (UART TX, Pin 8)
