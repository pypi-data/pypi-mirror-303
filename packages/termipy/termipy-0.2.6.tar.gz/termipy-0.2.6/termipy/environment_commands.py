"""
Environment-related commands for TermiPy.

This module contains commands that deal with setting up development environments.
"""

import os
import subprocess
import sys
from typing import List
from termipy.base_command import Command

class SetPyEnvCommand(Command):
    """Set up a Python virtual environment."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True

        if not args:
            print("Error: Please provide a name for the virtual environment.")
            return False

        env_name = args[0]
        try:
            subprocess.run([sys.executable, "-m", "venv", env_name], check=True)
            print(f"Python virtual environment '{env_name}' created successfully.")
            print(f"To activate, run: source {env_name}/bin/activate (Unix) or {env_name}\\Scripts\\activate (Windows)")
        except subprocess.CalledProcessError:
            print(f"Error: Failed to create Python virtual environment '{env_name}'.")
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <env_name>  The name of the virtual environment to create.")
        print("\nExample:")
        print("  setpyenv myenv")

class SetREnvCommand(Command):
    """Set up an R environment."""

    def execute(self, args: List[str]) -> bool:
        if self.handle_help_flag(args):
            return True

        if not args:
            print("Error: Please provide a name for the R environment.")
            return False

        env_name = args[0]
        try:
            r_script = f"""
            if (!require(renv)) install.packages("renv")
            renv::init(project = "{env_name}")
            """
            subprocess.run(["Rscript", "-e", r_script], check=True)
            print(f"R environment '{env_name}' created successfully.")
            print(f"To use, set your working directory to '{env_name}' and run library(renv)")
        except subprocess.CalledProcessError:
            print(f"Error: Failed to create R environment '{env_name}'.")
        except FileNotFoundError:
            print("Error: R is not installed or not in the system PATH.")
        return True

    def print_help(self):
        super().print_help()
        print("\nOptions:")
        print("  <env_name>  The name of the R environment to create.")
        print("\nExample:")
        print("  setrenv myenv")