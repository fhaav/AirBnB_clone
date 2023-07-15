#!/usr/bin/python3
""" Class that inherit from Basemodel """
from models.base_model import BaseModel


class City(BaseModel):
    """ class definition of City """
    state_id = ""
    name = ""
