""" 
Created on : 19/04/23 11:47 am
@author : ds  
"""

import email, base64, wave


audio = open("19_email.txt", "rb").read()
f = open("indian.wav", "wb")
f.write(audio)
w = wave.open("BadScan.wav","rb")
print(w.getframerate())
print(w.getnchannels())
print(w.getnframes())

#  Not able to solve, but learned about wave package.
# Next level http://www.pythonchallenge.com/pc/hex/idiot2.html