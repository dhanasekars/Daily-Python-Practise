""" 
Created on : 06/04/23 7:30 am
@author : ds  
"""
import zipfile
import re

# http://www.pythonchallenge.com/pc/def/channel.html
# This is a zip image - may need to use zip


f = zipfile.ZipFile("channel.zip")

num = '90052'
comments = []

while True:
    content = f.read("90052.txt").decode("utf-8")
    comments.append(f.getinfo(num + ".txt").comment.decode("utf-8"))
    print(content)
    pattern = r"Next nothing is \d+"
    match = re.search(pattern, content)
    if match is None:
        break
    num = match.group(1)

print("".join(comments))
#
# def zip_decoding(num):
#     file_path = f'./06_zip/{num}.txt'
#     with open(file_path, 'r') as file:
#         r = file.read()
#     comments.append(f.getinfo(str(num) + ".txt").comment.decode("utf-8"))
#     pattern = r"Next nothing is \d+"
#     match = re.search(pattern, r)
#     next_nothing = r.split()[-1]
#     if match:
#         print(f"match found : {r}")
#         print(next_nothing)
#         zip_decoding(next_nothing)
#     else:
#         print(f"match not found : {r}")
#     print("".join(comments))


# zip_decoding(90052)
# # zip_decoding(94191)
