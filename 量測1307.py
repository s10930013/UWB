import requests
import time
import math
import openpyxl
import os
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
    x,y=座標1307.xy1307(d1307,a1307)
    print(x,y)
    畫圖1.a1(x,y)


    i+=1
    time.sleep(1)
    
