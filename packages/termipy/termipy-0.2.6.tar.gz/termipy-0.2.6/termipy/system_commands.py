"""
System-related commands for TermiPy.

This module contains commands that deal with system operations.
"""

from typing import List
from termipy.base_command import Command
import os
import shutil
import sys

class EchoCommand(Command):
    """Print the given message to the console."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        print(" ".join(args))
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <message>  The message to be printed.")
        print("\nExample:")
        print("  echo Hello, World!")

class GetWdCommand(Command):
    """Display the current working directory."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        print(os.getcwd())
        return True

    def print_help(self):
        super().print_help()
        print("\nExample:")
        print("  getwd")

class LsCommand(Command):
    """List directory contents."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        path = args[0] if args else "."
        try:
            entries = os.listdir(path)
            for entry in sorted(entries):
                if os.path.isdir(os.path.join(path, entry)):
                    print(f"\033[1;34m{entry}/\033[0m")  # Blue color for directories
                elif os.access(os.path.join(path, entry), os.X_OK):
                    print(f"\033[1;32m{entry}*\033[0m")  # Green color for executables
                else:
                    print(entry)
        except FileNotFoundError:
            print(f"Error: Directory '{path}' not found.")
        except PermissionError:
            print(f"Error: Permission denied to access '{path}'.")
        except NotADirectoryError:
            print(f"Error: '{path}' is not a directory.")
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <path>  Optional. The directory to list. Defaults to current directory.")
        print("\nExamples:")
        print("  ls")
        print("  ls /path/to/directory")

class SetWdCommand(Command):
    """Change the current working directory."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        if not args:
            print("Error: Please provide a directory path.")
            return False
        
        try:
            os.chdir(args[0])
            print(f"Changed working directory to: {os.getcwd()}")
        except FileNotFoundError:
            print(f"Error: Directory '{args[0]}' not found.")
        except NotADirectoryError:
            print(f"Error: '{args[0]}' is not a directory.")
        except PermissionError:
            print(f"Error: Permission denied to access '{args[0]}'.")
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <path>  The directory to change to.")
        print("\nExample:")
        print("  setwd /path/to/directory")

class TypeOfCommand(Command):
    """Display the type of a file or directory."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        if not args:
            print("Error: Please provide a file or directory path.")
            return False
        
        path = args[0]
        if os.path.isfile(path):
            print(f"'{path}' is a file.")
        elif os.path.isdir(path):
            print(f"'{path}' is a directory.")
        elif os.path.islink(path):
            print(f"'{path}' is a symbolic link.")
        else:
            print(f"'{path}' does not exist or is of unknown type.")
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <path>  The file or directory to check.")
        print("\nExample:")
        print("  typeof myfile.txt")

class ClearCommand(Command):
    """Clear the console screen."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        os.system('cls' if os.name == 'nt' else 'clear')
        return True

    def print_help(self):
        super().print_help()
        print("\nExample:")
        print("  clear")

class DiskUsageCommand(Command):
    """Display disk usage information."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        path = args[0] if args else "."
        total, used, free = shutil.disk_usage(path)
        print(f"Total: {self._format_size(total)}")
        print(f"Used: {self._format_size(used)}")
        print(f"Free: {self._format_size(free)}")
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <path>  Optional. The directory to check. Defaults to current directory.")
        print("\nExample:")
        print("  diskusage /path/to/directory")

    def _format_size(self, size):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.2f} {unit}"
            size /= 1024
        return f"{size:.2f} PB"

class ExitCommand(Command):
    """Exit the TermiPy shell."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        print("Exiting TermiPy. Goodbye!")
        sys.exit(0)

    def print_help(self):
        super().print_help()
        print("\nExample:")
        print("  exit")