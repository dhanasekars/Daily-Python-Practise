""" 
Created on : 28/03/23 6:24 am
@author : ds  
"""

import validators
from fastapi import FastAPI, HTTPException
import schemas

app = FastAPI()

def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)
@app.get("/")
def read_root():
    return "Welcome to the URL Shortener API"

@app.post("/url")
def create_url(url: schemas.URLBase):
    if not validators.url(url.target_url):
        raise_bad_request(message="Your URL is not valid")
    return f"TODO: create database entry for {url.target_url}"
