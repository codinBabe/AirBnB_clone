#!/usr/bin/python3
"""class basemodel"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """class that defines all common atrribtes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.isoformat(val))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """ updates the public instance attribute updated_at"""
        """with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """method to return a dictionary containing all keys/values"""
        """of __dict__ of the instance"""
        newDict = {}
        newDict["__class__"] = self.__class__.__name__
        for key, val in self.__dict__.items():
            if isinstance(val, datetime):
                newDict[key] = val.isoformat()
            else:
                newDict[key] = val
        return newDict

    def __str__(self):
        """string represetation of base model methods"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
