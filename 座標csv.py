import csv

x = [1, 2, 3, 4, 5, 6, 7, 88, 999, 1000]
y = [5, 5, 66, 32, 26, 548, 364, 36, 99, 11111]
x.insert(0, "X座標")
y.insert(0, "Y座標")
data = list(zip(x, y))

with open('123.csv', "w", newline='') as s:
    # 創建 CSV 寫入器
    w = csv.writer(s)

    # 將配對後的資料逐列寫入 CSV 檔案
    w.writerows(data)

