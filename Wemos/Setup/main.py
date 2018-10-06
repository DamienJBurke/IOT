import machine
import time
import ubinascii
import webrepl
from umqtt.robust import MQTTClient
from dht import DHT22
import ujson as json
# These defaults are overwritten with the contents of /config.json by load_config()
CONFIG = {
    "broker": "192.168.0.129",
    "sensor_pin": 0, 
    "client_id": b"esp8266_" + ubinascii.hexlify(machine.unique_id()),
    "topic": "SENS-1",
}
client = None
def current_temp_humidity():
    d = DHT22(machine.Pin(CONFIG['sensor_pin']))
    d.measure()
    return d.temperature(),d.humidity()

def load_config():
    try:
        with open("/config.json") as f:
            config = json.loads(f.read())
    except (OSError, ValueError):
        print("Couldn't load /config.json")
        save_config()
    else:
        CONFIG.update(config)
        print("Loaded config from /config.json")

def save_config():
    try:
        with open("/config.json", "w") as f:
            f.write(json.dumps(CONFIG))
    except OSError:
        print("Couldn't save /config.json")

def deep_sleep(ms):
    rtc = machine.RTC()
    rtc.irq(trigger=rtc.ALARM0,wake=machine.DEEPSLEEP)
    rtc.alarm(rtc.ALARM0,ms)
    machine.deepsleep()


def main():
    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
        print('woke from a deep sleep')
    else:
        print('power on or hard reset')
    client = MQTTClient(CONFIG['client_id'], CONFIG['broker'])
    client.connect()
    print("Connected to {}".format(CONFIG['broker']))
    while True:
        temphum = current_temp_humidity()
        client.publish('{}'.format(CONFIG['topic']),bytes((str(temphum[0]) + ","+ str(temphum[1])), 'utf-8'))
        print('Published: T: {} H: {} '.format(temphum[0],temphum[1]))
        time.sleep(1)
        deep_sleep(59000)
        #time.sleep(60)

if __name__ == '__main__':
    load_config()
    main()