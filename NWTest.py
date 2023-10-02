import requests
from be4 import BeautifulSoup

# year
# month
# block_no

def scrape_weather_data(year, month, block_no):

    if block_no == "0958":
    # 西条市
        base_url = https://www.data.jma.go.jp/obd/stats/etrn/view/daily_a1.php
    else:
    # 松山市, 宇和島
        base_url = https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php

    block_no = {
        '47887': '松山',
        '47892': '宇和島',
        '0958':  '西条'
    }

    params = {
        'prec_no': '73',
        'block_no': block_no,
        'year': year,
        'month': month,
        'day': '',
        'view': 'p1'
    }

    response = requests.get(base_url, params=params)

        # URLにparamsを付与させる
        base_url = 

        html = requests.get(url)

    # Webスクレイピングする
    