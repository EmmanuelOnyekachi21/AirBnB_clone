#!/usr/bin/python3
"""
    console for managing my objects
"""
import datetime
import models
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        console itself
    """

    Storage = models.storage
    all_obj = Storage.all()

    ALL_CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Place': Place,
        'Amenity': Amenity,
        'Review': Review
    }
    prompt = "(hbnb) "

    def do_custom_command(self, arg):
        """
            ijoiwejfiwejof
        """
        print('custom')

    # dynamically strip quotes of the update method (obj_value)
    def strip_quotes(self, value) -> str:
        """
            oijikewf
        """
        if value is not None:
            if "\'" in value:
                value = value.strip("'")
                return value
            elif '\"' in value:
                value = value.strip('"')
                return value
            else:
                return value

    def emptyline(self) -> bool:
        pass

    def do_EOF(self, arg):
        """
            no docstring is found
        """
        print()
        return True

    def do_create(self, arg) -> None:
        """
            oijwiejfowe
        """
        usr_input = arg.split(' ')

        if not usr_input[0]:
            print("** class name missing **")
            return

        if usr_input[0] in self.ALL_CLASSES:
            obj = self.ALL_CLASSES[usr_input[0]]()
            print(obj.id)
            for match in range(1, len(usr_input)):
                if "=" in usr_input[match]:
                    attribute, value = usr_input[match].split('=')
                    if '_' in value:
                        value = value.replace("_", " ")
                    if hasattr(obj, attribute):
                        if isinstance(getattr(obj, attribute), float):
                            if '.' not in value:
                                continue
                        setattr(obj, attribute, value.strip('"'))
            obj.save()
            print(obj)
        else:
            print("** class dosen't exist **")

    def do_show(self, arg) -> None:
        """
            shows the str repre of the object
        """
        usr_input = arg.split()
        all_obj = self.Storage.all()

        # Define the regex pattern to match the desired format
        pattern = r'\w+\s\w{8}-\w{4}-\w{4}-\w{4}-\w{12}$'

        # Compile the regex pattern
        regex = re.compile(pattern)

        match = regex.match(arg)

        # validate user_input length
        if len(usr_input) < 1:
            print('** class name missing **')
            return
        elif usr_input[0] not in self.ALL_CLASSES:
            print('** class doesn\'t exist **')
            return
        elif len(usr_input) < 2:
            print('** instance id missing **')
            return

        key = f"{usr_input[0]}.{usr_input[1]}"

        if match:
            if key in self.all_obj.keys():
                print(all_obj[key])
            else:
                print('** no instance found **')
        else:
            print("Invalid input format "
                  "<show class-name xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx>")

    def do_delete(self, arg) -> None:
        """
            iojoewifjoweifwe
        """
        usr_input = arg.split()
        all_obj = self.Storage.all()

        # Define the regex pattern to match the desired format
        pattern = r'(\w+)?\s?(\w{8}-\w{4}-\w{4}-\w{4}-\w{12})?$'

        # Compile the regex pattern
        regex = re.compile(pattern)

        match = regex.match(arg)

        if match is not None:
            match_grp = match.groups()
            cls_name, cls_id = match_grp

        # validate user_input length
            if not cls_name:
                print('** class name missing **')
                return
            elif cls_name not in self.ALL_CLASSES:
                print('** class doesn\'t exist **')
                return
            elif not cls_id:
                print('** instance id missing **')
                return

            # construct a key using the users info
            key = "{}.{}".format(usr_input[0], usr_input[1])
            if key in all_obj:
                del all_obj[key]
                self.Storage.save_obj()
                return
            else:
                print('** no instance found **')
        else:
            print("Invalid input format "
                  "<delete class-name xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx>")

    def do_all(self, arg):
        """
            oijofew
        """
        if not arg:
            for k, v in self.all_obj.items():
                print(v)
            return 'true talk'

        if arg in self.ALL_CLASSES:
            all_obj = self.all_obj

            obj = []
            for k, v in all_obj.items():
                obj_name, obj_id = k.split('.')
                if obj_name == arg:
                    obj.append(str(all_obj[k]))
            print(obj)
        else:
            print('** class doesn\'t exist **')

    def match_pattern(self, arg) -> re.Match:
        """
            oijiefwefwe
        """
        pattern = r"([a-zA-Z_-]+\S+)?\s?([a-zA-Z0-9-]+)?\s?([a-zA-Z_]+)?\s?" \
                  r"(\'\w+\s?\w+\'|\"\w+\s?\w+|\w+\s?\w+)?"
        regex = re.compile(pattern)
        match_object = regex.search(arg)

        return match_object

    def check_arg(self, key, match_arg_group: tuple) -> None:
        """
            this is the arg for checking for arg in my strings
        """
        if match_arg_group[0] is None:
            print('** class name missing **')
            return
        else:
            if match_arg_group[0] not in self.ALL_CLASSES:
                print('** class doesn\'t exist ** ')
                return

        if match_arg_group[1] is None:
            print('** instance id missing **')
            return
        else:
            if key not in self.all_obj:
                print('** no instance found **')
                return

        if match_arg_group[2] is None:
            print('** attribute name missing **')
            return
        elif match_arg_group[3] is None:
            print('** value missing **')
            return

        return match_arg_group

    def do_update(self, arg) -> None:
        """
            update <class name> <id> <attribute name> "<attribute value>"
        """
        obj_dict = self.all_obj
        matches = self.match_pattern(arg)
        match_obj = matches.groups()
        key = f"{match_obj[0]}.{match_obj[1]}"

        all_obj = self.check_arg(key, match_obj)

        if all_obj is not None:
            obj_name, obj_id, obj_attri, obj_value = all_obj
            print(all_obj)
            # print(match_obj)

            model = obj_dict[key]

            if hasattr(model, obj_attri):
                # only update str, int and float
                if not isinstance(getattr(model, obj_attri),
                                  (str, int, float)):
                    print(f"Sorry can't update attribute of type"
                          f" {type(getattr(model, obj_attri))}")
                    return

                if obj_attri not in ['name', 'age', 'email', 'DOB']:
                    print('sorry you can only update your name,'
                          ' age and email only! ')
                    return
                else:
                    try:
                        if obj_attri == 'age':
                            if self.strip_quotes(obj_value):
                                obj_value = self.strip_quotes(obj_value)
                                obj_value = int(obj_value)
                                setattr(model, obj_attri, obj_value)
                                self.Storage.save_obj()
                                model.save()
                                print(f'({obj_attri}) Updated successfully!')
                                return
                        else:
                            obj_value = self.strip_quotes(obj_value)
                            setattr(model, obj_attri, obj_value)
                            self.Storage.save_obj()
                            model.save()
                    except ValueError:
                        print(f'Input <{obj_value}> '
                              f'not a valid format for attribute [age]'
                              f' must be type int!, eg: (18, 19 40)')
                        return
            else:
                print(f"attribute <{obj_attri}> does not exist")
                return

    def do_quit(self, arg) -> bool:
        """
            oijhoeiwfwe
        """
        print("Thank you for having an account with us! 🚀")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
