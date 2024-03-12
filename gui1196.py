import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk  # 匯入Pillow模塊
import math
import time
import csv

import 角度1196
import 距離1196
import 座標1196
import 畫圖1

def update_image_label(image_path, label):
    # 打開圖片文件並將其轉換為PhotoImage對象
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # 使用新圖像更新標籤
    label.configure(image=photo)
    label.image = photo  # 保持對PhotoImage的引用以防止被垃圾回收

def measure_and_display_result(n, root, image_label, result_label):
    i = 0
    flag = 0
    while i < n:
        a1196 = math.radians(角度1196.angle1196())
        d1196, a = 距離1196.distance1196()
        x, y, x1196, y1196, x2, y2 = 座標1196.xy1196(d1196, a1196)
        print(f"座標: ({x}, {y})")
        畫圖1.a1(x, y)

        if  250 < x < 350 and 660 < y < 740:
            flag = 1
            break
        i += 1
        time.sleep(1)

        # 在每次迭代後使用新圖像更新圖像標籤
        update_image_label("example.png", image_label)
        root.update()  # 強制更新視窗

    x1196.insert(0, "X座標")
    y1196.insert(0, "Y座標")
    x2.insert(0, "x誤差")
    y2.insert(0, "y誤差")
    data = list(zip(x1196, y1196, x2, y2))

    with open('1196.csv', "w", newline='') as s:
        w = csv.writer(s)
        w.writerows(data)

    result_text = "1196到課" if flag == 1 else "1196未到課"
    result_label.config(text=result_text)

def get_user_input():
    root = tk.Tk()
    root.title("偵測系統")

    # 建立用於顯示圖像的標籤
    image_label = tk.Label(root)
    image_label.pack()

    # 顯示初始圖片
    update_image_label("example.png", image_label)

    # 建立用於顯示結果的標籤
    result_label = tk.Label(root, text="")
    result_label.pack()

    user_input = simpledialog.askinteger("定位點名系統", "請輸入偵測次數:")
    if user_input is not None:
        measure_and_display_result(user_input, root, image_label, result_label)
        root.mainloop()

get_user_input()
