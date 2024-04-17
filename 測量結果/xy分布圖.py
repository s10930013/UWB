import csv
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
def plot_csv_data(csv_file, output_image):
    x_values = []
    y_values = []

    # 读取CSV文件并提取XY坐标数据，跳过第一行
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # 跳过第一行
        for row in reader:
            x_values.append(float(row[0]))  # 第一列为X坐标
            y_values.append(float(row[1]))  # 第二列为Y坐标
    img = mpimg.imread('m.png')
    plt.imshow(img, extent=[0, 616, 0, 780])
    # 创建散点图
    plt.scatter(x_values, y_values)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Scatter Plot')

    # 保存图像
    plt.savefig(output_image)

    # 显示图像（可选）
    plt.show()

# 替换以下路径为你的CSV文件路径和输出图像路径
csv_file_path = 'C:/Users/20171226/Desktop/UWB/測量結果/B1.csv'
output_image_path = 'output.png'

# 绘制散点图
plot_csv_data(csv_file_path, output_image_path)
