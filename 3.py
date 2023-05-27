import matplotlib.pyplot as plt

# 插入背景图片
img=plt.imread("t.png")
fig,ax=plt.subplots()
# 指定图片的高度和宽度
ax.imshow(img,extent=[0,120,0,100])

x = [10,20,30,40,50,60,70,80,90,100]
y1 = [7,17,27,37,43,49,57,65,71,77]
y2 = [7,17,27,37,45,54,59,67,75,83]
y3 = [8,18,28,38,47,56,64,73,80,89]
y4 = [10,20,30,40,50,60,70,80,90,100]
plt.plot(x,y1,color='grey',linewidth=2.0,linestyle='-')
plt.plot(x,y2,color='orange',linewidth=2.0,linestyle='-')
plt.plot(x,y3,color='blue',linewidth=2.0,linestyle='-')
plt.plot(x,y4,color='red',linewidth=2.0,linestyle='-')
plt.xlabel('Xlabel')
plt.ylabel('Ylabel')

# 设置小图标
plt.legend(['A','B','C','D'],loc='upper left',fontsize = 10)
plt.show()