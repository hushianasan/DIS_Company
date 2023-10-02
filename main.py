from scrape import scrape_weather_data

# 松山市, 西条市, 宇和島市の出力が出来る関数
# ３地点の指定をさせて出力する関数

print("Start ! !")
print("1. 年のみ指定 ! !")
print("2. 年月のみ指定 ! !")
n = int(input("Input : "))

#str year, month, block_info 多分使わない
j = 0

while True:
	if n == 1:
		# n = 1
		print("年のみ指定 ! !")
		year = input("year : ")
		month = input("month : ")
		block_info = input("block_info : ")
		scrape_weather_data(year, month, block_info)
		

	elif n == 2:
		# n = 2
		print("年月のみ指定 ! !")
		year = input("year : ")
		month = input("month : ")
		block_info = input("block_info : ")
		scrape_weather_data(year, month, block_info)

	else:
		print("Error")
		break
		