""" 
Created on : 25/09/22 5:34 AM
@author : ds  
"""

test_data = {
    "Phrase4": "COVID-19 is no good",
    "Phrase1": "COVID-19 is no good",
    "Phrase2": "COVID-18 is no good",
    "Phrase3": "COVID-17 is no good"
}
phrase = "COVID-19"


def find_pattern(dict_, p):
    lst = []
    flag = True
    for key, sentence in dict_.items():
        for word in sentence.split():
            if word == p:
                flag = False
                lst.append('%s = %s' % (key, p))
                # lst.append(f"{key} = {p}")
                break
            else:
                flag = True
        if flag:
            lst.append("%s = %s" % (key, 'None'))
            # lst.append(f"{key} = None")
    return lst


print(find_pattern(test_data, phrase))
