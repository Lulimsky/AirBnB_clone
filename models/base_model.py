#!/usr/bin/env python3

""" Creation of class base_model """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ BaseModel defines all common attributes/methods for other classes """

    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance.
        Args:
            - *args: list of arguments
            - **kwargs: dict of key-values arguments
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    self.created_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                elif key == 'updated_at':
                    self.updated_at = datetime.strptime(value,
                                                        '%Y-%m-%dT%H:%M:%S.%f')
                else:
                    if key != "__class__":
                        setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """ Save the object into .json file and updates the attribute
        'updated_at' with current time"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary with keys/values of __dict__
        of the instance
        """
        new_dict = dict(self.__dict__)
        new_dict["created_at"] = self.created_at.isoformat(sep='T')
        new_dict["updated_at"] = self.updated_at.isoformat(sep='T')
        new_dict["__class__"] = self.__class__.__name__
        return new_dict

    def __str__(self):
        """Return the instance's ID, class name, and attributes as a string"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)
