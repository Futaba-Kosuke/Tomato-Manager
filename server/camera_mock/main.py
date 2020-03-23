from flask import Flask
from PIL import Image
import base64

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def get_test():
    return 'this is camera_mock'

@app.route('/img', methods=['GET'])
def get_img():
    with open('./test/test.jpeg', 'rb') as f:
        img = f.read()
    # base64変換した画像が返ってくる
    img_encode=base64.b64encode(img)
    return img_encode

if __name__ == '__main__':
  print('main')
  app.debug = True
  app.run()
