import math
x1225=[]
y1225=[]
def xy1225(d1225,a1225):
    

    x = d1225 * math.sin(a1225)
    y = d1225 * math.cos(a1225)
    x=round(x,2)
    y=round(y,2)
    x=x+150
    y=y+17
    x1225.append(x)
    y1225.append(y)

    

    #   print(x,y)
    #  time.sleep(1)
    return x,y,x1225,y1225