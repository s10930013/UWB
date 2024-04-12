import requests
import time
def angle1196():
    
    
    response = requests.get('https://norgay.center/php/vilsnodes.php?loadranging=1&project_id=1')
    str1 = response.text.split('Tag1196')
    str2= str1[1].split('"')
    str3= str2[9].split('\\')
    a1196=float(str3[0])
    #print(a1196)
    

    #a1196=float(30)
    
    return a1196