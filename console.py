#!/usr/bin/python3
"""
that contains the entry point of the command interpreter
"""
import cmd
import string
import json
from models import storage
from models.base_model import BaseModel
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    class definition
    """
    prompt = "(hbnb) "
    identchar = string.ascii_letters + string.digits + '_' + ',' + ' '

    __classes = {
            "BaseModel",
            "User"
            }

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file)
        """
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)
            storage.save()

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        arg = line.split()
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** instance id missing **")
        else:
            print(obj_dict["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        arg = line.split()
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif arg[1] == 0:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg[0], arg[1])]
            storage.save()

    def do_all(self, line):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        arg = line.split()
        dict_str = []
        obj_dict1 = storage.all()
        if arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 0:
            dict_str1 = [str(obj) for obj in obj_dict1.values()]
            print(dict_str1)
        else:
            if arg[0] in HBNBCommand.__classes:
                for key, values in obj_dict1.items():
                    if arg[0] in key:
                        dict_str.append(str(values))
                print(dict_str)


    def do_count(self, line):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class.
        """
        arg = line.split()
        count = 0
        for obj in storage.all().values():
            if arg[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, line):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary.
        """
        arg = line.split()
        obj_dict = storage.all()

        if len(arg) == 0:
            print("** class name missing **")
            return False
        if arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg[0], arg[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg) == 2:
            print("** attribute name missing **")
            return False
        if len(arg) == 3:
            try:
                type(eval(arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(arg) == 4:
            obj = obj_dict["{}.{}".format(arg[0], arg[1])]
            if arg[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[arg[2]])
                obj.__dict__[arg[2]] = valtype(arg[3])
            else:
                obj.__dict__[arg[2]] = arg[3]
        elif type(eval(arg[2])) == dict:
            obj = obj_dict["{}.{}".format(arg[0], arg[1])]
            for key, values in eval(arg[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = valtype(values)
                else:
                    obj.__dict__[key] = values
        storage.save()

    def emptyline(self):
        """
        Do nothing upon recieving an empty command
        """
        pass

    def do_quit(self, line):
        """
        An instance to exit the program
        """
        return True

    def do_EOF(self, line):
        """
        to exit the program
        """
        print("")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
