import requests
import time
import openpyxl
import csv
a={}
def distance1196():

    n=int(input("請輸入偵測次數"))
    i=0
    while  i<n:
        response = requests.get('https://norgay.center/php/vilsnodes.php?loadranging=1&project_id=1')
        str1 = response.text.split('Tag1196')
        str2= str1[1].split('"')
        str3= str2[5].split('\\')
        print(int(str3[0]))
        a[i]=(int(str3[0]))


        time.sleep(1)
        i+=1
    print(a)
distance1196()
print(a[0])
r=zip(a)
with open('xy.csv', "w") as s:
    w = csv.writer(s)
    for row in r:
        w.writerow(row)
    
