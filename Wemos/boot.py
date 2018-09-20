import webrepl
from machine import Pin
import time

def do_connect():
    import network
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

#import mqtt-test



#led = Pin(2,Pin.OUT)
#count =1
#while True:
#	if count % 2 ==0:
#		led(1)
#	else:
#		led(0)
#	count +=1 
#	time.sleep(5)
#	if count == 3:
#		break
