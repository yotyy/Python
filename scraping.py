import requests
from bs4 import BeautifulSoup
import urllib.parse
 
# 対象のWebサイトからHTMLファイルをダウンロード
target_url = 'https://www.tohoku.ac.jp/japanese/'
response = requests.get(target_url)

# HTMLファイルを解析(Beautifulオブジェクトに変換します)
soup = BeautifulSoup(response.text, 'html.parser')

# 解析したHTMLファイルから必要なデータを抽出
title = soup.find('title').text


a_tags=soup.find_all('a')

#BeautidulSoupオブジェクトから<a>タグを全て検索します
url_list=[]

for a_tag in a_tags:
	href = a_tag.get('href')
	#相対URLを絶対URLに変換
	abosolute_url=urllib.parse.urljoin(target_url, href)
	#URLをリストに追加する
	url_list.append(abosolute_url)

for url in url_list:
	result = str(soup.find('kenichi'))

# 取得した情報をテキストファイルとして保存
with open("output.txt", "w") as f:
    f.write(title)
    f.write('検索結果'+result)
    #for url in url_list:
    	#f.write(url + '\n')