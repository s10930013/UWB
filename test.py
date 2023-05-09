import requests
import time
import math
import openpyxl
import 角度1196
import 距離1196
import 座標1196
n=int(input("請輸入偵測次數"))
i=0
while i<n:
    a1196=math.radians(角度1196.angle1196())
    d1196=距離1196.distance1196()
    ##角度轉弧度a1196=math.radians(a1196)
    x,y=座標1196.xy1196(d1196,a1196)
    print(x,y)
    i+=1
    time.sleep(1)