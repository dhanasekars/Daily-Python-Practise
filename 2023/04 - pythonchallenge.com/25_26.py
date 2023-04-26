""" 
Created on : 26/04/23 11:13 am
@author : ds  
"""
from PIL import Image
import wave

wavs = [wave.open("wave/wave%d.wav" % i) for i in range(1, 26)]
result = Image.new('RGB', (300,300), 0)
num_frames = wavs[0].getnframes()
for i in range(len(wavs)):
    byte = wavs[i].readframes(num_frames)
    img = Image.frombytes('RGB', (60, 60), byte)
    result.paste(img, (60 * (i % 5), 60 * (i // 5)))
result.save('level25.png')


# Level 26

# http://www.pythonchallenge.com/pc/hex/decent.html

import hashlib

def search_and_save():
    for i in range(len(data)):
        for j in range(256):
            newData = data[:i] + bytes([j]) + data[i + 1:]
            if hashlib.md5(newData).hexdigest() == md5code:
                open('repaired.zip', 'wb').write(newData)
                return

md5code = 'bbb8b499a0eef99b52c7f13f4e78c24b'
data = open('maze/mybroken.zip', 'rb').read()
search_and_save()


# Level 27

# http://www.pythonchallenge.com/pc/hex/speedboat.html

