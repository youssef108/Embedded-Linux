import os

#check if an envirnment variable exists
if 'HOME' in os.environ:
    print("HOME variable exists!")
#list all envirnment variables
for key, value in os.environ.items():
    print(f"{key}: {value}")
#set an envirnment variable
os.environ['MY_VARIABLE'] = 'Some Value'
