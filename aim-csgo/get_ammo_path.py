# _*_ coding : utf-8 _*_
# @Time : 2022/6/30 14:13
# @Author : Cosmica
# @File : get_ammo_path
# @Project : Yolov5ForCSGO


# 未完成
import csv

f = csv.reader(open('./ammo_path/ak47.csv', encoding='utf-8'))
list = []
for i in f:
    list.append(i)

print(list)


























