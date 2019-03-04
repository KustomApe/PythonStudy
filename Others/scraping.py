import urllib.request
import re
import time
import pandas as pd

from bs4 import BeautifulSoup as bs

reexp_ptn = r'^/list1/jp/.*/[0-9]{6}-category/$'
ptn = re.compile(reexp_ptn)


def scrap(url):
    parts_data = []
    r = urllib.request.urlopen(url)
    html = r.read()
    parser = 'html.parser'
    sp = bs(html, parser)
    for tag in sp.find_all('a'):
        url = tag.get('href')
        price = tag.get('span')
        if url is None or price is None:
            continue
        if ptn.match(url):
            parts_data.append([price, url])
    return parts_data


if __name__ == '__main__':
    url = 'https://auctions.yahoo.co.jp/list1/'
    yahuoku_page_url = 'https://auctions.yahoo.co.jp'
    parts_datas = scrap(url)

    datas = []
    for parts_data in parts_datas:
        print(parts_data[0])
        datas.append(parts_data)

    df = pd.DataFrame(datas)
    df.to_csv('parts_data.csv')
