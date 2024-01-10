import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk  # Import Pillow modules

import math
import time
import csv

import 角度1196
import 距離1196
import 座標1196
import 畫圖1

def update_image_label(image_path, label):
    # Open the image file and convert it to a PhotoImage object
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)

    # Update the label with the new image
    label.configure(image=photo)
    label.image = photo  # Keep a reference to the PhotoImage to prevent it from being garbage-collected

def measure_and_display_result(n, root, image_label):
    result_window = tk.Toplevel(root)
    result_window.title("偵測結果")

    i = 0
    flag = 0
    while i < n:
        a1196 = math.radians(角度1196.angle1196())
        d1196, a = 距離1196.distance1196()
        x, y, x1196, y1196 = 座標1196.xy1196(d1196, a1196)
        print(f"座標: ({x}, {y})")
        畫圖1.a1(x, y)

        if 300 < x < 400 and 660 < y < 740:
            flag = 1
            break
        i += 1
        time.sleep(1)

        # Update the image label with the new image after each iteration
        update_image_label("example.png", image_label)

    x1196.insert(0, "X座標")
    y1196.insert(0, "Y座標")
    data = list(zip(x1196, y1196))

    with open('1196.csv', "w", newline='') as s:
        w = csv.writer(s)
        w.writerows(data)

    result_text = "1196到課" if flag == 1 else "1196未到課"
    result_label = tk.Label(result_window, text=result_text)
    result_label.pack()

def get_user_input():
    root = tk.Tk()
    root.withdraw()

    # Create a label for displaying the image
    image_label = tk.Label(root)
    image_label.pack()

    user_input = simpledialog.askinteger("定位點名系統", "請輸入偵測次數:")
    if user_input is not None:
        measure_and_display_result(user_input, root, image_label)
        root.mainloop()

get_user_input()
