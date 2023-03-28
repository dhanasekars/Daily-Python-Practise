""" 
Created on : 28/03/23 6:24 am
@author : ds  
"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return "Welcome to the URL Shortener API"
