from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Activation, Conv2D, Flatten, Dense,Dropout
from sklearn.model_selection import train_test_split
from keras.optimizers import SGD, Adadelta, Adagrad, Adam, Adamax, RMSprop, Nadam
from PIL import Image
import numpy as np
import glob, os
import matplotlib.pyplot as plt
import random, math
import tensorflow as tf
import keras
# 不要な警告を非表示にする
import warnings
warnings.filterwarnings('ignore')

#ラベリングによる学習/検証データの準備
#画像が保存されているルートディレクトリのパス
root_dir = "./data"
# 熟し具合
categories = [1, 2, 3]

# 画像データ用配列
X = []
# ラベルデータ用配列
Y = []

#画像データごとにadd_sample()を呼び出し、X,Yの配列を返す関数
def make_sample(files):
    global X, Y
    X = []
    Y = []
    for cat, fname in files:
        add_sample(cat, fname)
    return np.array(X), np.array(Y)

#渡された画像データを読み込んでXに格納し、また、画像データに対応するcategoriesのidxをY格納する関数
def add_sample(cat, fname):
    img = Image.open(fname)
    img = img.convert("RGB")
    img = img.resize((150, 150))
    data = np.asarray(img)
    X.append(data)
    Y.append(cat)

#全データ格納用配列
allfiles = []

#カテゴリ配列の各値と、それに対応するidxを認識し、全データをallfilesにまとめる
for idx, cat in enumerate(categories):
    image_dir = root_dir + "/" + str(cat)
    files = glob.glob(image_dir + "/*.jpg")
    for f in files:
        allfiles.append((idx, f))

#シャッフル後、学習データと検証データに分ける
random.shuffle(allfiles)
th = math.floor(len(allfiles) * 0.8)
train = allfiles[0:th]
test  = allfiles[th:]
X_train, y_train = make_sample(train)
X_test, y_test = make_sample(test)
xy = (X_train, X_test, y_train, y_test)
#データを保存する（データの名前を「tomato_data.npy」としている）
np.save("./data/tomato_data.npy", xy)

#モデルの構築
model = Sequential()

model.add(Conv2D(filters=32,input_shape=(150,150,3), kernel_size=(18,18), strides=(1,1), padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Activation('relu'))

model.add(Conv2D(filters=64,kernel_size=(18,18), strides=(1,1), padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Activation('relu'))
          
model.add(Conv2D(filters=128,kernel_size=(18,18), strides=(1,1), padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Activation('relu'))

model.add(Conv2D(filters=128,kernel_size=(18,18), strides=(1,1), padding='same'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(200))
model.add(Activation('relu'))

model.add(Dense(3))
model.add(Activation("sigmoid")) #分類先の種類分設定

#モデル構成の確認
model.summary()

#モデルのコンパイル
model.compile(loss='categorical_crossentropy',
              optimizer = Adam(),
              metrics = ['accuracy'])

categories = [1, 2, 3]
nb_classes = len(categories)

X_train, X_test, y_train, y_test = np.load("./data/tomato_data.npy")#保存した学習データ・テストデータのパス

X_train = X_train[:10]
X_test = X_test[:10]
y_train = y_train[:10]
y_test = y_test[:10]

#データの正規化
X_train = X_train.astype("float") / 255
X_test  = X_test.astype("float")  / 255

#one-hotエンコーディング
y_train = np.identity(3)[y_train].astype('i')
y_test = np.identity(3)[y_test].astype('i')

# 学習の開始
hist = model.fit(X_train,
           y_train,
           epochs=10,
           validation_data=(X_test, y_test),
           verbose=1,
           batch_size=1)#サンプル数

#学習結果を表示
def plot_history_loss(hist):
    # 損失値(Loss)の遷移のプロット
    plt.plot(hist.history['loss'],label="loss for training")
    plt.plot(hist.history['val_loss'],label="loss for validation")
    plt.title('model loss')
    plt.xlabel('epoch')
    plt.ylabel('loss')
    plt.legend(loc='best')
    plt.show()

def plot_history_acc(hist):
    # 精度(Accuracy)の遷移のプロット
    plt.plot(hist.history['accuracy'],label="loss for training")
    plt.plot(hist.history['val_accuracy'],label="loss for validation")
    plt.title('model accuracy')
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.legend(loc='best')
    plt.ylim([0, 1])
    plt.show()

plot_history_loss(hist)
plot_history_acc(hist)
