    
import requests
import json
import base64

f=open('sample.zip','rb')
print(base64.b64encode(f.read()).decode('utf-8'))
base64.b64encode().decode('utf-8')
querystring = {"consumerToken": 'eb36c032-ade2-4dc6-acdf-d38e6e990afcrrr',
                   "employeeToken": '072cc0df-216d-4808-991f-e74cbb34889c',
                   "expirationDate": "2025-01-01"}
url = "https://api.tripletex.io/v2/token/session/:create"
response = requests.request("PUT", url, params=querystring)
print(response.text)
session_token = json.loads(response.text)['value']['token']
username_and_pass = str.encode("0:{}".format(session_token))  # make byte like
print( base64.b64encode(username_and_pass).decode('utf-8'))