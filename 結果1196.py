import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk  # 匯入 Pillow 模組

import math
import time
import csv

import 角度1196
import 距離1196
import 座標1196
import 畫圖1

def update_image_label(image_path, label):
    # 打開圖片文件並轉換為 PhotoImage 物件
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # 使用新圖片更新標籤
    label.configure(image=photo)
    label.image = photo  # 保持對 PhotoImage 的引用，防止被垃圾回收

def measure_and_display_result(n, root, image_label):
    result_window = tk.Toplevel(root)
    result_window.title("偵測結果")

    i = 0
    flag = 0
    while i < n:
        a1196 = math.radians(角度1196.angle1196())  # 將角度轉換為弧度
        d1196, a = 距離1196.distance1196()  # 獲取距離
        x, y, x1196, y1196,x2,y2 = 座標1196.xy1196(d1196, a1196)  # 計算座標
        print(f"座標: ({x}, {y})")
        畫圖1.a1(x, y)  # 繪製圖形

        # 檢查座標是否在特定範圍內
        if 250 < x < 350 and 660 < y < 740:
            flag = 1  # 設置旗標以表示條件符合
            break
        i += 1
        time.sleep(0.6)  # 暫停一秒

        # 在每次迭代後更新圖片標籤
        update_image_label("example.png", image_label)

    x1196.insert(0, "X座標")
    y1196.insert(0, "Y座標")
    x2.insert(0, "x誤差")
    y2.insert(0, "y誤差")
    data = list(zip(x1196, y1196,x2,y2))

    # 將資料寫入 CSV 檔案
    with open('1196.csv', "w", newline='') as s:
        w = csv.writer(s)
        w.writerows(data)

    # 根據條件顯示結果
    result_text = "1196到課" if flag == 1 else "1196未到課"
    result_label = tk.Label(result_window, text=result_text)
    result_label.pack()

def get_user_input():
    root = tk.Tk()
    root.withdraw()

    # 創建用於顯示圖片的標籤
    image_label = tk.Label(root)
    image_label.pack()

    # 詢問使用者輸入偵測次數
    user_input = simpledialog.askinteger("定位點名系統", "請輸入偵測次數:")
    if user_input is not None:
        # 呼叫 measure_and_display_result 函數
        measure_and_display_result(user_input, root, image_label)
        root.mainloop()

get_user_input()
