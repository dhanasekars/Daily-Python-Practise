""" 
Created on : 20/10/22 6:43 AM
@author : ds  
"""
data = ({
    "workshop": {
      "bedsheets": "2000",
      "working": "v0g89t7t",
      "pen": "370",
      "movies": "wo1a3d5d",
    },
  }, {
    "workshop": {
      "bedsheets": 2000,
      "pen": 370
      }
  })


def find_and_remove(dct):
    return {"workshop": {k: int(v) for k, v in dct[0]['workshop'].items() if k in dct[1]['workshop'].keys()}}


print(find_and_remove(data))