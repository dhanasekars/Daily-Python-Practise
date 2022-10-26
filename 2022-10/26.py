""" 
Created on : 26/10/22 6:55 AM
@author : ds  
"""

data = "2-5g-3-J"


def license_plate(s, n):
    """
    The function input consists of a string s and group length n.
    The output has to be upper case characters and digits.
    The new groups are made from right to left and connected by -.
    The original order of the dmv number is preserved.
    license_plate("5F3Z-2e-9-w", 4) ➞ "5F3Z-2E9W"
    license_plate("2-5g-3-J", 2) ➞ "2-5G-3J"
    license_plate("2-4A0r7-4k", 3) ➞ "24-A0R-74K"
    license_plate("nlj-206-fv", 3) ➞ "NL-J20-6FV"
    """
    # new string converts the string to a list and reverse it, as '-' needs to be added from right to left
    new = list((s[::-1].replace('-', "").upper()))
    # then every nth character is added with '-' then joined to form a string
    return "".join([c if e % n != 0 else c+"-" for e, c in enumerate(new, start=1)])[::-1].strip("-")


print(license_plate(data, 2))
