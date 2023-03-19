""" 
Created on : 19/03/23 2:15 pm
@author : ds  
"""

from sympy import *
from IPython.display import display
x = symbols('x')
pprint(diff(x**5 - 2*x**4 + 2), use_unicode=False)
pprint(Integral(sqrt(1/x), x), use_unicode=False)
#
# display(fun)
# display(Matrix([[1, -1], [3, 4], [0, 2]]))
#
# display(simplify(fun))
#
