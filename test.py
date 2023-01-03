import requests

#BASE = "http://localhost:5000/"
BASE = " http://127.0.0.1:5000/"

#To run this, you need to type following in  terminal: 
#  python test.py
response = requests.get(BASE+ "helloworld")
print(response.json())