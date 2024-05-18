#!/usr/bin/python3
"""
Command line interpreter (CLI) using the CMD module.
"""
import cmd
import sys
import models
import os
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
        emptyline(): Does nothing when an empty line + ENTER shouldn’t execute anything
        do_EOF(arg): Handles the end-of-file condition to gracefully exit the program.
    """
    prompt = '(hbnb) '
    MODELS = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review,
    }

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

    def do_create(self, arg):
        """
        Creates an instance of BaseModel, saves it to the JSON file
        and prints the id.
        """
        # Parse user input to extract the class name
        input = arg.split(' ')
        # Check if the class name is missing
        if not input[0]:
            print("* class name missing *")
            return
        # If the class name exists, a new instance(obj) is created.
        if input[0] in self.MODELS:
            # Create a new instance of the corresponding class
            obj = self.MODELS[input[0]]()
            # Save the new instance to the JSON file
            obj.save()
            # Print the ID of the newly created instance
            print(obj.id)
        else:
            print("* class doesn't exist *")

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the class and id.
        """
        # Parse user input to extract the class name and ID
        args = arg.split()
        if not args:
            print("* class name missing *")
            return
        class_name = args[0]
        # Check if class name exists
        if class_name not in self.MODELS:
            print("* class doesn't exist *")
            return
        if len(args) < 2:
            print("* instance id missing *")
            return
        instance_id = args[1]
        # Retrieve the instance based on the class name and ID
        key = f"{class_name}.{instance_id}"
        instance = models.storage.all().get(key)
        # If the instance exists, print its string representation.
        if instance:
            print(instance)
        else:
            print("* no instance found *")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.
        """
        # Parse user input based on the class name and ID
        args = arg.split()
        # Check if the class name is missing
        if not args:
            print("* class name missing *")
            return
        class_name = args[0]
        # Check if the class name exists.
        if class_name not in self.MODELS:
            print("* class doesn't exist *")
            return
        # Check if the ID is missing.
        if len(args) < 2:
            print("* instance id missing *")
            return
        instance_id = args[1]
        # Construct the key for the instance
        instance_key = f"{class_name}.{instance_id}"
        object_dict = models.storage.all()
        # Check if the instance exists
        if instance_key not in object_dict:
            print("* no instance found *")
            return
        # Deletes the instance from the storage and save changes
        del object_dict[instance_key]
        models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.
        """
        instances = []
        all_objects = models.storage.all()
        if arg:
            if arg in self.MODELS:
                for key, instance in all_objects.items():
                    if key.split('.')[0] == arg:
                        instances.append(str(instance))
            else:
                print("* class doesn't exist *")
                return
        else:
            for instance in all_objects.values():
                instances.append(str(instance))
        print(instances)

    def do_update(self, arg):
        """
        update <class name> <id> <attribute name> "<attribute value>"
        """
        # Split the arguments provided by the user.
        args = arg.split()
        # Check if class name is missing.
        if len(args) < 1:
            print("* class name missing *")
            return
        class_name = args[0]
        # Check if class name exists
        if class_name not in self.MODELS:
            print("* class doesn't exist *")
            return
        # Check if instance id is missing
        if len(args) < 2:
            print("* instance id missing *")
            return
        instance_id = args[1]
        key = f"{class_name}.{instance_id}"
        # Check if attribute name is missing
        if len(args) < 3:
            print("* attribute name missing *")
            return
        attribute_name = args[2]
        # Check if value for the attribute name is missing
        if len(args) < 4:
            print("* value missing *")
            return
        attribute_value = args[3]
        # Check if there are extra arguments
        if len(args) > 4:
            pass
        if key not in models.storage.all().keys():
            print("* no instance found *")
            return
        # Remove surrounding quotes from the attribute value if present
        if attribute_value.startswith('"') and attribute_value.endswith('"'):
            attribute_value = attribute_value[1:-1]
        obj = models.storage.all()[key]
        # Type casting for simple types: string, integer, float
        if hasattr(obj, attribute_name):
            attr_type = type(getattr(obj, attribute_name))
            try:
                attribute_value = attr_type(attribute_value)
            except ValueError:
                pass
        setattr(obj, attribute_name, attribute_value)
        models.storage.save()

if __name__ == "__main__":
    if not sys.stdin.isatty():
        for command in sys.stdin:
            HBNBCommand().onecmd(command)
    else:
        HBNBCommand().cmdloop()
