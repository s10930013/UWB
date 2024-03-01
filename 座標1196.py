import math
x1196=[]
y1196=[]
x2=[]
y2=[]
def xy1196(d1196,a1196):
    

    x = d1196 * math.sin(a1196)
    y = d1196 * math.cos(a1196)
    x=round(x,2)
    y=round(y,2)
    x=x+150
    y=y+17
    x1196.append(x)
    y1196.append(y)

    x1=300-x
    y1=300-y
    x2.append(x1)
    y2.append(y1)
    return x,y,x1196,y1196,x2,y2