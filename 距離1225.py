import requests
import time
a=[]
def distance1225():
    
    response = requests.get('https://norgay.center/php/vilsnodes.php?loadranging=1&project_id=1')
    str1 = response.text.split('Tag1225')
    str2= str1[1].split('"')
    str3= str2[5].split('\\')
    #print(int(str3[0]))
    a.append(int(str3[0]))
    d1225=int(str3[0])


    # time.sleep(1)
    return d1225
    