"""
Created by: DS
Created at: 2023-06-19 10:45:57

This script is to fetch explore parsing markdown files
"""


import glob
import os

folder_path_1 = '/Users/ds/Library/Mobile Documents/com~apple~CloudDocs/Second Brain/500 Publish'
folder_path_2 = '/Users/ds/Library/Mobile Documents/com~apple~CloudDocs/Second Brain/'

if os.path.exists(folder_path_1) and os.path.isdir(folder_path_1):
    print("YES")
    md_files = glob.glob(folder_path_1 + '/*.md')
    total = len(md_files)
    print(f"Total md files in the given path {folder_path_1} is {total}")
else:
    print("invalid folder path")

count = 0
if os.path.exists(folder_path_2) and os.path.isdir(folder_path_2):
    for root, dirs, files in os.walk(folder_path_2):
        dirs[:] = [ d for d in dirs if not d.startswith(".")]
        # for dir in dirs:
        #     print(dir)
        for file in files:
            if file.endswith('.md'):
                count += 1
    print(f"Total md files in the given path including sub folders {folder_path_2} is {count}")

if os.path.exists(folder_path_2) and os.path.isdir(folder_path_2):
    md_files = glob.glob(folder_path_2  + '/**/*.md', recursive=True)
    print(f"Total md files in the given path including sub folders {folder_path_2} is {len(md_files)}")
