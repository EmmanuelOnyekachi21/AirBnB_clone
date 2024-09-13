#!/usr/bin/python3
"""
File
"""


import cmd
from models import storage
import re
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Classsjfn
    """

    class_list = ['BaseModel', 'User']
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

    def do_create(self, arg):
        """
        Create
        """
        if arg:
            if arg == "BaseModel":
                new = BaseModel()
            else:
                print("** class doesn't exist **")
                return
            new.save()
            print(new.id)
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        show
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
        ghrh
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
        sjdfsfhur
        """
        obj_list = []
        obj_dict = storage.all()
        if arg:
            if arg not in self.class_list:
                print("** class doesn't exist **")
                return

            for key in obj_dict.keys():
                if arg == key.split('.')[0]:
                    obj_list.append(str(obj_dict[key]))
        else:
            for key in obj_dict.keys():
                obj_list.append(str(obj_dict[key]))
        print(obj_list)

    def do_update(self, arg):
        """
        Update.
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

        current_attr = getattr(obj, attr_name, "")
        attr_type = type(current_attr)

        if attr_type is int:
            attr_val = int(attr_val)
        elif attr_type is float:
            attr_val = float(attr_val)
        setattr(obj, attr_name, attr_val)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
