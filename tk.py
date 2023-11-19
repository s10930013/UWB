import requests
import time
import math
import openpyxl
import os
import csv
import numpy as np
##import matplotlib.pyplot as plt
import 角度1196
import 距離1196
import 座標1196
import 畫圖1
import tkinter as tk

def custom_program(n,text_widget):
    # 在这里执行你的自定义程序，例如打印一条消息
    
    
    output_text = f"輸出 {n}."
    text_widget.insert(tk.END, output_text + "\n")

class CustomProgramApp:
    def __init__(self, master):
        self.master = master
        self.master.title("計時定位點名系統")

        self.label = tk.Label(master, text="請輸入計時秒數:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.text_widget = tk.Text(master, height=40, width=90)
        self.text_widget.pack()

        self.start_button = tk.Button(master, text="Run Program", command=self.run_program)
        self.start_button.pack()

    def run_program(self):
        try:
            duration = int(self.entry.get())
            custom_program(duration, self.text_widget)
        except ValueError:
            self.text_widget.insert(tk.END, "Invalid input. Please enter a valid number.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomProgramApp(root)
    root.mainloop()
