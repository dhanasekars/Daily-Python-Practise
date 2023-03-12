""" 
Created on : 11/03/23 11:56 AM
@author : ds  
"""

from github import Github
from config import GitHubDetails

g = Github(GitHubDetails.access_token)
print(g.get_user().login)

for repo in g.get_user().get_repos():
    print(repo.name)

