""" 
Created on : 15/09/22 6:43 PM
@author : ds  
"""
test_data = {"name": "Max", "notes": [1, 4, 6]}


def top_note(student):
    if list(student.keys())[0] == 'name':
        new_dict = {"name": student["name"], "top_note": max(student["notes"])}
    else:
        new_dict = {"top_note": max(student["notes"]), "name": student["name"] }
    return new_dict


print(top_note(test_data))