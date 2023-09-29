import os
import requests
import json

print(os.getcwd())

# 気象庁データの取得
url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json'
response = requests.get(url)
data = response.json()

print("response : ", json.dumps(data, indent=2))