import requests
import time
import openpyxl
import csv
import 距離1196

def xy(x):
    r=zip(x)
    with open('xy.csv', "w") as s:
        w = csv.writer(s)
        for row in r:
            w.writerow(row)
