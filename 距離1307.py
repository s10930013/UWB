import requests
import random
a=[]
def distance1307():
    
    '''
    response = requests.get('https://norgay.center/php/vilsnodes.php?loadranging=1&project_id=1')
    str1 = response.text.split('Tag1307')
    str2= str1[1].split('"')
    str3= str2[5].split('\\')
    print(int(str3[0]))
    a.append(int(str3[0]))
    d1307=int(str3[0])
    '''

    d1307=int(random.randint(100,700))
    return d1307
    