#!/usr/bin/python3
""" BaseModel that defines all common attributes/methods for other classes: """
from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """
    A class of the base model
    """
    def __init__(self, *args, **kwargs):
        """
        initialization of the baseModel
        you will use *args,
        **kwargs arguments for the constructor of a BaseModel
        """
        if kwargs:
            for key, values in kwargs.items():
                if key in ["id", "created_at", "updated_at"]:
                    if key == "created_at" or key == "updated_at":
                        dtime_obj = datetime.strptime(values, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, key, dtime_obj)
                    else:
                        setattr(self, key, values)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        string representation of the object
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        return dict_obj
