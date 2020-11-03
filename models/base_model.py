#!/usr/bin/python3
"""class BaseModel"""
import uuid
from datetime import datetime
from models import storage

class BaseModel:
    """New instance BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """Method constructor initialize an instance
        """
        if kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            else:
                self.id = str(uuid.uuid4())
            if "craeted_at" in kwargs:
                self.created_at = datetime.datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
                )
            else:
                self.created_at = datetime.datetime.now()
            if "updated_at" in kwargs:
                self.updated_at = datetime.datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                )
            else:
                self.updated_at = datetime.datetime.now()
            for key, value in kwargs.items():
                if key in ["id", "created_at", "updated_at", "__class__"]:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)

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
