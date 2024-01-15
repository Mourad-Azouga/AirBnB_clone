#!/usr/bin/python3
"""user class, subclass of BaseModel
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """This is a user class that inherits from Basemodel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""