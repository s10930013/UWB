import requests
import time
import math
import openpyxl
import os
import csv
import matplotlib.pyplot as plt

import 角度1196
import 距離1196
import 座標1196
import 畫圖1

n = int(input("請輸入偵測次數"))
i = 0
x1196 = []
y1196 = []
a = []

while i < n:
    # 角度轉弧度
    a1196 = math.radians(角度1196.angle1196())
    d1196, a_val = 距離1196.distance1196()
    x, y, x1196_val, y1196_val = 座標1196.xy1196(d1196, a1196)
    print(x, y)
    畫圖1.a1(x, y)

    x1196.append(x1196_val)
    y1196.append(y1196_val)
    a.append(a_val)

    i += 1
    time.sleep(1)

# ******座標數據儲存******
x1196.insert(0, "X座標")
y1196.insert(0, "Y座標")
data = list(zip(x1196, y1196))

with open('1196.csv', "w", newline='') as s:
    # 創建 CSV 寫入器
    w = csv.writer(s)

    # 將配對後的資料逐列寫入 CSV 檔案
    w.writerows(data)

# 生成 x 軸數據
x = range(len(a))

# 繪製折線圖
plt.plot(x, a)

# 設定標題和軸標籤
plt.title('Line Chart')
plt.xlabel('Index')
plt.ylabel('Value')

# 顯示圖形
plt.show()