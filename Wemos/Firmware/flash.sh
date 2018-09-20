#!/usr/bin/env bash 

esptool.py --port /dev/ttyUSB0 erase_flash \
&& esptool.py \
    --port /dev/ttyUSB0 \
    --baud 460800 write_flash \
    -fm dio -fs 16MB \
    0 firmware-combined.bin 0xffc000 esp_init_data_default.bin