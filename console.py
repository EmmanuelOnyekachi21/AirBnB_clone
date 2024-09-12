#!/usr/bin/python3
"""
File
"""


import cmd


class HBNBCommand(cmd.Cmd):
    """
    Classsjfn
    """
    prompt = "(hbnb) "
    def do_quit(self, arg):
        """
        g
        """
        return True

    def do_EOF(self, arg):
        '''
        g
        '''
        return True

    def emptyline(self):
        """
        dhf
        """
        pass



if __name__ == '__main__':
    HBNBCommand().cmdloop()
