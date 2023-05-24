import requests
import time
import math
import csv
import openpyxl
import 角度1196
import 距離1196
def xy1196(d1196,a1196):
    

    x = d1196 * math.sin(a1196)
    y = d1196 * math.cos(a1196)
    x=round(x,2)
    y=round(y,2)
    x=x+150
    y=y+17
 

    

    #   print(x,y)
    #  time.sleep(1)
    return x,y