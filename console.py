"""
This module provides a command-line interface
for interacting with an AirBnB clone.
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, arg):
        """Handle end-of-file"""
        return True

    def do_quit(self, arg):
        """Exit the program."""
        return True

    def emptyline(self):
        pass

    def default(self, line):
        if not line:
            return self.emptyline()
        else:
            print(f"Command '{line}' not recognized")


if __name__ == '__main__':

    HBNBCommand().cmdloop()
