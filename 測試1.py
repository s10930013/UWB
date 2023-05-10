import matplotlib.pyplot as plt
def a1(x,y):
    # 設定座標點的x, y值

    # 繪製座標點圖
    plt.scatter(x, y)
    save_path = 'example.png'
    plt.savefig(save_path)
    plt.clf()

    # 顯示圖形
    #plt.show()