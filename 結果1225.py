import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import math
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
        d1225 = 距離1225.distance1225()
        x125, y125, x1225, y1225, x12252, y12252= 座標1225.xy1225(d1225, a1225)
        print(f"1225座標: ({x125}, {y125})")
        畫圖1.a1(x125, y125)

        coord_label.config(text=f"1225座標: ({x125}, {y125})")

        if 2 < x125 < 3 and 1 < y125 < 7:   #設定座位範圍
            flag = 1
            break
        i += 1
        time.sleep(1)

        update_image_label("example.png", image_label)
        root.update()

    x1225.insert(0, "X座標")
    y1225.insert(0, "Y座標")
    x12252.insert(0, "x誤差")
    y12252.insert(0, "y誤差")
    data = list(zip(x1225, y1225, x12252, y12252))

    with open('1225.csv', "w", newline='') as s:
        w = csv.writer(s)
        w.writerows(data)

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