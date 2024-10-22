"""
TermiPy shell module.

This module contains the main TermiPy class that runs the shell.
"""

import shlex
from typing import Dict
from termipy.base_command import Command
from termipy.file_commands import (
    TreeCommand, CreateCommand, SearchCommand, DeleteCommand, RenameCommand,
    PermissionsCommand
)
from termipy.system_commands import (
    EchoCommand, GetWdCommand, SetWdCommand, TypeOfCommand, ClearCommand,
    DiskUsageCommand, ExitCommand
)
from termipy.environment_commands import SetPyEnvCommand, SetREnvCommand
from termipy.utility_commands import (
    HelpCommand, AboutCommand, CommandsCommand
)
from termipy.resource_commands import ResourceUsageCommand
from termipy.docs import WELCOME_MESSAGE

class TermiPy:
    def __init__(self):
        self.commands: Dict[str, Command] = {
            "echo": EchoCommand(),
            "getwd": GetWdCommand(),
            "ls": GetWdCommand(),
            "setwd": SetWdCommand(),
            "typeof": TypeOfCommand(),
            "clear": ClearCommand(),
            "cls": ClearCommand(),
            "clr": ClearCommand(),
            "tree": TreeCommand(),
            "create": CreateCommand(),
            "search": SearchCommand(),
            "setpyenv": SetPyEnvCommand(),
            "setrenv": SetREnvCommand(),
            "help": HelpCommand(),
            "about": AboutCommand(),
            "commands": CommandsCommand(),
            "delete": DeleteCommand(),
            "rename": RenameCommand(),
            "diskusage": DiskUsageCommand(),
            "permissions": PermissionsCommand(),
            "exit": ExitCommand(),
            "resource": ResourceUsageCommand(),
            "resources": ResourceUsageCommand(),
            "stats": ResourceUsageCommand(),
        }

    def run(self):
        print(WELCOME_MESSAGE)
        while True:
            try:
                user_input = input("@termipy >> ")
                if not self.handle_input(user_input):
                    break
            except KeyboardInterrupt:
                print("\nUse 'exit' to quit TermiPy.")
            except EOFError:
                print("\nExiting TermiPy.")
                break

    def handle_input(self, user_input: str) -> bool:
        try:
            parts = shlex.split(user_input)
            if not parts:
                return True
            cmd, *args = parts
            command = self.commands.get(cmd)
            if command:
                return command.execute(args)
            else:
                print(f"{cmd}: command not found")
                return True
        except Exception as e:
            print(f"Error processing command: {str(e)}")
            return True