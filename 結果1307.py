import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk  # Import Pillow modules

import math
import time
import csv

import 角度1307
import 距離1307
import 座標1307
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
        a1307 = math.radians(角度1307.angle1307())
        d1307, a = 距離1307.distance1307()
        x, y, x1307, y1307 = 座標1307.xy1307(d1307, a1307)
        print(f"座標: ({x}, {y})")
        畫圖1.a1(x, y)

        if 250 < x < 350 and 460 < y < 540:
            flag = 1
            break
        i += 1
        time.sleep(1)

        # Update the image label with the new image after each iteration
        update_image_label("example.png", image_label)

    x1307.insert(0, "X座標")
    y1307.insert(0, "Y座標")
    data = list(zip(x1307, y1307))

    with open('1307.csv', "w", newline='') as s:
        w = csv.writer(s)
        w.writerows(data)

    result_text = "1307到課" if flag == 1 else "1307未到課"
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
