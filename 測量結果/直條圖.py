import csv
import matplotlib.pyplot as plt

# 讀取 CSV 檔案，提取資料
x_error = []
y_error = []

with open('D2.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # 跳過標題行
    for row in reader:
        x_error.append(float(row[2]))  # x 誤差
        y_error.append(float(row[3]))  # y 誤差

# 繪製直條圖
plt.figure(figsize=(10, 6))
plt.bar(range(len(x_error)), x_error, color='blue', alpha=0.5, label='X Error')
plt.bar(range(len(y_error)), y_error, color='red', alpha=0.5, label='Y Error')
plt.xlabel('Data Point')
plt.ylabel('Error')
plt.title('X and Y Errors')
plt.legend()
plt.show()
