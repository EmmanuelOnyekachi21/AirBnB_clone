#!/usr/bin/python3
"""
Command line interpreter (CLI) using the CMD module.
"""

import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """
    Contain the entry point of the command interpreter.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        sys.exit()

    def emptyline(self):
        """Does nothing when an empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_EOF(self, arg):
        """Handles end-of-file (EOF).
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
