import requests
import time
import openpyxl
def angle1196():
    i=0
    while i<n:
        response = requests.get('https://norgay.center/php/vilsnodes.php?loadranging=1&project_id=1')
        str1 = response.text.split('Tag1196')
        str2= str1[1].split('"')
        str3= str2[9].split('\\')
        a1196=float(str3[0])
        print(a1196)
        
        time.sleep(1)
        i+=1
    return a1196