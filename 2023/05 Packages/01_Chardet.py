""" 
Created on : 21/04/23 3:02 pm
@author : ds  
"""
import chardet
import urllib.request
from chardet.universaldetector import UniversalDetector

# helps to find the encoding type used

rawdata = urllib.request.urlopen('http://mixi.jp')
detector = UniversalDetector()
for line in rawdata.readlines():
    detector.feed(line)
    if detector.done:
        break
detector.close()
rawdata.close()
print(detector.result)

# https://chardet.readthedocs.io/en/latest/index.html