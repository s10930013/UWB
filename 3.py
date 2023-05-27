import csv
x=[1,2,3,4,5,6,7,88,999,1000]
r=zip(x)
with open('123.csv', "w") as s:
     w = csv.writer(s)
     for row in r:
        w.writerow(row)
