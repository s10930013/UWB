import tkinter as tk
winimport tkinter as tk
window = tk.Tk()
window.title('window')
window.geometry('500x100') #寬度*高度
label_1 = tk.Label(window, text='Hello World', bg='yellow', fg='#bd34eb',
font=('Arial', 12))
#label_1.grid(column=0, row=0)
label_1.pack() # 預設位置’top’來配置標籤
window.mainloop()