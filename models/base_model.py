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

    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance.
        """
        # Always create the id attribute
        self.id = str(uuid.uuid4())

        if kwargs:  # Check if kwargs is not empty
            # Iterate through key-value pairs in kwargs
            for key, value in kwargs.items():
                # Skip __class__ attribute
                if key == "__class__":
                    continue
                # Convert created_at and updated_at strings to datetime objects
                if key in ["created_at", "updated_at"]:
                    if value is not None:
                        if isinstance(value, str):
                            value = datetime.strptime(
                                    value,
                                    "%Y-%m-%dT%H:%M:%S.%f"
                                    )
                setattr(self, key, value)  # Set attribute
        else:
            # If kwargs is empty, create
            # new instance with created_atand updated_at
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            # Set created_at and updated_at to
            # current datetime if None is provided
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()

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
