#!/usr/bin/python3
"""[summary]
    """
# task 5 imcompleta
import json


class FileStorage:
    """[summary]
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """[summary]
        """
        return FileStorage.__objects

    def new(self, obj):
        """[summary]
        Args:
            obj ([type]): [description]
        """
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """[summary]
        """

    def reload(self):
        """[summary]
        """
        
            
