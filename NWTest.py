import requests

# 気象庁データの取得
url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json'
response = requests.get(url)
data = response.json()

# レスポンスを文字列に変換して表示
print("response : ", data)
