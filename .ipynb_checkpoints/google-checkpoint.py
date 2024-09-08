import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

keyword = 'python'

url = 'https://kino-code.work/?s={}'.format(keyword)

r = requests.get(url)
time.sleep(3)

soup = BeautifulSoup(r.text, 'html.parser')
page_na = soup.find(class_="pagination")
page_num = page_na.find_all(class_="page-numbers")

pages = []

for i in page_num:
    pages.append(i.text)

urls = []

if not pages:
    url = 'https://kino-code.work/?s={}'.format(keyword)
else:
    last_page = int(pages[-2])

for i in range(1, last_page + 1):
    url = 'https://kino-code.work/?s={}'.format(keyword) + '&paged={}'.format(i)
    urls.append(url)

links = []
titles = []
snippets = []

for url in urls:
    r = requests.get(url)
    time.sleep(3)

    soup = BeautifulSoup(r.text, 'html.parser')

    get_list_info = soup.find_all("a", class_="gs_webResult")

    for n in range(len(get_list_info)):
        # リンクを取得
        get_list_link = get_list_info[n].attrs['href']
        links.append(get_list_link)

        # タイトルを取得
        get_list_title = get_list_info[n].attrs['title']
        titles.append(get_list_title)

        # スニペットを取得
        get_list_snippet = get_list_info[n].attrs['snippets']
        snippets.append(get_list_snippet)

result = {
    'title': titles,
    'link': links,
    'snippet': snippets
}

df = pd.DataFrame(result)
df.to_csv('result.csv', index=False, encoding='UTF-8')
