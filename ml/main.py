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

#ラベリングによる学習/検証データの準備
#画像が保存されているルートディレクトリのパス
root_dir = "パス"
# 熟し具合
categories = ["熟している", "熟す途中", "熟していない"]

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
    image_dir = root_dir + "/" + cat
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
np.save("保存先パス/tomato_data.npy", xy)

#モデルの構築
model = models.Sequential()
model.add(Conv2D(32,(3,3),Activation="relu",input_shape=(150,150,3)))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(64,(3,3),Activation="relu"))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(128,(3,3),Activation="relu"))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(128,(3,3),Activation="relu"))
model.add(MaxPooling2D((2,2)))
model.add(Flatten())
model.add(Dropout(0.2))
model.add(Dense(512,Activation="relu"))
model.add(Dense(10,Activation="sigmoid")) #分類先の種類分設定

#モデル構成の確認
model.summary()

#モデルのコンパイル
model.compile(loss='categorical_crossentropy',
              optimizer = Adam(),
              metrics = ['accuracy'])

categories = ["熟している", "熟す途中", "熟していない"]
nb_classes = len(categories)

X_train, X_test, y_train, y_test = np.load("保存した学習データ・テストデータのパス")

#データの正規化
X_train = X_train.astype("float") / 255
X_test  = X_test.astype("float")  / 255

#one-hotエンコーディング
y_train = np.identity(5)[y_train].astype('i')
y_test = np.identity(5)[y_test].astype('i')

# 学習の開始
model.fit(X_train, 
          Y_train,
          epochs=30,
          validation_data=(X_test, Y_test),
          verbose=1,
          batch_size=#サンプル数
          )

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
    plt.plot(hist.history['acc'],label="loss for training")
    plt.plot(hist.history['val_acc'],label="loss for validation")
    plt.title('model accuracy')
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.legend(loc='best')
    plt.ylim([0, 1])
    plt.show()

plot_history_loss(hist)
plot_history_acc(hist)
