# 松山, 西条市, 宇和島市の出力が出来る関数
# ３地点の指定をさせて出力する関数

print("Start ! !\n")
print("1. 年のみ指定\n")
print("2. 年月のみ指定\n")
n = int(input("Input : "))

if n == 1:
	print("年のみ指定 ! !\n")
	m = int(input("Input : ")) #松山, 西条市, 宇和島 地点の指定
	# mを関数につなげて結果返す
elif n == 2:
	print("年月のみ指定 ! !\n")
	m = int(input("Input : ")) # 松山, 西条市, 宇和島 地点の指定
	# mを関数につなげて結果返す 
else:
	print("Error")
# do whileで組む
