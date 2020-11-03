#!/usr/bin/python3

"""AirBnB project - Base Models"""
import uuid
from datetime import datetime
import models
import copy


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

        """Print a readable sstirng
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates with the current datetime
        """
        self.update_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary with all keys/value
        of __dict__ of the instance
        """
        dictn = copy.deepcopy(self.__dict__)
        dicn['__class__'] = self.__clas__.__name__

        form = "%Y-%m-%dT%H:%M:%S.%f"
        dictn['created_at'] = self.created_at.strftime(form)
        dictn['updated_at'] = self.update_at.strftime(form)
        dictn['id'] = self.id
        return dictn
