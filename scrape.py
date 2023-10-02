import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
from urllib.parse import urlencode

# スクレイピング部分

# year, month,block_no

def scrape_weather_data(year, month,block_no):
    
    # 西条の場合はURLを変更
    if block_no == '0958':
        base_url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/daily_a1.php'
    else:
        base_url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/daily_s1.php'
    
    params = {
        'prec_no': '73',
        'block_no': block_no,
        'year': year,
        'month': month,
        'day': '',
        'view': 'p1'
    }

    # Webページを取得
    response = requests.get(base_url, params=params)
    response.raise_for_status()

    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(response.content, 'html.parser')

    # テーブルを探す
    table = soup.find("table", class_="data2_s")

    if table is None:
        full_url = f"{base_url}?{urlencode(params)}"
        print(f"テーブルが見つかりませんでした。: {year}/{month} {full_url}")

        # テーブルの中身がなかった場合にデバッグ用にHTMLを保存
        with open(f"weather_{year}_{month}.html", mode="w") as f:
            f.write(str(soup))

        return []


    # 行を抽出
    trs = table.find_all("tr")
    
    data_list = []
    for tr in trs:
        tds = tr.find_all("td")
        if len(tds) == 0:
            continue

        # 降水量
        prec = tds[3].text

        # 平均気温
        avg_temp = tds[6].text

        # 最低気温
        min_temp = tds[7].text

        # 最高気温
        max_temp = tds[8].text


        row_data = [year, month, prec, avg_temp, min_temp, max_temp]
        data_list.append(row_data)

    return data_list

# 現在の年と月を取得
current_year = datetime.now().year
current_month = datetime.now().month

# 直近1年のデータを取得するための年月リストを生成 (現在の月は除外)
dates = []
current_month -= 1  # 現在の月を除外
if current_month == 0:
    current_month = 12
    current_year -= 1

for _ in range(12):
    dates.append((current_year, current_month))
    current_month -= 1
    if current_month == 0:
        current_month = 12
        current_year -= 1

# 松山・宇和島・西条の観測地点番号と名称
block_info = {
    '47887': '松山',
    '47892': '宇和島',
    '0958':  '西条'
}

#出力データ
weather_data = []

for block, location in block_info.items():
    for year, month in dates:
        data = scrape_weather_data(year, month, block)
        # time.sleep(0.1)
        for row in data:
            row_data = [location] + row  # 地点名をデータに追加
            weather_data.append(row_data)

# pandasを使用してデータフレームに変換
df = pd.DataFrame(weather_data, columns=['Location', 'Year', 'Month', 'Precipitation', 'Average Temp', 'Min Temp', 'Max Temp'])
print(df)