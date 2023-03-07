""" 
Created on : 07/03/23 5:34 AM
@author : ds  
"""
import requests
from config import GoldRates

def gold_rate():
    """
    Get gold rate from Rapid API
    :return: a tuple ('₹ 5,502', '₹ 5,240') (Pure Gold (24 K) (1 gram), Standard Gold (22 K) (1 gram))
    """

    url = "https://gold-rates-india.p.rapidapi.com/Gold-City/"
    querystring = {"city": "coimbatore"}
    output = requests.request("GET", url, headers=GoldRates.headers, params=querystring).json()
    return output["result"][2]["Today"], output["result"][0]["Today"]


if __name__ == "__main__":
    print(gold_rate())


# Response sample
# {'result':
# 	 [{'type': ' Standard Gold (22 K) (1 gram)', 'Today': '₹ 5,240', 'Yesterday': '₹ 5,243', 'Change': ' ₹ -3 ↓'},
# 	  {'type': ' Standard Gold (22 K) (8 grams)', 'Today': '₹ 41,920', 'Yesterday': '₹ 41,944', 'Change': ' ₹ -24 ↓'},
# 	  {'type': ' Pure Gold (24 K) (1 gram)', 'Today': '₹ 5,502', 'Yesterday': '₹ 5,505', 'Change': ' ₹ -3 ↓'},
# 	  {'type': ' Pure Gold (24 K) (8 grams)', 'Today': '₹ 44,016', 'Yesterday': '₹ 44,040', 'Change': ' ₹ -24 ↓'}]}
