#!/usr/bin/python3
<<<<<<< HEAD
from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
=======
"""Test base_model file
"""

import unittest
import pep8
import os
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Tests for the BaseModel class
    """

    def test_basemodel_pep8(self):
        """Test PEP8 style
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(["./models/base_model.py"])
        self.assertEqual(result.total_errors, 0)
>>>>>>> aca072dcd039a43b89d0543378a6695cd16ca11e
