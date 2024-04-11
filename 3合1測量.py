import math
x1225=[]
y1225=[]
x251=[]
y251=[]

def xy1225(d1225,a1225):
    x125 = d1225 * math.sin(a1225)
    y125 = d1225 * math.cos(a1225)
    x125 = round(x125, 2) + 150
    y125 = round(y125, 2) + 17
    x1225.append(x125)
    y1225.append(y125)
    x1 = 500 - x125
    y1 = 300 - y125
    x251.append(x1)
    y251.append(y1)
    return x125, y125, x1225, y1225, x251, y251

import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import time
import csv

import 角度1225
import 距離1225
import 座標1225
import 畫圖1

def update_image_label(image_path, label):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo

def measure_and_display_result(n, root, image_label, result_label, coord_label):
    i = 0
    flag = 0
    while i < n:
        a1225 = math.radians(角度1225.angle1225())
        d1225, a = 距離1225.distance1225()
        x1225, y1225, x251, y251, _, _ = 座標1225.xy1225(d1225, a1225)
        print(f"1225座標: ({x1225}, {y1225})")
        畫圖1.a1(x1225, y1225)

        coord_label.config(text=f"1225座標: ({x1225}, {y1225})")

        if 250 < x1225 < 350 and 660 < y1225 < 740:
            flag = 1
            break
        i += 1
        time.sleep(1)

        update_image_label("example.png", image_label)
        root.update()

    result_text = "1225到課" if flag == 1 else "1225未到課"
    result_label.config(text=result_text)

def on_exit(root):
    root.destroy()
    root.quit()

def get_user_input():
    root = tk.Tk()
    root.title("偵測系統")

    image_label = tk.Label(root)
    image_label.pack()

    update_image_label("example.png", image_label)

    result_label = tk.Label(root, text="")
    result_label.pack()

    coord_label = tk.Label(root, text="")
    coord_label.pack()

    exit_button = tk.Button(root, text="確認", command=lambda: on_exit(root))
    exit_button.pack()

    user_input = simpledialog.askinteger("定位點名系統", "請輸入偵測次數:")
    if user_input is not None:
        measure_and_display_result(user_input, root, image_label, result_label, coord_label)
        root.mainloop()

get_user_input()
