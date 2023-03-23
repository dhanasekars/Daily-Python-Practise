""" 
Created on : 23/03/23 9:37 am
@author : ds  
"""

import requests

test_url = ['https://www.dhanasekars.com', 'https://notes.dhanasekars.com']
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}

def daily_website_check(urls):
    for url in urls:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            print(f'{url} is up and running. \n')
        else:
            print(f'Not 200. Received ' + str(response.status_code) + f' for {url} \n')

daily_website_check(test_url)