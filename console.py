#!/usr/bin/python3
"""
Command line interpreter (CLI) using the CMD module.
"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """
    Command-line interpreter for the HBNB application.

    Attributes:
        prompt (str): The prompt string displayed to the user.

    Methods:
        do_quit(arg):   Handles the 'quit' command to exit the program.
        emptyline():    Does nothing when an
                        empty line + ENTER shouldn’t execute anything
        do_EOF(arg):    Handles the end-of-file condition to gracefully
                        exit the program.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
         Quit command to exit the program.

        Args:
            arg:    Unused argument (required by cmd.Cmd).

        Returns:
            None

        Raises:
            SystemExit:     Exits the program with a status code of 0.
        """
        sys.exit()

    def emptyline(self):
        """
        Does nothing when an empty line + ENTER shouldn’t execute anything
        """
        pass

    def do_EOF(self, arg):
        """
        Handles end-of-file (EOF) to gracefully exit the program.

        Args:
            arg: Unused argument (required by cmd.Cmd).

        Returns:
            bool: True to indicate the end-of-file condition.

        Notes:
            Typing CTRL+D (UNIX-like systems) triggers EOF.
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
