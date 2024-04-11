import requests
import time
import math
import openpyxl
import os
import csv
import 角度1307
import 距離1307
import 座標1307
import 畫圖1
n=int(input("請輸入偵測次數"))
i=0
while i<n:
    ##角度轉弧度
    a1307=math.radians(角度1307.angle1307())
    d1307=距離1307.distance1307()
    x,y,x1307,y1307=座標1307.xy1307(d1307,a1307)
    print(x,y)
    畫圖1.a1(x,y)


    i+=1
    time.sleep(1)
##******座標數據儲存******
x1307.insert(0, "X座標")
y1307.insert(0, "Y座標")
data = list(zip(x1307, y1307))

with open('1307.csv', "w", newline='') as s:
    # 創建 CSV 寫入器
    w = csv.writer(s)

    # 將配對後的資料逐列寫入 CSV 檔案
    w.writerows(data)
    