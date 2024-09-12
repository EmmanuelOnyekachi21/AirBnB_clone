#!/usr/bin/python3
"""This script contains the HBNBCommand class for the AirBNB clone project.
It provides a command interpreter for managing objects within the project.
"""

from models.base_model import BaseModel
import re
from models import storage
# from models.user import User
# from models.amenity import Amenity
# from models.city import City
# from models.state import State
# from models.review import Review
# from models.place import Place
import cmd


class HBNBCommand(cmd.Cmd):
    """Command processor class for the AirBNB project.
    This class allows for interactive command line commands to manage
    and manipulate the application's objects.
    """

    prompt = "(hbnb) "
    class_list = ["BaseModel", "User", "Amenity", "City", "State", "Review",
                  "Place"]

    def do_quit(self, arg):
        """Exit the command line interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the interpreter using EOF (Ctrl+D)."""
        return True

    def emptyline(self):
        """Handle empty input line to do nothing."""
        pass

    def do_create(self, arg):
        """Create a new instance of a specified class, save it, and print the ID.
        Usage: create <class name>
        Example:
            create BaseModel
            create User
        """
        if arg:
            if arg == "BaseModel":
                new = BaseModel()
            # elif arg == "User":
            #     new = User()
            # elif arg == "Amenity":
            #     new = Amenity()
            # elif arg == "City":
            #     new = City()
            # elif arg == "State":
            #     new = State()
            # elif arg == "Review":
            #     new = Review()
            # elif arg == "Place":
            #     new = Place()
            else:
                print("** class doesn't exist **")
                return
            new.save()
            print(new.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """Display the string representation of an instance given its class name and ID.
        Usage: show <class name> <id>
        Example:
            show BaseModel 1234-5678-1234
            show User 1234-5678-1234
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
        """Delete an instance based on its class name and ID.
        Usage: destroy <class name> <id>
        Example:
            destroy BaseModel 1234-5678-1234
            destroy User 1234-5678-1234
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
        """Print all string representations of instances of a given class,
        or all instances if no class is specified.
        Usage: all <class name>
        Example:
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
        """Update an instance based on the class name and ID by adding or modifying an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Example:
            update BaseModel 1234-5678-1234 name "Alice"
            update User 1234-5678-1234 email "alice@example.com"
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

    # def default(self, arg):
    #     """Handle unrecognized commands, allowing for additional syntax.
    #     Additional Usage: <class name>.<command>(args)
    #     """
    #     pattern = r'^([^.]*)\.(.*?)\((.*?)\)$'
    #     matches = re.match(pattern, arg)
    #     if matches:
    #         class_arg = matches.group(1)
    #         command = matches.group(2)
    #         args = matches.group(3)
    #     else:
    #         print(f"*** Unknown syntax: {arg}")
    #         return
    #     if class_arg not in self.class_list:
    #         print("** class doesn't exist **")
    #         return
    #     if command == "all":
    #         self.do_all(class_arg)
    #     elif command == "count":
    #         count = 0
    #         obj_dict = storage.all()
    #         for key in obj_dict.keys():
    #             if class_arg == (key[:len(class_arg)]):
    #                 count += 1
    #         print(count)
    #     elif command == "show":
    #         line = " ".join([class_arg, args.strip('"')])
    #         self.do_show(line)
    #     elif command == "destroy":
    #         line = " ".join([class_arg, args.strip('"')])
    #         self.do_destroy(line)
    #     elif command == "update":
    #         dict_list = re.findall(r'\{(.+?)\}', args)
    #         if dict_list:
    #             args_list = args.split(", ")
    #             class_id = args_list[0].strip('"')
    #             dict_args_list = dict_list[0].split(", ")
    #             for dict_args in dict_args_list:
    #                 key, val = dict_args.split(": ")
    #                 key = key.strip('"')
    #                 line = " ".join([class_arg, class_id, key.strip("'"),
    #                                  val.strip("'")])
    #                 print(line)
    #                 self.do_update(line)
    #         else:
    #             args_list = args.split(", ")
    #             class_id, attr_name, attr_val = args_list
    #             attr_name = attr_name.strip('"')
    #             line = " ".join([class_arg, class_id.strip('"'),
    #                             attr_name.strip("'"), attr_val.strip("'")])
    #             print(line)
    #             self.do_update(line)
    #     else:
    #         print(f"*** Unknown syntax: {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
