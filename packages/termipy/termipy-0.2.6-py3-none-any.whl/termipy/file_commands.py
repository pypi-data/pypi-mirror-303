"""
File-related commands for TermiPy.

This module contains commands that deal with file and directory operations.
"""

import os
import shutil
from typing import List
from termipy.base_command import Command

class TreeCommand(Command):
    """Display the directory structure in a tree-like format."""
    
    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        level = None
        path = "."
        
        for i, arg in enumerate(args):
            if arg == "-l" and i + 1 < len(args):
                try:
                    level = int(args[i + 1])
                    args = args[:i] + args[i+2:]
                    break
                except ValueError:
                    print("Error: Invalid level value. Please provide an integer.")
                    return False
        
        if args:
            path = args[0]
        
        self._print_tree(path, level=level)
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <path>     Optional. The directory to display. Defaults to current directory.")
        print("  -l <level> Optional. The maximum depth level to display.")
        print("\nExamples:")
        print("  tree /path/to/directory")
        print("  tree -l 2 /path/to/directory")

    def _print_tree(self, path, prefix="", level=None, current_level=0):
        if not os.path.exists(path):
            print(f"Error: Path '{path}' does not exist.")
            return

        print(f"{prefix}{os.path.basename(path)}/")
        
        if level is not None and current_level >= level:
            return

        prefix += "│   "
        
        try:
            entries = os.listdir(path)
        except PermissionError:
            print(f"{prefix}Permission denied")
            return

        entries.sort()
        for i, entry in enumerate(entries):
            entry_path = os.path.join(path, entry)
            is_last = (i == len(entries) - 1)
            
            if is_last:
                print(f"{prefix[:-4]}└── {entry}")
                new_prefix = prefix[:-4] + "    "
            else:
                print(f"{prefix[:-4]}├── {entry}")
                new_prefix = prefix

            if os.path.isdir(entry_path):
                self._print_tree(entry_path, new_prefix, level, current_level + 1)
                

class CreateCommand(Command):
    """Create a new file or directory."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        if not args:
            print("Error: Please provide a file or directory name.")
            return False
        
        path = args[0]
        if path.endswith('/'):
            os.makedirs(path, exist_ok=True)
            print(f"Directory '{path}' created successfully.")
        else:
            with open(path, 'w') as f:
                pass
            print(f"File '{path}' created successfully.")
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <path>  The file or directory to create.")
        print("\nExample:")
        print("  create myfile.txt    # Creates a file")
        print("  create mydir/        # Creates a directory")

class SearchCommand(Command):
    """Search for files and directories."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        if len(args) < 2:
            print("Error: Please provide both a search term and a directory.")
            return False
        
        term, directory = args[0], args[1]
        self._search(term, directory)
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <term>       The search term to look for.")
        print("  <directory>  The directory to search in.")
        print("\nExample:")
        print("  search myfile.txt /path/to/search")

    def _search(self, term, directory):
        for root, dirs, files in os.walk(directory):
            for name in files + dirs:
                if term.lower() in name.lower():
                    print(os.path.join(root, name))

class DeleteCommand(Command):
    """Delete a file or directory."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        if not args:
            print("Error: Please provide a file or directory to delete.")
            return False
        
        path = args[0]
        if os.path.isdir(path):
            shutil.rmtree(path)
            print(f"Directory '{path}' deleted successfully.")
        elif os.path.isfile(path):
            os.remove(path)
            print(f"File '{path}' deleted successfully.")
        else:
            print(f"Error: '{path}' does not exist.")
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <path>  The file or directory to delete.")
        print("\nExample:")
        print("  delete myfile.txt")
        print("  delete mydir/")

class RenameCommand(Command):
    """Rename a file or directory."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        if len(args) != 2:
            print("Error: Please provide both the old and new names.")
            return False
        
        old_name, new_name = args
        try:
            os.rename(old_name, new_name)
            print(f"Successfully renamed '{old_name}' to '{new_name}'.")
        except FileNotFoundError:
            print(f"Error: '{old_name}' does not exist.")
        except PermissionError:
            print(f"Error: Permission denied to rename '{old_name}'.")
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <old_name>  The current name of the file or directory.")
        print("  <new_name>  The new name for the file or directory.")
        print("\nExample:")
        print("  rename oldfile.txt newfile.txt")

class PermissionsCommand(Command):
    """Change permissions of a file or directory."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
        
        if len(args) != 2:
            print("Error: Please provide both the permissions and the file/directory name.")
            return False
        
        permissions, path = args
        try:
            os.chmod(path, int(permissions, 8))
            print(f"Successfully changed permissions of '{path}' to {permissions}.")
        except FileNotFoundError:
            print(f"Error: '{path}' does not exist.")
        except PermissionError:
            print(f"Error: Permission denied to change permissions of '{path}'.")
        except ValueError:
            print(f"Error: Invalid permissions format. Use octal notation (e.g., 755).")
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <permissions>  The new permissions in octal notation (e.g., 755).")
        print("  <path>         The file or directory to change permissions for.")
        print("\nExample:")
        print("  permissions 755 myfile.txt")
        
        
class AboutCommand(Command):
    """Display information about file or folder."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True
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

    def print_help(self):
        super().print_help()
        print("\nExample:")
        print("  about <filename_here>")
