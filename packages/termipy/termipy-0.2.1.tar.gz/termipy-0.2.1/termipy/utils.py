"""
Utility functions for  TermiPy.

This module contains various utility functions used throughout the TermiPy shell.
"""

import os
import readline

def setup_readline():
    """Set up readline for command history and tab completion."""
    readline.set_completer(completer)
    readline.parse_and_bind("tab: complete")

def completer(text, state):
    """Provide autocompletion for commands and file paths."""
    options = [cmd for cmd in ["echo", "getwd", "setwd", "typeof", "clear", "tree", "create", "search", 
                               "setpyenv", "setrenv", "help", "about", "commands", "delete", "rename", 
                               "diskusage", "permissions", "exit"] if cmd.startswith(text)]
    options.extend([f for f in os.listdir('.') if f.startswith(text)])
    if state < len(options):
        return options[state]
    else:
        return None