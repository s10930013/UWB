import requests
import time
import openpyxl
import csv
a=[]
def distance1196():

    n=int(input("請輸入偵測次數"))
    i=0
    while  i<n:
        response = requests.get('https://norgay.center/php/vilsnodes.php?loadranging=1&project_id=1')
        str1 = response.text.split('Tag1196')
        str2= str1[1].split('"')
        str3= str2[5].split('\\')
        print(int(str3[0]))
        a.append(int(str3[0]))


        time.sleep(1)
        i+=1
    return a
    
