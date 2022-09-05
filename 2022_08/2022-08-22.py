""" 
Created on : 22/08/22 6:21 PM
@author : ds  
"""


def validate(code):
    if "def" not in code:
        return "missing def"
    if ":" not in code:
        return "missing :"
    if "(" and ")" not in code:
        return "missing paren"
    if "(" + ")" in code:
        return "missing param"
    if "    " not in code:
        return "missing indent"
    if "validate" not in code:
        return "wrong name"
    if "return" not in code:
        return "missing return"
    else:
        return True



print(validate('def validate(code):\n if "def" not in code:\n return "missing def"\n if ":" not in code:\n return "missing :"\n if "(" not in code:\n return "missing paren"\n if ")" not in code:\n return "missing paren"\n if "()" in code:\n return "missing param"\n if " " not in code:\n return "missing indent"\n if "validate" not in code:\n return "wrong name"\n if "return" not in code:\n return "missing return"\n else:\n return True'))