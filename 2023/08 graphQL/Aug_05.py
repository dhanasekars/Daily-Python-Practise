""" 
Created on : 05/08/23 1:20 pm
@author : ds  
"""
birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'}


print('Welcome to the birthday dictionary. We know the birthdays of:')
for name in birthdays:
    print(name)

choice = input("\nWho's birthday do you want to look up?").strip()
if choice in birthdays:
    print(f"The birthday of {choice} is {birthdays[choice]}")
else:
    print(f"We don't have birthday of {choice}")