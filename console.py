#!/usr/bin/python3
"""Defines the HBNB console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Initialize the cmd shell
    """
    prompt = '(hbnb) '

    def emptyline(self):
        """empty line"""
        pass

    def do_EOF(self, line):
        """EOF to exit the program"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
