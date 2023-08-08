import machine
import utime

# 配置蜂鸣器引脚
buzzer_pin = machine.Pin(28, machine.Pin.OUT)

def beep():
    # 触发蜂鸣器声音
    buzzer_pin.on()
    utime.sleep(0.5)  # 控制蜂鸣器持续时间
    buzzer_pin.off()

# 启动一个 Web 服务器，接收关闭警报器的请求
from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/close':
            beep()  # 触发蜂鸣器声音
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Not Found')

server_address = ('', 8080)
httpd = HTTPServer(server_address, RequestHandler)
httpd.serve_forever()
