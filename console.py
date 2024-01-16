#!/usr/bin/python3
"""Defines the HBNB console"""


import cmd
import models
from models.base_model import BaseModel
from datetime import datetime
from shlex import shlex


class HBNBCommand(cmd.Cmd):
    """
    Initialize the cmd shell
    """
    prompt = '(hbnb) '
    cls_list = {'BaseModel': BaseModel}

    def emptyline(self):
        """empty line"""
        pass

    def do_create(self, clsname=None):
        """
        Creates a new instance of BaseModel, saves it and prints the id
        """
        if not clsname:
            print('** class name missing **')
        elif not self.cls_list.get(clsname):
            print('** class doesn\'t exist **')
        else:
            obj = self.cls_list[clsname]()
            models.storage.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based on the
        class name and id
        """
        clsname, obj_id = None, None
        args = arg.split(' ')
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if not clsname:
            print('** class name missing **')
        elif not obj_id:
            print('** instance id missing **')
        elif not self.cls_list.get(clsname):
            print('** class doesn\'t exist **')
        else:
            a = clsname + "." + obj_id
            obj = models.storage.all().get(a)
            if not obj:
                print('** no instance found **')
            else:
                print(obj)
    
    def do_destroy(self, arg):
        """
         Deletes an instance based on the class name and id
        """
        clsname, obj_id = None, None
        args = arg.split(' ')
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if not clsname:
            print('** class name missing **')
        elif not obj_id:
            print('** instance id missing **')
        elif not self.cls_list.get(clsname):
            print('** class doesn\'t exist **')
        else:
            a = clsname + "." + obj_id
            obj = models.storage.all().get(a)
            if not obj:
                print('** no instance found **')
            else:
                del models.storage.all()[a]
                models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances based or not on the class name. 
        """
        if not arg:
            print([str(a) for b, a in models.storage.all().items()])
        else:
            if not self.cls_list.get(arg):
                print('** class doesn\'t exist **')
                return False
            print([str(a) for b, a in models.storage.all().items()
                   if type(a) is self.cls_list.get(arg)])
            
    def do_update(self, arg):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        """
        clsname, obj_id, attr_name, attr_val = None, None, None, None
        updatetime = datetime.now()
        args = arg.split(' ', 3)
        if len(args) > 0:
            clsname = args[0]
        if len(args) > 1:
            obj_id = args[1]
        if len(args) > 2:
            attr_name = args[2]
        if len(args) > 3:
            attr_val = list(shlex(args[3]))[0].strip('"')
        if not clsname:
            print('** class name missing **')
        elif not obj_id:
            print('** instance id missing **')
        elif not attr_name:
            print('** attribute name missing **')
        elif not attr_val:
            print('** value missing **')
        elif not self.cls_list.get(clsname):
            print("** class doesn't exist **")
        else:
            a = clsname + "." + obj_id
            obj = models.storage.all().get(a)
            if not obj:
                print('** no instance found **')
            else:
                if hasattr(obj, attr_name):
                    attr_val = type(getattr(obj, attr_name))(attr_val)
                else:
                    attr_val = self.getType(attr_val)(attr_val)
            setattr(obj, attr_name, attr_val)
            obj.updated_at = updatetime
            models.storage.save()

    @staticmethod
    def getType(attr_val):
        """return input string type"""
        try:
            int(attr_val)
            return (int)
        except ValueError:
            pass
        try:
            float(attr_val)
            return (float)
        except ValueError:
            return (str)

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """EOF to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
