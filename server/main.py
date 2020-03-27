from flask import Flask
import numpy as np
import cv2
import base64
import requests
import json

import tensorflow as tf
import keras
import keras
from keras.models import Sequential
from keras.layers import Dense, Activation,Dropout
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
from keras.layers import Flatten
from keras.optimizers import Adam
from keras.models import load_model
from keras.models import model_from_json

app = Flask(__name__)

graph = tf.get_default_graph()

# JSONファイルからモデルのアーキテクチャを得る
model_arc_str = open('./model/model_architecture.json').read()
model = model_from_json(model_arc_str)

# モデル構成の確認
model.summary()

# モデルの重みを得る
model.load_weights('./model/weights.hdf5')

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
    global graph
    with graph.as_default():
        X = base64_to_numpy(img_base64)
        print(X.shape)
        X = cv2.resize(X, (150, 150))
        X = X.astype('float') / 255
        X = X.reshape(1, 150, 150, 3)
        print(X.shape)
        y = model.predict(X)
        # y = 1  # 機械学習によって求める。テスト用に1としておく。
        if np.round(y)[0][0] == 1:
            result = False
        else:
            result = True
        return result

@app.route('/result/<num>', methods=['GET'])
def get_result(num):
    response = requests.get('http://127.0.0.1:5001/camera/' + num)
    img_base64 = response.text
    y = img_processing(img_base64)
    result = {
        'result': y, 
        'img_base64': img_base64
    }
    return result

@app.route('/result', methods=['GET'])
def get_results():

    results = {}
    for num in range(1, 5):
        response = requests.get('http://127.0.0.1:5001/camera/' + str(num))
        img_base64 = response.text
        y = img_processing(img_base64)
        result = {
            'result': y, 
            'img_base64': img_base64
        }
        results[str(num)] = result
    
    return results

if __name__ == '__main__':
    model = create_model()
    model.load_weights('./model/model.ckpt')
