"""
Base Command module for TermiPy.

This module contains the abstract base class for all commands.
"""

from abc import ABC, abstractmethod
from typing import List

class Command(ABC):
    @abstractmethod
    def execute(self, args: List[str]) -> bool:
        """
        Execute the command with the given arguments.

        Args:
            args (List[str]): List of command arguments.

        Returns:
            bool: True if the shell should continue running, False otherwise.
        """
        pass
    
    def print_help(self):
        print(f"Usage: {self.__class__.__name__.lower()} [options]")
        print(f"Description: {self.__doc__}")
        print("Use -h or --help to display this help message.")

    def handle_help_flag(self, args: List[str]) -> bool:
        if "-h" in args or "--help" in args:
            self.print_help()
            return True
        return False