# _*_ coding : utf-8 _*_
# @Time : 2022/6/30 14:13
# @Author : Lucid1ty
# @File : get_ammo_path
# @Project : Yolov5ForCSGO

# Incomplete
import csv

f = csv.reader(open('./ammo_path/ak47.csv', encoding='utf-8'))
list = []
for i in f:
    list.append(i)

print(list)
