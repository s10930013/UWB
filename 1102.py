import math
x1225=[]
y1225=[]
x251=[]
y251=[]
def xy1225(d1225,a1225):
    

    x125 = d1225 * math.sin(a1225)
    y125 = d1225 * math.cos(a1225)
    x125=round(x125,2)+150
    y125=round(y125,2)+17
   
    x1225.append(x125)
    y1225.append(y125)

    x1=500-x125
    y1=300-y125
    x251.append(x1)
    y251.append(y1)
    return x125,y125,x1225,y1225,x251,y251