from flask import Flask
import numpy as np
import cv2
import base64
import requests
import json

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def get_test():
    return 'this is camera_mock'

def base64_to_numpy(img_base64):
    # base64をnumpyに変換
    img_bytes = base64.b64decode(img_base64)
    temp = np.fromstring(img_bytes, np.uint8)
    img_np = cv2.imdecode(temp, cv2.IMREAD_ANYCOLOR)
    return img_np

def numpy_to_base64(img_np):
    # numpyをbase64に変換
    _, temp = cv2.imencode('.jpeg', img_np)
    img_base64 = base64.b64encode(temp)
    return img_base64

def img_processing(img_base64):
    X = base64_to_numpy(img_base64)
    """
    ここに機械学習の処理を書き込む
    """
    y = 1  # 機械学習によって求める。テスト用に1としておく。
    return y

@app.route('/img/<num>', methods=['GET'])
def get_img(num):
    # camera_mockにリクエストを送る
    response = requests.get('http://127.0.0.1:5001/camera/1')
    img_base64 = response.text
    return img_base64

@app.route('/result/<num>', methods=['GET'])
def get_img_processing_result(num):
    response = requests.get('http://127.0.0.1:5001/camera/1')
    img_base64 = response.text
    result = img_processing(img_base64)
    return str(result)