import requests
import time
import math
import openpyxl
import os
import csv
import numpy as np
##import matplotlib.pyplot as plt
import 角度1196
import 距離1196
import 座標1196
import 畫圖1
def measure1196():  
    n=int(input("請輸入偵測次數"))
    i=0
    flag = 0
    while i<n:
        ##角度轉弧度
        a1196=math.radians(角度1196.angle1196())
        d1196,a=距離1196.distance1196()
        x,y,x1196,y1196=座標1196.xy1196(d1196,a1196)
        print(x,y)
        畫圖1.a1(x,y)
        
        if 200<x<400 and 0<y<200:
            flag=1
            break
        i+=1
        time.sleep(1)
    ##******座標數據儲存******
    x1196.insert(0, "X座標")
    y1196.insert(0, "Y座標")
    data = list(zip(x1196, y1196))

    with open('1196.csv', "w", newline='') as s:
        # 創建 CSV 寫入器
        w = csv.writer(s)

        # 將配對後的資料逐列寫入 CSV 檔案
        w.writerows(data)

    if flag == 1:
        print("1196到課")
    else:
        print("1196未到課")

