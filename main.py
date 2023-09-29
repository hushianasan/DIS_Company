import os
import requests
import json

# 気象庁データの取得
A = open("https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json", "r")
B = json.load(A) 
#print(B)

'''
jma_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
print(jma_url)
'''