"""
BaseModel module provides a base model for other classes.
It includes common functionality such as ID generation,
creation and update timestamps, string representation,
and dictionary conversion.

Classes:
    BaseModel: Represents a base model with common functionality.

Usage:
    # Example usage of the BaseModel class
    obj = BaseModel()
    print(obj.to_dict())
"""

from datetime import datetime
import uuid


class BaseModel:
    """
    BaseModel class represents a base model for other classes.
    It provides common functionality such as ID generation,
    creation and update timestamps, and string representation.
    """

    def __init__(self, created_at=None, updated_at=None):
        """
        Initializes a BaseModel instance.

        :param created_at: Optional datetime object specifying the
                           creation timestamp. If not provided,
                           defaults to the current datetime.
        :param updated_at: Optional datetime object specifying the
                           last update timestamp. If not provided,
                           defaults to the current datetime.

         """
        self.id = str(uuid.uuid4())
        self.created_at = created_at if created_at else datetime.now()
        self.updated_at = updated_at if updated_at else datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        :return: String representation containing class name, ID,
                 and instance attributes.
        """
        class_name = type(self).__name__

        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates the 'updated_at' attribute with the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.

        :return: Dictionary containing all keys/values of __dict__
                 of the instance,with '__class__' key
                 added with the class name of the object, and
                 'created_at' and 'updated_at' converted to ISO
                 format strings.
        """
        # Convert 'created_at' and 'updated_at' to ISO format strings
        created_at_iso = self.created_at.isoformat()
        updated_at_iso = self.updated_at.isoformat()

        # Create dictionary representation with class name, instance
        # attributes,and timestamps
        obj_dict = {
                "__class__": type(self).__name__,
                **self.__dict__,
                "created_at": created_at_iso,
                "updated_at": updated_at_iso
                }
        return obj_dict
