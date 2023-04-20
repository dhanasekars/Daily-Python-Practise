""" 
Created on : 20/04/23 3:18 pm
@author : ds  
"""
import urllib.request, base64

request = urllib.request.Request('http://www.pythonchallenge.com/pc/hex/unreal.jpg')
cred = base64.b64encode(b"butter:fly")
request.add_header("Authorization", "Basic %s" % cred.decode())
print(request.headers)
# {'Authorization': 'Basic YnV0dGVyOmZseQ=='}

response = urllib.request.urlopen(request)
print(response.headers)