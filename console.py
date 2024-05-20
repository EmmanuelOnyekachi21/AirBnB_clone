#!/usr/bin/python3
"""This module provides the HBNBCommand class which provides
a command interpreter to be used in the AirBNB clone project
"""

import cmd
from models.base_model import BaseModel
import re
from models import storage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place


class HBNBCommand(cmd.Cmd):
    """This is the command interpreter class for the AirBNB project
        which inherits from the cmd module.

    The Class implements various project specific commands and the usual
    `help` to get tips on usage and `quit` or `EOF` command to exit program

    """
    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "Amenity", "City", "State", "Review",
                  "Place"]

    def do_quit(self, arg):
        """Exits the command interpreter"""
        return True

    def do_EOF(self, arg):
        """Exits the command interpreter"""
        return True

    def emptyline(self):
        """Action to be taken if emptyline is passed"""
        pass

    def do_create(self, arg):
        """
        Creates a new instance of a given class, saves it and prints the id
        USAGE: create <class name>
        EXAMPLE:
            create BaseModel
            create User
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
        Prints the string representation of an instance based on the
            given class name and id.
        USAGE: show <class name> <id>
        EXAMPLE:
            show BaseModel 87654321-1234-5678-12345678
            show User 12345678-1234-1234-1234-12345678
        Note: class name and id must be provided
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
            print(obj_dict[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        USAGE: destroy <class name> <id>
        EXAMPLE:
            destroy BaseModel 87654321-1234-5678-12345678
            destroy User 12345678-1234-1234-1234-12345678
        Note: class name and id must be provided
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

    def do_all(self, class_arg):
        """
        Prints string representation of all instances of a given class based
            on class name provided or all instances is printed if class name
            not provided.
        USAGE: all <class name>
        EXAMPLE:
            all BaseModel
            all User
            all
        """
        all_list = []
        obj_dict = storage.all()
        if class_arg:
            if class_arg not in self.class_list:
                print("** class doesn't exist **")
                return
            for key in obj_dict.keys():
                if class_arg == (key[:len(class_arg)]):
                    all_list.append(str(obj_dict[key]))
        else:
            for key in obj_dict.keys():
                all_list.append(str(obj_dict[key]))
        print(all_list)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or
            updating attribute.
        USAGE: update <class name> <id> <attribute name> "<attribute value>"
        EXAMPLE:
            update BaseModel 87654321-1234-5678-12345678 name "Emmanuel"
            update User 12345678-1234-1234-1234-12345678 email "ea@z.com"
        Note: all arguments must be provided exactly and id, created_at and
            updated_at can't be updated.
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
            class_arg = arg_list[0]
            class_id = arg_list[1]
            attr_name = arg_list[2]
            attr_val = arg_list[3].strip('"')
        if class_arg not in self.class_list:
            print("** class doesn't exist **")
            return
        key = f"{class_arg}.{class_id}"
        obj_dict = storage.all()
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
        Additional Usage: <class name>.<command>(args)
        """
        pattern = r'^([^.]*)\.(.*?)\((.*?)\)$'
        matches = re.match(pattern, arg)
        if matches:
            class_arg = matches.group(1)
            command = matches.group(2)
            args = matches.group(3)
        else:
            print(f"*** Unknown syntax: {arg}")
            return
        if class_arg not in self.class_list:
            print("** class doesn't exist **")
            return
        if command == "all":
            self.do_all(class_arg)
        elif command == "count":
            count = 0
            obj_dict = storage.all()
            for key in obj_dict.keys():
                if class_arg == (key[:len(class_arg)]):
                    count += 1
            print(count)
        elif command == "show":
            line = " ".join([class_arg, args.strip('"')])
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
