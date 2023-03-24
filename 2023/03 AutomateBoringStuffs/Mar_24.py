""" 
Created on : 24/03/23 12:59 pm
@author : ds  
"""

from bs4 import BeautifulSoup
import requests

url = 'https://www.dhanasekars.com'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}

response = requests.get(url=url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title')
    print(title.text)
else:
    print('Server down')