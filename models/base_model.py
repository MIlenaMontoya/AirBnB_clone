#!/usr/bin/python3
"""[summary]
    """
# task 3, 4
import uuid
from datetime import datetime

class BaseModel:
    """[summary]
    """

    def __init__(self, *args, **kwargs):
        """[summary]
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
        """[summary]
        """

    def save(self):
        """docstring
        """
    def to_dict(self):
        """[summary]
        """
    