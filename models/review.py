#!/usr/bin/python3
"""[summary]
    """
# task 9
from models.base_model import BaseModel


class Review(BaseModel):
    """[summary]

    Args:
        BaseModel ([type]): [description]
    """
    place_id = ""
    user_id = ""
    text = ""
    