""" 
Created on : 01/04/23 2:48 pm
@author : ds  
"""

# http://www.pythonchallenge.com/pc/def/0.html
# replace 0 with pow(2, 38)
# http://www.pythonchallenge.com/pc/def/274877906944.html

# print(2**38)

public_key = "abcdefghijklmnopqrstuvwxyz"
private_key = "cdefghijklmnopqrstuvwxyzab"

encryption = dict(zip(list(public_key), list(private_key)))
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. " \
       "bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. " \
       "sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

decoded_text = ""
for char in text:
    if char in encryption:
        decoded_text += encryption[char]
    else:
        decoded_text = decoded_text + char

# print(decoded_text)

#  The encoded text recommends using string.maketrans

result = str.maketrans(public_key, private_key)
print(text.translate(result))

# so the answer is replace map with ocr in the url