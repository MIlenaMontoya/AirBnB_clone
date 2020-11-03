#!/usr/bin/python3
"""class BaseModel"""
# task 3, 4
import uuid
from datetime import datetime


class BaseModel:
    """New instance BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """Method constructor initialize an instance
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

        if kwargs:
            form = "%Y-%m-%dT%H:%M:%S.%f"
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                    continue
                if key == "created_at":
                    self.created_at = datetime.strptime(value, form)
                    continue
                if key == "update_at":
                    self.update_at = datetime.strptime(value, form)
                    continue
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """representation of an object
        """
        printable_str = "[{}] ({}) {}".format(
            type(self).__name__, self.id, str(self.__dict__)
        )
        return printable_str

    def save(self):
        """Instance public update the datetime
        """
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Instance public create a dict
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = type(self).__name__
        new_dict["updated_at"] = new_dict["updated_at"].isoformat()
        new_dict["created_at"] = new_dict["created_at"].isoformat()
        return new_dict
