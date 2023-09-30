# -*- coding: utf-8 -*-

import os
import requests
import json

# 気象庁データの取得
url = 'https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json'
response = requests.get(url)
date = response.json()
str(date)

print("response : ", date)