from flask import Flask, render_template, send_file, request
from all_metods import sobel, canny, sharra, laplass
import cv2
import time

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    update = request.args.get('update')
    if update == None:
        timeout = 2
        cap = cv2.VideoCapture(0)
        time.sleep(timeout)
        sobel(cap)
        canny(cap)
        canny(cap)
        sharra(cap)
        laplass(cap)
        try:  
            cap.release(cap)
        except BaseException as e:
            print(e)
    return render_template("index.html")
@app.route('/image_canny')
def get_image1():
    # Здесь вместо path/to/image.png укажите путь к вашему изображению
    return send_file('static/img/canny.jpg', mimetype='image/png')

@app.route('/image_laplass')
def get_image2():
    # Здесь вместо path/to/image.png укажите путь к вашему изображению
    return send_file('static/img/laplass.jpg', mimetype='image/png')

@app.route('/image_sharra')
def get_image3():
    # Здесь вместо path/to/image.png укажите путь к вашему изображению
    return send_file('static/img/sharra.jpg', mimetype='image/png')

@app.route('/image_sobel')
def get_image4():
    # Здесь вместо path/to/image.png укажите путь к вашему изображению
    return send_file('static/img/sobel.jpg', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=5000)