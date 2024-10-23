"""
File-related commands for TermiPy.

This module contains commands that deal with file and directory operations.
"""

import os
import shutil
from typing import List
from termipy.base_command import Command

class TreeCommand(Command):
    def execute(self, args: List[str]) -> bool:
        def print_tree(directory, prefix=""):
            entries = os.listdir(directory)
            for i, entry in enumerate(entries):
                is_last = i == len(entries) - 1
                print(f"{prefix}{'└── ' if is_last else '├── '}{entry}")
                if os.path.isdir(os.path.join(directory, entry)):
                    print_tree(os.path.join(directory, entry), prefix + ('    ' if is_last else '│   '))
        
        path = args[0] if args else "."
        print(f"Directory tree of {os.path.abspath(path)}:")
        print_tree(path)
        return True

class CreateCommand(Command):
    def execute(self, args: List[str]) -> bool:
        if not args:
            print("create: Missing argument")
            return True
        path = args[0]
        try:
            if path.endswith('/'):
                os.makedirs(path, exist_ok=True)
                print(f"Directory '{path}' created successfully.")
            else:
                with open(path, 'w') as f:
                    pass
                print(f"File '{path}' created successfully.")
        except Exception as e:
            print(f"Error creating '{path}': {str(e)}")
        return True

class SearchCommand(Command):
    def execute(self, args: List[str]) -> bool:
        if not args:
            print("search: Missing argument")
            return True
        filename = args[0]
        for root, dirs, files in os.walk('.'):
            if filename in files:
                print(os.path.join(root, filename))
        return True

class DeleteCommand(Command):
    def execute(self, args: List[str]) -> bool:
        if not args:
            print("delete: Missing argument")
            return True
        path = args[0]
        try:
            if os.path.isdir(path):
                shutil.rmtree(path)
                print(f"Directory '{path}' deleted successfully.")
            else:
                os.remove(path)
                print(f"File '{path}' deleted successfully.")
        except Exception as e:
            print(f"Error deleting '{path}': {str(e)}")
        return True

class RenameCommand(Command):
    def execute(self, args: List[str]) -> bool:
        if len(args) != 2:
            print("rename: Requires two arguments (old_name new_name)")
            return True
        old_name, new_name = args
        try:
            os.rename(old_name, new_name)
            print(f"'{old_name}' renamed to '{new_name}' successfully.")
        except Exception as e:
            print(f"Error renaming '{old_name}' to '{new_name}': {str(e)}")
        return True

class PermissionsCommand(Command):
    def execute(self, args: List[str]) -> bool:
        if not args:
            print("permissions: Missing argument")
            return True
        path = args[0]
        try:
            stats = os.stat(path)
            print(f"Permissions for '{path}':")
            print(f"Owner: {oct(stats.st_mode)[-3:]}")
        except Exception as e:
            print(f"Error getting permissions for '{path}': {str(e)}")
        return True