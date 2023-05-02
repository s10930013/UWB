import requests
import time
import openpyxl
import csv
import 距離1196

a=距離1196.distance1196()
r=zip(a)
with open('xy.csv', "w") as s:
    w = csv.writer(s)
    for row in r:
        w.writerow(row)
