import requests

#BASE = "http://localhost:5000/"
BASE = " http://127.0.0.1:5000/"

#To run this, you need to type following in  terminal: 
#  python test.py

data = [
    {"likes": 10, "name": "Martin", "views":100},
    {"likes": 20, "name": "Ken", "views":200},
    {"likes": 30, "name": "Simon", "views":300}
]

#PUT
for i in range(len(data)):
    response = requests.put(BASE+ "video/"+str(i), data[i])
    print(response.json())


input()

#PATCH
response = requests.patch(BASE+ "video/2", {"views":99} )
print(response.json())

input()

# #DELTE
# response = requests.delete(BASE+"video/0")
# print(response.json())

# input()

#GET
response = requests.get(BASE+ "video/2")
print(response.json())

