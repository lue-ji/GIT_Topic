from machine import Pin, Timer 
from time import sleep
from ir_rx.nec import NEC_8, NEC_16, SAMSUNG

# 創建LED對象
led=Pin(25, Pin.OUT)
led_14=Pin(14, Pin.OUT)
tim = Timer() # 構建定時器
ir_data= 0
          
# 
def tick(tim):
    led.toggle()

ir_key = {
    0x45: '1',
    0x46: '2',
    0x47: '3',
    0x44: '4',
    0x40: '5',
    0x43: '6',
    0x07: '7',
    0x15: '8',
    0x09: '9',
    0x16: '*',
    0x19: '0',
    0x0D: '#',
    0x0C: '1',
    0x18: 'UP',
    0x5E: '3',
    0x08: 'LEFT',
    0x1C: 'OK',
    0x5A: 'RIGHT',
    0x42: '7',
    0x52: 'DOWN',
    0x4A: '9'    
    }

def callback(data, addr, ctrl):
    global ir_data 
    print('raw = ',data)
    if data > 0:  # NEC protocol sends repeat codes.
        print('Data {:02x} Addr {:04x}'.format(data, addr))
        print('data = ',ir_key[data])
        ir_data = ir_key[data]

tim.init(period=500, mode=Timer.PERIODIC, callback=tick)
while True:
    sleep(0.1)
    ir = NEC_16(Pin(28, Pin.IN), callback)  #,Pin.PULL_UP
    if int(ir_data) != 0 :
        if  ir_data == '1' :
            led_14.value(1)
            print ('led on')
            ir_data = 0
        elif ir_data == '2':
            led_14.value(0)
            print ('led off')
            ir_data = 0
        