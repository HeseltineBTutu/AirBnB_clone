import json
import os
import importlib
from models.user import User
"""
FileStorage module provides the FileStorage class, which serializes instances
to a JSON file and deserializes JSON file to instances.

This module contains the FileStorage class, which facilitates the storage and
retrieval of objects by serializing them to a JSON file and deserializing JSON
data back into Python objects. It offers methods for managing objects in a
persistent manner, allowing data to be saved and reloaded across program
sessions.

Classes:
    FileStorage: Class for serializing instances to a JSON file and
    deserializing JSON file to instances.

Usage:
    # Example usage of the FileStorage class
    from models.engine.file_storage import FileStorage

    # Create a FileStorage instance
    storage = FileStorage()

    # Save objects to the JSON file
    storage.save()

    # Reload objects from the JSON file
    storage.reload()

    # Access stored objects
    objects = storage.all()
"""


class FileStorage:
    """
    FileStorage class serializes instances to a JSON file and deserializes
    JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}  # Dictionary to store objects

    def all(self, cls=None):
        """
        Returns the dictionary __objects.

        Args:
            cls (str or class, optional): Class name or class itself. If provided,
                filters the dictionary to include only instances of the specified class.
                Defaults to None.

        Returns:
            dict: Dictionary of objects stored in __objects. If cls is provided,
                returns a filtered dictionary containing instances of the specified class.

        """
        if cls is not None:
            if type(cls) == str:
                cls_dict = eval(cls)
            cls_dict = {}
            for k, v in self.__objects.items():
                if type(v) == cls:
                    cls_dict[k] = v
            return cls_dict
        return self.__objects


    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (BaseModel): Instance of BaseModel or its subclasses to be
            added to __objects.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        serialized_objects = {
                key: obj.to_dict()
                for key, obj in FileStorage.__objects.items()
                }
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing).
        """
        if os.path.exists(FileStorage.__file_path) and os.path.getsize(self.__class__.__file_path) > 0:
            with open(FileStorage.__file_path, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON file: {e}")
                    return

                module_name = "models.base_model"
                module = importlib.import_module(module_name)

                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name == "User":
                        cls = User
                    else:
                        cls = getattr(module, class_name)

                    # Add new objects from the JSON file
                    # if they do not already exist
                    if key in FileStorage.__objects:
                        # Update existing object with data from JSON
                        obj_instance = FileStorage.__objects[key]
                        obj_instance.__dict__.update(value)
                    else:
                        obj_instance = cls(**value)
                        FileStorage.__objects[key] = obj_instance
        else:
            # If the file is empty or doesn't exist, clear the storage
            FileStorage.__objects.clear()
