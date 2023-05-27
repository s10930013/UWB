import requests
import time
import math
import openpyxl
import os
import csv
import 角度1225
import 距離1225
import 座標1225
import 畫圖1
n=int(input("請輸入偵測次數"))
i=0
while i<n:
    ##角度轉弧度
    a1225=math.radians(角度1225.angle1225())
    d1225=距離1225.distance1225()
    x,y,x1225,y1225=座標1225.xy1225(d1225,a1225)
    print(x,y)
    畫圖1.a1(x,y)


    i+=1
    time.sleep(1)
##******座標數據儲存******
x1225.insert(0, "X座標")
y1225.insert(0, "Y座標")
data = list(zip(x1225, y1225))

with open('1225.csv', "w", newline='') as s:
    # 創建 CSV 寫入器
    w = csv.writer(s)

    # 將配對後的資料逐列寫入 CSV 檔案
    w.writerows(data)
    
