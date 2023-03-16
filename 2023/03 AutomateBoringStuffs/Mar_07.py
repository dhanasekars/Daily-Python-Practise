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

    url = "https://gold-silver-live-prices.p.rapidapi.com/getGoldRate"
    querystring = {"place": "coimbatore"}
    date = datetime.today().strftime('%d-%b-%Y')

    try:
        output = requests.request("GET", url, headers=GoldRates.headers, params=querystring).json()
        k22 = int(output["variations per 10g"]["Gold 22 Karat (Rs ₹)"].replace(',', '')) / 10
        k24 = int(output["variations per 10g"]["Gold 24 Karat (Rs ₹)"].replace(',', '')) / 10

    except Exception as e:
        print(e)
    else:
        return [[date], [k22], [k24]]


if __name__ == "__main__":
    print(gold_rate())


# {
#   "location": "COIMBATORE",
#   "variations per 10g": {
#     "Gold 24 Karat (Rs ₹)": "57,690",
#     "Gold 22 Karat (Rs ₹)": "52,883",
#     "Gold 20 Karat (Rs ₹)": "48,075",
#     "Gold 18 Karat (Rs ₹)": "43,268",
#     "Gold 16 Karat (Rs ₹)": "38,460",
#     "Gold 14 Karat (Rs ₹)": "33,653",
#     "Gold 12 Karat (Rs ₹)": "28,845",
#     "Gold 10 Karat (Rs ₹)": "24,038"
#   },
#   "GOLD": {
#     "price": "57,690.00",
#     "change": "-70.00 (-0.120%)",
#     "per value": "Rs ₹ / 10gm"
#   }
# }