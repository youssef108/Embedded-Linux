import requests

url = 'https://www.boredapi.com/api/activity'
url2='https://api.ipify.org/?format=json'
url3='https://ipinfo.io/<192.168.56.1>/geo'

while True:
    p=input("press b to suggest an activity\npress i to get ip\npress g to get location\nChoice: ")
    if(p=='b'):
        response = requests.get(url)
    
    # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            print(data["activity"])
    elif(p=='i'):
        response = requests.get(url2)
    
    
        if response.status_code == 200:
            data = response.json()
            print("IP: ",data["ip"])
    elif(p=='g'):                #website not working
        response = requests.get(url3)
    
    
        if response.status_code == 200:
            data = response.json()
            print(data)
        


    
