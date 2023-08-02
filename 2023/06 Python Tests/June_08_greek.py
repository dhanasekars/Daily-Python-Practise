""" 
Created on : 08 graphQL/06/23 4:54 am
@author : ds  
"""

import math


def sinusoid(A, ω, ϴ):
    return lambda t: A * math.sin(ω * t + ϴ)


waveform = sinusoid(1, 1, 1)
result = waveform(1)
print(result)
