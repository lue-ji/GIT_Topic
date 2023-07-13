from machine import I2C, Pin, UART, ADC
import time
from ssd1306 import SSD1306_I2C
from mfrc522 import MFRC522
from machine import Pin

g_led = Pin(25, Pin.OUT)
r_led = Pin(14, Pin.OUT)

ic = I2C(0, sda=Pin(12), scl=Pin(13), freq=400000)
dis = SSD1306_I2C(128, 64, ic)
def uidToString(uid):
    mystring = ""
    for c in uid:
        mystring = "%02X" % c + mystring
    return mystring

reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=26, rst=10)
print(".....card to sensor please.....")

try:
    while True:
        (stat, tag_type) = reader.request(reader.REQIDL)
        if stat == reader.OK:
            (stat, uid) = reader.SelectTagSN()
            if stat == reader.OK:
                card_num = uidToString(uid)
                print("...card num: %s" % card_num)
                if card_num == "A9968823":
                    print('商品1')
                    g_led.value(1)
                    time.sleep(1)
                    g_led.value(0)
                    dis.text(card_num,10,15)
                    dis.text("commodity1",30,30)
                elif card_num == "A59D7953":
                    print("商品2")
                    g_led.value(1)
                    time.sleep(2)
                    g_led.value(0)
                    dis.text(card_num,10,15)
                    dis.text("commodity2",30,30)
                elif card_num == "A62812C3":
                    print("商品3")
                    g_led.value(1)
                    time.sleep(2)
                    g_led.value(0)
                    dis.text(card_num,10,15)
                    dis.text("commodity3",30,30)
                elif card_num == "A6FF1433":
                    print("商品4")
                    g_led.value(1)
                    time.sleep(2)
                    g_led.value(0)
                    dis.text(card_num,10,15)
                    dis.text("commodity4",30,30)
                elif card_num == "A62703C3":
                    print("商品5")
                    g_led.value(1)
                    time.sleep(2)
                    g_led.value(0)
                    dis.text(card_num,10,15)
                    dis.text("commodity5",30,30)
                elif card_num == "A6669663":
                    print("商品6")
                    g_led.value(1)
                    time.sleep(2)
                    g_led.value(0)
                    dis.text(card_num,10,15)
                    dis.text("commodity6",30,30)
                else:
                    print("查無此項")
                    r_led.value(1)    # 讀到除其他商品以外的物件後點亮紅LED
                    time.sleep(2)    # 亮 2 秒鐘
                    r_led.value(0)
                    dis.text(card_num,10,15)
                    dis.text("???",30,30)
                dis.show()
                time.sleep(1)
                dis.fill(0)
            else:
                print("WTF???")
                dis.text(str(114514),10,15)
              
                
        dis.show()
except KeyboardInterrupt:
    print("...end loading...")
    