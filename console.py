#!/usr/bin/python3
"""Defines the HBNBCommand class for the AirBNB clone project.
This class provides a command interpreter for managing project objects.
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
    """Command interpreter class for the AirBNB clone project.
    Inherits from cmd.Cmd and implements custom commands for managing objects.
    """
    
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity, "City": City, "State": State, "Review": Review, "Place": Place}

    def do_quit(self, arg):
        """Exit the command interpreter."""
        return True

    def do_EOF(self, arg):
        """Exit the command interpreter on EOF (Ctrl-D)."""
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Create a new instance of a given class, save it, and print its ID.
        Usage: create <class name>
        Example:
            create BaseModel
            create User
        """
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print the string representation of an instance based on class name and ID.
        Usage: show <class name> <id>
        Example:
            show BaseModel 1234-5678-1234
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, instance_id = args
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Delete an instance based on class name and ID.
        Usage: destroy <class name> <id>
        Example:
            destroy BaseModel 1234-5678-1234
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        class_name, instance_id = args
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{instance_id}"
        instance = storage.all().pop(key, None)
        if instance:
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Print all instances of a given class, or all instances if no class is specified.
        Usage: all [<class name>]
        Example:
            all BaseModel
            all
        """
        instances = storage.all()
        if arg:
            if arg not in self.classes:
                print("** class doesn't exist **")
                return
            instances = {k: v for k, v in instances.items() if k.startswith(arg)}
        print([str(instance) for instance in instances.values()])

    def do_update(self, arg):
        """Update an instance by adding or updating an attribute.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Example:
            update BaseModel 1234-5678-1234 name "Alice"
        """
        pattern = r'"[^"]*"|\S+'
        args = re.findall(pattern, arg)
        if len(args) < 4:
            print("** class name missing **" if len(args) < 1 else 
                  "** instance id missing **" if len(args) < 2 else 
                  "** attribute name missing **" if len(args) < 3 else 
                  "** value missing **")
            return
        class_name, instance_id, attr_name, attr_value = args
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{class_name}.{instance_id}"
        instance = storage.all().get(key)
        if not instance:
            print("** no instance found **")
            return
        attr_value = attr_value.strip('"')
        setattr(instance, attr_name, type(getattr(instance, attr_name, attr_value))(attr_value))
        instance.save()

    def default(self, arg):
        """Handle unrecognized commands.
        Additional usage: <class name>.<command>(<args>)
        """
        pattern = r'^([^.]*)\.(.*?)\((.*?)\)$'
        match = re.match(pattern, arg)
        if not match:
            print(f"*** Unknown syntax: {arg}")
            return
        class_name, command, params = match.groups()
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        if command == "all":
            self.do_all(class_name)
        elif command == "count":
            count = sum(1 for key in storage.all() if key.startswith(class_name))
            print(count)
        elif command == "show":
            self.do_show(f"{class_name} {params.strip('\"')}")
        elif command == "destroy":
            self.do_destroy(f"{class_name} {params.strip('\"')}")
        elif command == "update":
            if '{' in params and '}' in params:
                id_part, dict_part = params.split(', {')
                dict_part = '{' + dict_part
                id_part = id_part.strip().strip('"')
                updates = eval(dict_part)
                for key, value in updates.items():
                    self.do_update(f'{class_name} {id_part} {key} "{value}"')
            else:
                self.do_update(params.replace(",", " ", 1))
        else:
            print(f"*** Unknown syntax: {arg}")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
