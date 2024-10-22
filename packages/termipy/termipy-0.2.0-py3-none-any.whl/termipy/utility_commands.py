"""
Utility commands for TermiPy.

This module contains miscellaneous utility commands.
"""

import os
from typing import List
from termipy.base_command import Command

class HelpCommand(Command):
    def execute(self, args: List[str]) -> bool:
        help_text = """
        Available commands:
        echo <message>     - Print a message
        getwd              - Get current working directory
        setwd <directory>  - Change directory
        typeof <command>   - Show command type
        clear (cls, clr)   - Clear the screen
        tree [directory]   - Show directory structure
        create <path>      - Create file or directory
        search <filename>  - Search for a file
        setpyenv [name] [version] - Create Python virtual environment
        setrenv [name]     - Initialize R environment
        help               - Show this help message
        about <file>       - Show file details
        commands           - List all commands
        delete <path>      - Delete file or directory
        rename <old> <new> - Rename file or directory
        diskusage [path]   - Show disk usage
        permissions <file> - Show file permissions
        resource, resources, stats - Show system resource usage
        exit               - Exit TermiPy
        """
        print(help_text)
        return True

class AboutCommand(Command):
    def execute(self, args: List[str]) -> bool:
        if not args:
            print("about: Missing argument")
            return True
        path = args[0]
        try:
            stats = os.stat(path)
            print(f"File: {path}")
            print(f"Size: {stats.st_size} bytes")
            print(f"Permissions: {oct(stats.st_mode)[-3:]}")
            print(f"Last modified: {stats.st_mtime}")
        except FileNotFoundError:
            print(f"File not found: {path}")
        return True

class CommandsCommand(Command):
    def execute(self, args: List[str]) -> bool:
        commands = ["echo", "getwd", "setwd", "typeof", "clear", "tree", "create", "search", 
                    "setpyenv", "setrenv", "help", "about", "commands", "delete", "rename", 
                    "diskusage", "permissions", "exit"]
        print("Available commands:")
        for cmd in commands:
            print(f"  {cmd}")
        return True