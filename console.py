#!/usr/bin/python3
"""
This module provides a command-line interface
for interacting with an AirBnB clone.
"""
import cmd
from models.base_model import BaseModel
import json


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Handle end-of-file"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

    def do_help(self, arg):
        """Get help on commands"""
        if arg:
            super().do_help(arg)

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file"""
        if not arg:
            print("** class name missing **")
            return

        # Map class names to their corresponding Python class
        class_mapping = {
                'BaselModel': BaseModel
                }

        class_name = arg.split()[0]
        if class_name not in class_mapping:
            print("** class doesn't exist **")
            return

        new_instance = class_mapping[class_name]()
        new_instance.save()
        print(new_instance.id)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
