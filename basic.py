
import json
import requests

#file read/write
f=open("D:\\bin\\xx.json",'r')
y = json.loads(f.read())
x=open("D:\\bin\\xx.json","w")
json.dump(y,x,indent=4)


#http module
dta= requests.get('https://jsonplaceholder.typicode.com/todos/1' )   
print(dta.content)



#foreach loop and conditions 

for val in y['children']:
    print(val['firstName'])
