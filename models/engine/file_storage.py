#!/usr/bin/python3
"""class file storage"""


import json
from models.base_model import BaseModel


class FileStorage:
    """A class that serializes instances to a JSON file and deserializes"""
    """JSON file to instances"""
    def __init__(self):
        """Initialize the FileStorage instance with private attributes"""
        self.__file_path ="file.json"
        self.__objects = {}
    def all(self):
        """Return a dictionary containing all stored objects"""
        return self.__objects
    def new(self, obj):
        """Add a new object to the storage
        Args:
            Obj: object to be added
        """
        cls_name = obj.__class__.__name__
        self.__objects[f"{cls_name}.{obj.id}"] = obj
    def save(self):
        """Convert object to JSON file"""
        newDict = {}
        for key, val in self.__objects.items():
            newDict[key] = val.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(newDict, file)
    def reload(self):
        """Deserialize json file to dictionary"""
        userClass = {'BaseModel':BaseModel}
        try:
            with open(self.__file_path, 'r') as file:
                loaded_data = json.load(file)
                for key, val in loaded_data.items():
                    cls_name, obj_id = key.split(".")
                    self.__objects[key] = globals()[cls_name](**val)
        except FileNotFoundError:
            pass