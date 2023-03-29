""" 
Created on : 29/03/23 1:16 pm
@author : ds  
"""
from pydantic import BaseModel


class URLBase(BaseModel):
    target_url: str

class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        orm_mode = True

class URLInfo(URL):
    url: str
    admin_url: str

