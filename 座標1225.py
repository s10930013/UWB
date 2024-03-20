import math
x1225=[]
y1225=[]
x12252=[]
y12252=[]
def xy1225(d1225,a1225):
    

    x125 = d1225 * math.sin(a1225)
    y125 = d1225 * math.cos(a1225)
    x125=round(x125,2)+150
    y125=round(y125,2)+17
   
    x1225.append(x125)
    y1225.append(y125)

    x1=300-x125 #將正確的 xy - 測量座標得到誤差
    y1=500-y125
    x12252.append(x1)
    y12252.append(y1)
    return x125,y125,x1225,y1225,x12252,y12252

