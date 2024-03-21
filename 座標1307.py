import math
x1307=[]
y1307=[]
x13072=[]
y13072=[]
def xy1307(d1307,a1307):
    

    x307 = d1307 * math.sin(a1307)
    y307 = d1307 * math.cos(a1307)
    x307=round(x307,2)+150
    y307=round(y307,2)+17
   
    x1307.append(x307)
    y1307.append(y307)

    x1=300-x307 #將正確的 xy - 測量座標得到誤差
    y1=500-y307
    x13072.append(x1)
    y13072.append(y1)
    return x307,y307,x1307,y1307,x13072,y13072
