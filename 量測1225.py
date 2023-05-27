import requests
import time
import math
import openpyxl
import os
import 角度1225
import 距離1225
import 座標1225
import 畫圖1
n=int(input("請輸入偵測次數"))
i=0
while i<n:
    #print('4')
    a1225=math.radians(角度1225.angle1225())
    #print('4')
    d1225=距離1225.distance1225()
    #print('4')
    ##角度轉弧度a1196=math.radians(a1196)
    x,y=座標1225.xy1225(d1225,a1225)
    print(x,y)
    畫圖1.a1(x,y)


    i+=1
    time.sleep(1)
    
