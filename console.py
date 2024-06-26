#!/usr/bin/python3
"""
This module allocates a command-line interface
for interacting with an AirBnB clone.
"""
import cmd
import json
from models import storage
from models.state import State
from models.city import City
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.user import User
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    class_map = storage.class_map

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

        class_name = arg.split()[0]
        if class_name not in self.class_map:
            print("** class doesn't exist **")
            return

        new_instance = self.class_map[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        try:
            args = arg.split()
            if not args:
                raise SyntaxError()

            class_name = args[0]
            instance_id = args[1]

            if class_name not in self.class_map:
                raise NameError()

            if len(args) < 2:
                raise IndexError()


            # Retrieve the instance from storage
            objects = storage.all()
            key = class_name + '.' + instance_id

            if key in objects:
                print("Instance found in storage:", objects[key].__str__())
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
        try:
            args = arg.split()
            if not args:
                raise SyntaxError()

            class_name = args[0]
            if class_name not in self.class_map:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            instance_id = args[1]
            objects = storage.all()

            key = class_name + '.' + instance_id
            if key in objects:
                del objects[key]
                storage.save()
            else:
                raise  KeyError()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        if not arg:
            instances = storage.all()
            print([instances[k].__str__() for k in instances])
            return
        try:
            class_name = arg.split()[0]
            if class_name not in self.class_map:
                raise NameError("** class doesn't exist **")

            instances = storage.all(self.class_map[class_name])
            print([instances[k].__str__() for k in instances])
            
        except (NameError) as e:
            print(e)

    def default(self, arg):
        """
        Executes when the command entered by the user is not recognized by
        the user is not recognized by the interpreter.

        Args (str): The command entered by the user.
        """
        args = arg.split('.')
        if len(args) >= 2:
            if args[1].startswith("show(") and args[1].endswith(")"):
                # Extract the instance ID from the command
                instance_id = args[1][5:-1]
                # Call do_show method with class name and instance ID
                self.do_show(args[0] + " " + instance_id)
            elif args[1] == "count()":
                self.do_count(args[0])
            elif args[1] == "all()":
                self.do_all(args[0])
            elif args[1].startswith("destroy(") and args[1].endswith(")"):
                # Extract the instance ID from the command
                instance_id = args[1][8:-1]
                # Call do_destroy method with class name and instance ID
                self.do_destroy(args[0] + " " + instance_id)
            elif  args[1].startswith("update(") and args[1].endswith(")"):
                # Extract the instance ID, attribute name, and attribute value from the command
                params = args[1][7:-1].split(', ')
                instance_id = params[0]
                attribute_name = params[1]
                attribute_value = params[2]
                # Call do_update method with class name, instance ID, attribute name, and attribute value
                self.do_update(args[0] + " " + instance_id + " " + attribute_name + " " + attribute_value)
        else:
            super().default(arg)

    def do_count(self, arg):
        """Retrieves the number of instances of a class.

        Args:
            arg (str): The command entered by the user, which should be in the format
                    '<class name>.count()'.
        """
        try:
            class_name = arg.split()[0]
            if class_name not in self.class_map:
                raise NameError("** class doesn't exist **")
            instances = storage.all(self.class_map[class_name])
            print(len(instances))
        except (NameError, SyntaxError) as e:
            print(e)

    def do_update(self, arg):
         """Updates an instance based on the class name and id"""
         try:
             args = arg.split()
             if not args:
                 raise SyntaxError()

             class_name = args[0]
             if class_name not in self.class_map:
                 raise NameError()

             if len(args) < 2:
                 raise IndexError()
             objects = storage.all()

             instance_id = args[1]
             key = class_name + '.' + instance_id

             if key not in objects:
                 raise KeyError()

             if len(args) < 3:
                 raise AttributeError()
             if len(args) < 4:
                 raise ValueError()

             attribute_name = objects[key]
             try:
                 attribute_name.__dict__[args[2]] = eval(args[3])
             except Exception:
                 attribute_name.__dict__[args[2]] = args[3]
                 attribute_name.save()
         except SyntaxError:
             print("** class name missing **")
         except NameError:
             print("** class doesn't exist **")
         except IndexError:
             print("** instance id missing **")
         except KeyError:
             print("** no instance found **")
         except AttributeError:
             print("** attribute name missing **")
         except ValueError:
             print("** value missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
