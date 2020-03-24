import lxml
import requests
from bs4 import BeautifulSoup
import urllib.request

for num in range(25):
	#ヘッダーを設定する
	headers = {"User-Agent":"hoge"}
	#検索ページのURLを格納する
	URL = "https://search.yahoo.co.jp/image/search?p=%E3%83%88%E3%83%9E%E3%83%88+-%E6%96%99%E7%90%86&fr=top_ga1_sa&ei=UTF-8&b={}".format(1 + 20*num)
	#URLからレスポンスが返ってくるようにする
	resp = requests.get(URL, timeout=1, headers=headers)
	#HTMLの抽出したい部分を格納
	soup = BeautifulSoup(resp.text, "lxml")
	#find_allで条件の部分をすべて書き出す
	imgs = soup.find_all(alt="「トマト -料理」の画像検索結果")
	#filepathに画像のURLをいれ、そのURLをダウンロードする。
	for i in range(len(imgs)):
		filepath = "image_data/{0}-{1}.jpg".format(num,i)
		urllib.request.urlretrieve(imgs[i]["src"],filepath)

