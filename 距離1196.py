import requests
import time
import openpyxl
n=int(input("請輸入偵測次數"))
a={}
def distance1196():
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