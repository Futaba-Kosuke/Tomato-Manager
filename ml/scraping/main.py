import sys
import requests
from bs4 import BeautifulSoup
from urllib import request

def main():
    url = sys.argv[1]
    num = sys.argv[2]
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    img_tags = soup.find_all('img')
    i = 0
    for img_tag in img_tags:
      img_url = img_tag.get('src')
      if img_url != None and img_url[-3:] != 'gif':
        request.urlretrieve(img_url, './data/' + num + '-' + str(i) + '.jpeg')
        i += 1

if __name__ == '__main__':
    main()
