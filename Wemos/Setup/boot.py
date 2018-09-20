import webrepl
from machine import Pin
import time
import network
def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect("D'Internet", '11Kilteragh')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
do_connect()
webrepl.start()