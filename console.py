#!/usr/bin/python3
"""console"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Initialize the cmd shell
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF to exit the program"""
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
