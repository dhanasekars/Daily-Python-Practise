""" 
Created on : 07/03/23 5:34 AM
@author : ds  
"""
import requests
from config import GoldRates
from datetime import datetime


def gold_rate():
    """
    Get gold rate from Rapid API
    :return: a tuple ('₹ 5,502', '₹ 5,240') (Pure Gold (24 K) (1 gram), Standard Gold (22 K) (1 gram))
    """

    url = "https://gold-rates-india.p.rapidapi.com/Gold-City/"
    querystring = {"city": "coimbatore"}
    date = datetime.today().strftime('%d-%b-%Y')

    try:
        output = requests.request("GET", url, headers=GoldRates.headers, params=querystring).json()
        k22 = int(output["result"][0]["Today"].strip()[2:].replace(',', ''))
        k24 = int(output["result"][2]["Today"].strip()[2:].replace(',', ''))
    except Exception as e:
        print(e)
    else:
        return [[date], [k22], [k24]]


if __name__ == "__main__":
    print(gold_rate())

# Sample response
# {'result':
# 	 [{'type': ' Standard Gold (22 K) (1 gram)', 'Today': '₹ 5,240', 'Yesterday': '₹ 5,243', 'Change': ' ₹ -3 ↓'},
# 	  {'type': ' Standard Gold (22 K) (8 grams)', 'Today': '₹ 41,920', 'Yesterday': '₹ 41,944', 'Change': ' ₹ -24 ↓'},
# 	  {'type': ' Pure Gold (24 K) (1 gram)', 'Today': '₹ 5,502', 'Yesterday': '₹ 5,505', 'Change': ' ₹ -3 ↓'},
# 	  {'type': ' Pure Gold (24 K) (8 grams)', 'Today': '₹ 44,016', 'Yesterday': '₹ 44,040', 'Change': ' ₹ -24 ↓'}]}
