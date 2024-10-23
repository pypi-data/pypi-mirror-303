"""
System-related commands for TermiPy.

This module contains commands that deal with system operations.
"""

import os
import shutil
from typing import List
from termipy.base_command import Command

class EchoCommand(Command):
    def execute(self, args: List[str]) -> bool:
        print(" ".join(args))
        return True

class GetWdCommand(Command):
    def execute(self, args: List[str]) -> bool:
        print(os.getcwd())
        return True

class SetWdCommand(Command):
    def execute(self, args: List[str]) -> bool:
        if not args:
            print("cd: No directory specified.")
            return True
        try:
            os.chdir(os.path.expanduser(args[0]))
        except FileNotFoundError:
            print(f"cd: No such file or directory: {args[0]}")
        except PermissionError:
            print(f"cd: Permission denied: {args[0]}")
        return True

class TypeOfCommand(Command):
    def execute(self, args: List[str]) -> bool:
        if not args:
            print("typeof: Missing argument")
            return True
        command = args[0]
        if command in ["echo", "exit", "setwd", "getwd", "clear", "typeof", "help"]:
            print(f"{command} is a shell builtin")
        elif shutil.which(command):
            print(f"{command} is {shutil.which(command)}")
        else:
            print(f"{command}: not found")
        return True

class ClearCommand(Command):
    def execute(self, args: List[str]) -> bool:
        os.system('cls' if os.name == 'nt' else 'clear')
        return True

class DiskUsageCommand(Command):
    def execute(self, args: List[str]) -> bool:
        path = args[0] if args else "."
        try:
            total, used, free = shutil.disk_usage(path)
            print(f"Disk usage for '{path}':")
            print(f"Total: {total // (2**30)} GB")
            print(f"Used: {used // (2**30)} GB")
            print(f"Free: {free // (2**30)} GB")
        except Exception as e:
            print(f"Error getting disk usage for '{path}': {str(e)}")
        return True

class ExitCommand(Command):
    def execute(self, args: List[str]) -> bool:
        print("Exiting TermiPy. Goodbye!")
        return False