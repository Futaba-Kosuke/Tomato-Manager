from flask import Flask
import base64
import random

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def get_test():
    return 'this is camera_mock'

@app.route('/camera/<camera_number>', methods=['GET'])
def get_img1(camera_number):
    num = random.randint(1, 294)
    with open('./data/' + str(num) + '.jpeg', 'rb') as f:
        img = f.read()
        print(type(img))
    # base64変換した画像が返ってくる
    img_encode=base64.b64encode(img)
    return img_encode
