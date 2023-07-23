from machine import Pin
import machine
import utime
from lib.dht import DHT11, InvalidChecksum

pin = Pin(28, Pin.OUT)
sensor = DHT11(pin)

count=0
wifi_ready=0
uart = machine.UART(1,tx=Pin(8),rx=Pin(9),baudrate=115200)
led = Pin(25,Pin.OUT)
rst = Pin(5,Pin.OUT)
rst.value(0)
utime.sleep(0.1)
rst.value(1)
#=======MQTT========
reset='RESET'
ssid = "SSID+lu's project"   # wifi 帳號
password = 'PSWD+songgy0926'   # wifi 密碼
mqtt_server = 'BROKER+mqttgo.io'  # MQTT Broker
topic_sub = 'TOPIC+MQTT/reset/LC'  #subscribe Topic     
topic_pub1= 'TOPIC1+free2023/PICO/ear_z'  #Publish Topic
topic_pub2= 'TOPIC2+FK114514/PICO/real_me' #2nd PUB
ready='ready'  # 資料傳送至ESP01完成，開始連線

def sendCMD_waitResp(cmd, uart=uart, timeout=1000):
    print(cmd)
    uart.write(cmd+'\r\n')
    waitResp()
   
def waitResp(uart=uart, timeout=1000):
    global count,wifi_ready
    prvMills = utime.ticks_ms()
    resp = b""
    while (utime.ticks_ms()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    if resp != b'' :
        resp = str(resp)  
        print(resp)   #印出接收MQTT的paylod
        if (resp.find('on'))>=0:
            led.value(1)
        if (resp.find('off'))>=0:
            led.value(0)
            count = 0
        if (resp.find('broker_connected'))>=0:
            print('Ready')
            wifi_ready=1
            
sendCMD_waitResp(reset)
utime.sleep(0.5)
sendCMD_waitResp(ssid)
utime.sleep(0.01)
sendCMD_waitResp(password)
utime.sleep(0.01)
sendCMD_waitResp(mqtt_server)
utime.sleep(0.01)
sendCMD_waitResp(topic_sub)
utime.sleep(0.01)
sendCMD_waitResp(topic_pub1)
utime.sleep(0.01)
sendCMD_waitResp(topic_pub2)
utime.sleep(0.01)
sendCMD_waitResp(ready)

while (not wifi_ready) :
    utime.sleep(0.3)
    led.value(1)
    print('.')
    utime.sleep(0.3)
    led.value(0)
    print('.')
    waitResp()    
print('start')
utime.sleep(1)

while True :
    