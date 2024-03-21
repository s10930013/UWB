import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk
import math
import time
import 角度1196
import 距離1196
import 座標1196
import 角度1225
import 距離1225
import 座標1225
import 畫圖2

def update_image_label(image_path, label):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo

def measure_and_display_result(n, root, image_label, result_label, coord_label):
    i = 0
    flag1196 = 0
    flag1225 = 0
    while i < n:
        # 檢測 tag 1196
        a1196 = math.radians(角度1196.angle1196())
        d1196, a = 距離1196.distance1196()
        x196, y196, x1196, y1196, x11962, y11962 = 座標1196.xy1196(d1196, a1196)
        print(f"1196座標: ({x196}, {y196})")

   
        if 280 < x196 < 700 and 450 < y196 < 500:   # 設定1196座位範圍
            flag1196 = 1
            
        # 檢測 tag 1225
        a1225 = math.radians(角度1225.angle1225())
        d1225 = 距離1225.distance1225()
        x125, y125, x1225, y1225, x12252, y12252 = 座標1225.xy1225(d1225, a1225)
        print(f"1225座標: ({x125}, {y125})")
        
        
        
        coord_label.config(text=f"藍點1225座標: ({x125}, {y125})\n橘點1196座標: ({x196}, {y196})")
        # 繪製 tag 1225 的座標 繪製 tag 1196 的座標
        畫圖2.a1(x125, y125,x196, y196)

        if 2 < x125 < 400 and 1 < y125 < 300:   # 設定 1225 座位範圍
            flag1225 = 1

        if flag1196 == 1 and flag1225 == 1:
            break

        i += 1
        time.sleep(1)
        update_image_label("example.png", image_label)
        root.update()

   
    


    result_text = "1196到課" if flag1196 == 1 else "1196未到課"
    result_text += "\n"
    result_text += "1225到課" if flag1225 == 1 else "1225未到課"
    result_label.config(text=result_text)

def on_exit(root):
    root.destroy()
    root.quit()

def get_user_input():
    root = tk.Tk()
    root.title("偵測點名系統")

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
