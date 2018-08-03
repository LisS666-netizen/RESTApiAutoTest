import json
import os
from logModule import logModule
import requests
import time
data = {}
dataTemp = []
j_file = open("",'r')
data = json.load(j_file)
j_file.close() 
refreshToken = data.get("refresh_token")
#print (refreshToken)
header = {"Content-Type":"application/x-www-form-urlencoded"}
url = ""
body = "grant_type=refresh_token&refresh_token=" + refreshToken 
#print (body)
a = time.clock()
response = requests.post(url=url,headers=header,data=body)
b = time.clock()
c = b-a
print ("took " + str(c) + "seconds")
#print (response.json())
j_file = open("accesstoken",'w')
json.dump(response.json(),j_file)
j_file.close()
