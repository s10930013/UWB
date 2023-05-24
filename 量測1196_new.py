import csv
import 距離1196
import 角度1196
import 距離1225
import 角度1225
import 距離1307
import 角度1307
import 座標換算
import os
import matplotlib.pyplot as plt
from pylab import yticks,np
import numpy as np
import time
import math
import 座標數據
import 座標數據
#ospath=os.path.dirname(os.path.abspath(__file__))
os.chdir('./data')#位置設定
offsettime,offsetx,offsety,offsetl=20,0,0,0#樣本數據數設定
print("輸入1196編號")
choise=input()
C=座標數據.choise(choise)
orl1196=C['l']
ora1196=C['a']
orx1196=C['x']
ory1196=C['y']
print('請輸入測量次數')
te=input().split()
#te=('300').split()
tme=int(te[0])
talx,taly,length,angle,pi,po=[],[],[],[],[],[]
fixx,fixy,fixl=[],[],[]
i=1
while i <= tme:
    length1196 = 距離1196.length()#距離
    angle1196 = 角度1196.angle()#角度
    x1196,y1196=座標換算.mathxy(length1196,angle1196)#AOA座標在這裡設定
    print(x1196,y1196)
    talx.append(float(x1196))
    taly.append(float(y1196))
    length.append(int(length1196))
    angle.append(angle1196)
    pi.append(i),po.append(int(orl1196))
    time.sleep(0.6)#迴圈秒數
    i=i+1
for i in range(0,offsettime,1):
    offsetx=offsetx+talx[i]
    offsety=offsety+taly[i]
    offsetl=offsetl+length[i]
    fixx.append(talx[i])
    fixy.append(taly[i])
    fixl.append(length[i])
offsetx=offsetx/offsettime-orx1196
offsety=offsety/offsettime-ory1196
offsetl=offsetl/offsettime-orl1196
for i in range(offsettime,len(talx),1):
    fixx.append(talx[i]-offsetx)
    fixy.append(taly[i]-offsety)
    fixl.append(length[i]-offsetl)
with open(choise+'.csv', 'w+',encoding='utf-8-sig', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([ '距離' , '角度','修正距離', 'x', 'y', '修正x', '修正y', '距離offset='+str(offsetl),'xoffset='+str(offsetx),'yoffset='+str(offsety), '樣本數據數'+str(offsettime)])  
    for i in range(0,len(talx),1):
        writer.writerow([str(format(length[i])), str(format(angle[i])), str(format(fixl[i])), str(format(talx[i])), str(format(taly[i])) , str(format(fixx[i])), str(format(fixy[i])),'', '', '' , '' ])
#圖表的設定
print(len(pi),len(length),len(fixl))
fig = plt.figure(1,figsize=(20,10))
ax = fig.add_subplot(1, 2, 1)
#散佈圖
ax.grid(True)

plt.rcParams['font.sans-serif']=['DFKai-SB']
plt.title(choise+"距離誤差導正", fontsize=15, x=0.5, y=1.03)
ax.plot(pi, length,linestyle = 'dotted',label="測量距離")  
ax.plot(pi, fixl, 'b',label="修正距離")
ax.plot(pi, po, 'r',label="實際距離")
plt.xlabel("次數",  fontsize=10, labelpad = 5)
plt.ylabel("距離",  fontsize=10, labelpad = 10)
plt.legend()

ax = fig.add_subplot(1, 2, 2)

ax.grid(True)
plt.xlim(0,750)
plt.ylim(0,600)
plt.rcParams['font.sans-serif']=['DFKai-SB']
plt.title(choise+'座標分布', fontsize=15, x=0.5, y=1.03)
ax.scatter(talx, taly, color='b',label="測量座標") 
ax.scatter(int(orx1196), int(ory1196), color='r',label="原本座標",marker='D')
ax.scatter(fixx, fixy, color='g',label="修正座標",marker='*')
plt.xlabel("x",  fontsize=10, labelpad = 5)
plt.ylabel("y",  fontsize=10, labelpad = 2)
plt.legend()
plt.savefig(choise+".jpg",transparent = True)
plt.show()
#plt.savefig(cm+'公分誤差導正.png')