import math
x1196=[]
y1196=[]
x11962=[]
y11962=[]
def xy1196(d1196,a1196):
    

    x196 = d1196 * math.sin(a1196)
    y196 = d1196 * math.cos(a1196)
    x196=round(x196,2)+150
    y196=round(y196,2)+17
   
    x1196.append(x196)
    y1196.append(y196)

    x1=300-x196     #將正確的 xy - 測量座標得到誤差
    y1=500-y196
    x11962.append(x1)
    y11962.append(y1)
    return x196,y196,x1196,y1196,x11962,y11962