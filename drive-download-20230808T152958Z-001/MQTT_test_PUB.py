import network
import time
from machine import Pin
from umqtt.simple import MQTTClient

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Walter_4G","ab1cd2ef33")
time.sleep(5)
print(wlan.isconnected())

sensor = Pin(16, Pin.IN, Pin.PULL_UP)
mqtt_server = 'broker.hivemq.com'   #'broker.hivemq.com'
client_id = 'bigles0814'
topic_pub = b'snail_fan'
topic_pub2 = b'snail_fan2'
topic_msg = b'hello PICO'

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
    print('Failed to connect to the MQTT Broker. Reconnecting...')
    time.sleep(5)
    machine.reset()
    
try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
client.publish(topic_pub2, "")
time.sleep(0.5)
client.publish(topic_pub, "")
while True:
    if sensor.value() == 0:
        client.publish(topic_pub2, topic_msg)
        client.publish(topic_pub, "")
        print('low')
        time.sleep(0.5)
    else:
        client.publish(topic_pub, topic_msg)
        client.publish(topic_pub2, "")
        time.sleep(0.5)
        #pass
    time.sleep(1)