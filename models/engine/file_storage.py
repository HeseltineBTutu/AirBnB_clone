import json
import os
import importlib

class FileStorage:
    """
    FileStorage class serializes instances to a JSON file and deserializes
    JSON file to instances.
    """

    __file_path = "file.json"
    __objects = {}  # Dictionary to store objects

    def all(self):
        """
        Returns the dictionary __objects.
        """
        if not FileStorage.__objects:
            return {}
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        print("Serialized objects:", serialized_objects)
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists; otherwise, do nothing).
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    module_name = f"models.base_model"
                    module = importlib.import_module(module_name)
                    cls = getattr(module, class_name)

                    # Add new objects from the JSON file if they do not already exist
                    if key not in FileStorage.__objects:
                        obj_instance = cls(**value)
                        FileStorage.__objects[key] = obj_instance
