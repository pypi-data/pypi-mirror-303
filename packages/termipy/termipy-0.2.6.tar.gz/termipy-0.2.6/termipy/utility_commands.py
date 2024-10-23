"""
Utility commands for TermiPy.

This module contains miscellaneous utility commands.
"""

import os
from typing import List
from termipy.base_command import Command
from termipy.docs import HELP_MESSAGE

class HelpCommand(Command):
    """Display help information for TermiPy."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        print(HELP_MESSAGE)
        return True

    def print_help(self):
        super().print_help()
        print("\nExample:")
        print("  help")


class CommandsCommand(Command):
    """List all available commands in TermiPy."""

    def execute(self, args: List[str]) -> bool:
        commands = ["echo", "getwd", "setwd", "typeof", "clear", "tree", "create", "search", 
                    "setpyenv", "setrenv", "help", "about", "commands", "delete", "rename", 
                    "diskusage", "permissions", "exit"]
        print("Available commands:")
        for cmd in commands:
            print(f"  {cmd}")
        return True

    def print_help(self):
        super().print_help()
        print("\nExample:")
        print("  commands")