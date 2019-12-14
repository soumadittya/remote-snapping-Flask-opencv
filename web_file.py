from flask import Flask, send_file
from capture_file import capture, condition

app= Flask(__name__)

@app.route('/')
def image_show():
    capture()
    if condition == False:
        return '<h1>Cannot load image</h1>'
    else:
        return send_file('static/image.jpg', mimetype='image/jpg')

app.run(host = '0.0.0.0', port = 80, debug = True)

