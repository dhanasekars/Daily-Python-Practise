""" 
Created on : 27/04/23 10:35 am
@author : ds  
"""
from github import Github
from config import GitHubDetails
import os

g = Github(GitHubDetails.access_token)
user = g.get_user().name
print(user)
os.chdir(GitHubDetails.second_brain)
os.system("git add .")
commit_message = "weekly commit"
os.system(f"git commit -m '{commit_message}'")
remote_url = f"git@github.com: dhanasekars/secondbrain.git"
os.system("git push -u origin main")

