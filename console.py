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
    __classes = {
            "BaseModel"
            }

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
        elif arg == "update":
            print("Updates an instance based on the class name and id")
            print("Usage: update <class name> <id> <attribute name> \"<attribute value>\"")
            print("Example: update BaseModel 1234-1234-1234 email \"aibnb@mail.com\"")
            print("Note: Only one attribute can be updated at a time")
            print("      id, created_at, and updated_at cannot be updated")
            print("      Only simple attributes can be updated: string, integer, and float")
        else:
            super().do_help(arg)

    def do_create(self, arg):
        """Create a new instance of BaseModel and save it to the JSON file"""
        if not arg:
            print("** class name missing **")
            return

        # Map class names to their corresponding Python class
        class_mapping = {
                "BaseModel": BaseModel
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
        try:
            args = arg.split()
            if not args:
                raise SyntaxError()

            class_name = args[0]
            if class_name not in self.__classes:
                raise NameError()

            if len(args) < 2:
                raise IndexError()

            instance_id = args[1]
            key = class_name + '.' + instance_id
            if key not in storage.all():
                print(storage.all()[key])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

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
            print(instances)
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

    def do_update(self, arg):
         """Updates an instance based on the class name and id"""
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

         if len(args) < 3:
             print("** attribute name missing **")
             return

         attribute_name = args[2]
         if len(args) < 4:
             print("** value missing **")
             return

         attribute_value_str = args[3]

         # Get the instance from storage
         instance = storage.all()[key]

         # Only simple attributes can be updated: string, integer, and float
         if hasattr(instance, attribute_name):
             # Get the attribute type
             attribute_type = type(getattr(instance, attribute_name))

             # Cast attribute value to the attribute type
             try:
                 attribute_value = attribute_type(attribute_value_str)
             except ValueError:
                 print("** value missing **")
                 return

             # Update the attribute
             setattr(instance, attribute_name, attribute_value)

             # Save the change into the JSON file
             storage.save()
         else:
             print("** attribute name doesn't exist **")



if __name__ == '__main__':
    HBNBCommand().cmdloop()
