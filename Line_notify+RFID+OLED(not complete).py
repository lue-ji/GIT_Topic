import machine
from lib.dht import DHT11, InvalidChecksum
from machine import I2C, Pin, UART, ADC
import time
from ssd1306 import SSD1306_I2C
from mfrc522 import MFRC522
from machine import Pin

pin = Pin(28, Pin.OUT)
sensor = DHT11(pin)
g_led = Pin(25, Pin.OUT)
r_led = Pin(14, Pin.OUT)

ic = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
dis = SSD1306_I2C(128, 64, ic)

wifi_ready=0
uart = machine.UART(1,tx=Pin(8),rx=Pin(9),baudrate=115200)
led = Pin(25,Pin.OUT)
rst = Pin(5,Pin.OUT)
rst.value(0)
time.sleep(0.1)
rst.value(1)
reset='RESET'
def sendCMD_waitResp(cmd, uart=uart, timeout=500):
    print(cmd)
    uart.write(cmd+'\r\n')
    waitResp()
   
def waitResp(uart=uart, timeout=500):
    global count,wifi_ready
    prvMills = time.ticks_ms()
    resp = b""
    while (time.ticks_ms()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    if resp != b'' :
        resp = str(resp)  
        print(resp)   #印出接收MQTT的paylod
        if (resp.find('connect'))>=0:
            print('Ready')
            wifi_ready=1
            
sendCMD_waitResp("RESET")
time.sleep(0.5)
sendCMD_waitResp("SSID+lu's project")
time.sleep(0.1)
sendCMD_waitResp("PSWD+songgy0926")
time.sleep(0.1)
sendCMD_waitResp("TOKEN+ZTFrMwibjoJ26tmaceTLNzhXWwPpojFj684ORdSrhF1")
time.sleep(0.1)
sendCMD_waitResp("ready")
time.sleep(0.1)

while (not wifi_ready) :
    time.sleep(0.3)
    led.value(1)
    print('.')
    time.sleep(0.3)
    led.value(0)
    print('.')
    waitResp()    
print('start')
time.sleep(5)

def uidToString(uid):
    mystring = ""
    for c in uid:
        mystring = "%02X" % c + mystring
    return mystring

reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=26, rst=10)
print(".....commodity to sensor.....")

try:
    while True:
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card_num = uidToString(uid)
                print("...card num: %s" % card_num)
                if card_num == "A9968823":
                    print('commodity1')
                    g_led.value(1)
                    time.sleep(1)
                    g_led.value(0)
                    #sendCMD_waitResp('commodity coming')
                    time.sleep(0.5)
                    dis.text(card_num,10,10)
                    dis.text("commodity1",10,25)
                    dis.text("kind:",4,50)
                elif card_num == "A59D7953":
                    print("commodity2")
                    g_led.value(1)
                    time.sleep(2)
                    g_led.value(0)
                    dis.text(card_num,10,10)
                    dis.text("commodity2",10,25)
                    dis.text("kind:",4,50)
                elif card_num == "A62812C3":
                    print("commodity3")
                    g_led.value(1)
                    time.sleep(2)
                    g_led.value(0)
                    dis.text(card_num,10,10)
                    dis.text("commodity3",10,25)
                    dis.text("kind:",4,50)
                elif card_num == "A6FF1433":
                    print("commodity4")
                    g_led.value(1)
                    time.sleep(2)
                    g_led.value(0)
                    dis.text(card_num,10,10)
                    dis.text("commodity4",10,25)
                    dis.text("kind:",4,50)
                elif card_num == "A62703C3":
                    print("commodity5")
                    g_led.value(1)
                    time.sleep(2)
                    g_led.value(0)
                    dis.text(card_num,10,10)
                    dis.text("commodity5",10,25)
                    dis.text("kind:",4,50)
                elif card_num == "A6669663":
                    print("commodity6")
                    g_led.value(1)
                    time.sleep(2)
                    g_led.value(0)
                    dis.text(card_num,10,10)
                    dis.text("commodity6",10,25)
                    dis.text("kind:",4,50)
                else:
                    print("Out of range")
                    r_led.value(1)    # 讀到除其他商品以外的物件後點亮紅LED
                    time.sleep(1)    # 亮1秒鐘
                    r_led.value(0)
                    dis.text(card_num,10,10)
                    dis.text("???",10,25)
                    dis.text("kind not found",4,50)
                dis.show()
                time.sleep(1)
                dis.fill(0)
            else:
                print("out of permission")
                dis.text(str(1919810),25,30)
              
                
        dis.show()
except KeyboardInterrupt:
    print("...end loading...")
    