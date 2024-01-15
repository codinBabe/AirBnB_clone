#!/usr/bin/python3
"""class filestorage"""


import json
from models.base_model import BaseModel


class FileStorage:
    """
    A class that serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):

        """Return a dictionary containing all stored objects"""
        return self.__objects

    def new(self, obj):

        """Add a new object to the storage
        Args:
            Obj: object to be added
        """

        keyF = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[keyF] = obj

    def save(self):

        """Convert object to JSON file"""
        newObj = {}
        for key, val in self.__objects.items():
            newObj[key] = val.to_dict()
            with open(self.__file_path, 'w', encoding='utf8') as file:
                json.dump(newObj, file)

    def reload(self):

        """Deserialize json file to dictionary"""
        userClass = {'BaseModel': BaseModel}
        try:
            with open(self.__file_path, 'r', encoding='utf8') as jsonString:
                loaded_data = json.load(jsonString)
                for objVal in loaded_data.values():
                    clsName = objVal["__class__"]
                    clsObj = userClass[clsName]
                    self.new(clsObj(**objVal))
        except FileNotFoundError:
            pass
