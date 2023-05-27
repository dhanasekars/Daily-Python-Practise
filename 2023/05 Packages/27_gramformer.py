""" 
Created on : 24/05/23 1:32 pm
@author : ds
"""

import gramformer

gf = gramformer.Gramformer(models=1, use_gpu=False)
output = gf.correct(""" New Zealand is island countrys in southwestern Paciific Ocaen. Country population was 5 million """)
print(output)