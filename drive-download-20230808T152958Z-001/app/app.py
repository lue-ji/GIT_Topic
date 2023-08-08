from flask import Flask, render_template, Response

app = Flask(__name__)

# 模拟视频流，您可以将其替换为您的实际视频源
def generate_fake_video():
    while True:
        frame = b'\x00\xFF\x00' * 300  # 这只是一个示例的假图像数据
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_fake_video(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
