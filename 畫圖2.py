import matplotlib.pyplot as plt
def a1(x,y,x1,y1):
   # 插入背景图片
    img=plt.imread("m.png")
    fig,ax=plt.subplots()
    # 指定图片的高度和宽度
    ax.imshow(img,extent=[0,616,0,780])
    plt.xlim(0,616)
    plt.ylim(0,780)

    plt.scatter(x,y)
    plt.scatter(x1,y1)
    save_path = 'example.png'
    plt.savefig(save_path)
    plt.clf()

    # 顯示圖形
    #plt.show()12