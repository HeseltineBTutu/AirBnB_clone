#!/usr/bin/python3
"""
This module provides a command-line interface
for interacting with an AirBnB clone.
"""
import cmd
from models.base_model import BaseModel
import json
from models import storage

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
        if arg == "show":
            print("Prints the string representation of an instance")
            print("Usage: show <class name> <id>")
            print("Example: show BaseModel 1234-1234-1234")
        elif arg == "create":
            print("Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id")
            print("Usage: create <class name>")
            print("Example: create BaseModel")
        elif arg == "destroy":
            print("Deletes an instance based on the class name and id")
            print("Usage: destroy <class name> <id>")
            print("Example: destroy BaseModel 1234-1234-1234")
        elif arg == "all":
            print("Prints all string representation of all instances")
            print("Usage: all BaseModel or all")
            print("Example: all BaseModel or all")
        else:
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

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in [key.split('.')[0] for key in storage.all()]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in [key.split('.')[0] for key in storage.all()]:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        key = class_name + '.' + instance_id
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            # If no class name provided, print all instances
            instances = storage.all().values()
        else:
            class_name = arg
            if class_name not in [key.split('.')[0] for key in storage.all()]:
                print("** class doesn't exist **")
                return
            # Filter instances by class name
            instances = [instance for instance in storage.all().values()
                    if instance.__class__.__name__ == class_name]

            # Print string representation of all instances
            print([str(instance) for instance in instances])



if __name__ == '__main__':
    HBNBCommand().cmdloop()
