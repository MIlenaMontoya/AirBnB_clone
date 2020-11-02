#!/usr/bin/python3
"""[summary]
    """
# task 8 
from models.base_model import BaseModel


class User(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
