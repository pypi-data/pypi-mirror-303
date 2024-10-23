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