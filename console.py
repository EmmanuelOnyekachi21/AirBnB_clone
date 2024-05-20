#!/usr/bin/python3
"""
Command line interpreter (CLI) using the CMD module.
"""

import cmd
import sys
import models
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Command-line interpreter for the HBNB application.
    Attributes:
        prompt (str): The prompt string displayed to the user.
    Methods:
        do_quit(arg): Handles the 'quit' command to exit the program.
        emptyline(): Does nothing when an empty line + ENTER 
                        shouldn’t execute anything
        do_EOF(arg): Handles the end-of-file condition to gracefully
                        exit the program.
    """
    prompt = '(hbnb) '
    class_list = ["BaseModel", "User", "Amenity", "City", "State", "Review",
                  "Place"]

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        Args:
            arg: Unused argument (required by cmd.Cmd).
        Returns:
            None
        Raises:
            SystemExit: Exits the program with a status code of 0.
        """
        return True

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

    def do_create(self, arg):
        """
        Create a new instance of BaseModel, saves it to the JSON file
        and prints the id.
        """
        if arg:
            if arg == "BaseModel":
                new = BaseModel()
            elif arg == "User":
                new = User()
            elif arg == "Amenity":
                new = Amenity()
            elif arg == "City":
                new = City()
            elif arg == "State":
                new = State()
            elif arg == "Review":
                new = Review()
            elif arg == "Place":
                new = Place()
            else:
                print("** class doesn't exist **")
                return
            new.save()
            print(new.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class and id.
        """
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return

        elif len(arg_list) == 1:
            print("** instance id missing **")
            return
        else:
            class_name = arg_list[0]
            class_id = arg_list[1]

        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{class_id}"
        obj_dict = models.storage.all()
        if key not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict[key])

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        arg_list = arg.split()
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        elif len(arg_list) == 1:
            print("** instance id missing **")
            return
        else:
            class_arg = arg_list[0]
            class_id = arg_list[1]
        if class_arg not in self.class_list:
            print("** class doesn't exist **")
            return
        key = f"{class_arg}.{class_id}"
        obj_dict = storage.all()
        if key in obj_dict:
            del obj_dict[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        all_list = []
        obj_dict = models.storage.all()
        if arg:
            if arg not in self.class_list:
                print("** class doesn't exist **")
                return

            for key in obj_dict.keys():
                if arg == (key[:len(arg)]):
                    all_list.append(str(obj_dict[key]))
        else:
            for key in obj_dict.keys():
                all_list.append(str(obj_dict[key]))
        print(all_list)

    def do_update(self, arg):
        """
        update <class name> <id> <attribute name> "<attribute value>"
        """
        pattern = r'"[^"]+"|\S+'
        arg_list = re.findall(pattern, arg)
        if len(arg_list) == 0:
            print("** class name missing **")
            return
        elif len(arg_list) == 1:
            print("** instance id missing **")
            return
        elif len(arg_list) == 2:
            print("** attribute name missing **")
            return
        elif len(arg_list) == 3:
            print("** value missing **")
            return
        else:
            class_name = arg_list[0]
            class_id = arg_list[1]
            attr_name = arg_list[2]
            attr_value = arg_list[3].strip('"')

        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return

        key = f"{class_name}.{class_id}"
        obj_dict = models.storage.all()
        if key in obj_dict:
            obj = obj_dict[key]
        else:
            print("** no instance found **")
            return
        setattr(obj, attr_name, (type(getattr(obj, attr_name, "")))(attr_val))
        obj.save()

    def default(self, arg):
        """
        Overrides the default implementation to allow for some additional
        use cases.
        """
        pattern = r'^([^.]*)\.(.*?)\((.*?)\)$'
        matches = re.match(pattern, arg)
        if matches:
            class_name = matches.group(1)
            command = matches.group(2)
            args = matches.group(3)
        else:
            print(f"*** Unknown syntax: {arg}")
            return

        if class_name not in self.class_list:
            print("** class doesn't exist **")
            return
        if command == "all":
            self.do_all(class_name)
        elif command == "count":
            count = 0
            obj_dict = models.storage.all()
            for key in obj_dict.keys():
                if class_name == (key[:len(class_name)]):
                    count += 1
                    print(count)
        elif command == "show":
            line = " ".join([class_name, args.strip('"')])
            self.do_show(line)
        elif command == "destroy":
            line = " ".join([class_arg, args.strip('"')])
            self.do_destroy(line)
        elif command == "update":
            dict_list = re.findall(r'\{(.+?)\}', args)
            if dict_list:
                args_list = args.split(", ")
                class_id = args_list[0].strip('"')
                dict_args_list = dict_list[0].split(", ")
                for dict_args in dict_args_list:
                    key, val = dict_args.split(": ")
                    key = key.strip('"')
                    line = " ".join([class_arg, class_id, key.strip("'"),
                                     val.strip("'")])
                    print(line)
                    self.do_update(line)
            else:
                args_list = args.split(", ")
                class_id, attr_name, attr_val = args_list
                attr_name = attr_name.strip('"')
                line = " ".join([class_arg, class_id.strip('"'),
                                attr_name.strip("'"), attr_val.strip("'")])
                print(line)
                self.do_update(line)
        else:
            print(f"*** Unknown syntax: {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
