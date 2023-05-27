import requests
def angle1225():

    response = requests.get('https://norgay.center/php/vilsnodes.php?loadranging=1&project_id=1')
    str1 = response.text.split('Tag1225')
    str2= str1[1].split('"')
    str3= str2[9].split('\\')
    a1225=float(str3[0])
    #print(a1196)
    
    return a1225