#!/usr/bin/python3
""" contain class inherit from basemodel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ class definition of the review """
    def __init__(self, *args, **kwargs):
        self.place_id = ""
        self.user_id = ""
        self.text = ""
