import json
import webbrowser

with open('Python_Tasks/websites.json', 'r') as file:
    data = json.load(file)

for key,value in data.items():
    print(key," ",value)


site=input("Enter number of website you want to open ")
webbrowser.open(data[site])