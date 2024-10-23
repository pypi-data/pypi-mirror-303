"""
Environment-related commands for TermiPy.

This module contains commands that deal with setting up development environments.
"""

import subprocess
import venv
from typing import List
from termipy.base_command import Command

class SetPyEnvCommand(Command):
    def execute(self, args: List[str]) -> bool:
        project_name = args[0] if args else "my_project"
        python_version = args[1] if len(args) > 1 else "3.8"
        
        try:
            venv.create(project_name, with_pip=True)
            print(f"Python virtual environment '{project_name}' created with Python {python_version}")
        except Exception as e:
            print(f"Error creating virtual environment: {str(e)}")
        return True

class SetREnvCommand(Command):
    def execute(self, args: List[str]) -> bool:
        project_name = args[0] if args else "my_r_project"
        
        try:
            subprocess.run(["R", "-e", f"if (!require('renv')) install.packages('renv'); renv::init('{project_name}')"], check=True)
            print(f"R environment '{project_name}' initialized")
        except Exception as e:
            print(f"Error initializing R environment: {str(e)}")
        return True