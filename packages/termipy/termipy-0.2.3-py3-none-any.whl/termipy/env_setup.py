import os
import sys
import subprocess
import readline
import venv

def create_virtual_environment(python_version, project_name, req_file):
    """Create a virtual environment and install requirements."""
    try:
        if not os.path.exists(project_name):
            os.makedirs(project_name)
            sys.stdout.write(f"Created project directory: {project_name}\n")
            sys.stdout.flush()

        python_executable = f"python{python_version}"
        if subprocess.run([python_executable, "--version"], capture_output=True).returncode != 0:
            sys.stdout.write(f"Error: Python {python_version} is not installed or not found.\n")
            sys.stdout.flush()
            return
        
        venv_dir = os.path.join(project_name, 'venv')
        sys.stdout.write(f"Creating virtual environment with Python {python_version}...\n")
        sys.stdout.flush()
        venv.create(venv_dir, with_pip=True)
        
        activate_script = os.path.join(venv_dir, 'bin', 'activate') if os.name != 'nt' else os.path.join(venv_dir, 'Scripts', 'activate')
        sys.stdout.write(f"Activating virtual environment...\n")
        sys.stdout.flush()
        
        if req_file and os.path.exists(req_file):
            sys.stdout.write(f"Installing requirements from {req_file}...\n")
            sys.stdout.flush()
            subprocess.run([os.path.join(venv_dir, 'bin', 'pip'), 'install', '-r', req_file], check=True)
        else:
            sys.stdout.write("No valid requirements.txt found.\n")
            sys.stdout.flush()
    except Exception as e:
        sys.stdout.write(f"Error creating virtual environment: {str(e)}\n")
        sys.stdout.flush()

def handle_setpyenv(args, command):
    """Handle the 'setPyenv' command to set up a Python environment."""
    python_version = "3.10"
    req_file = None
    project_name = "my-app"

    try:
        for i, arg in enumerate(args):
            if arg == "--python" and i + 1 < len(args):
                python_version = args[i + 1]
            elif arg == "--req" and i + 1 < len(args):
                req_file = args[i + 1]
            elif arg == "--name" and i + 1 < len(args):
                project_name = args[i + 1]

        create_virtual_environment(python_version, project_name, req_file)
    except Exception as e:
        sys.stdout.write(f"Error handling setPyenv command: {str(e)}\n")
        sys.stdout.flush()


def get_R(r_version):
    pass

def handle_setrenv(args, command):
    """Set up an R environment for a project."""
    if len(args) < 3:
        sys.stdout.write("Usage: setRenv --name <project-name> --req <requirements-file>\n")
        sys.stdout.flush()
        return

    project_name = None
    requirements_file = None

    try:
        for i in range(len(args)):
            if args[i] == '--name':
                project_name = args[i + 1] if i + 1 < len(args) else None
            elif args[i] == '--req':
                requirements_file = args[i + 1] if i + 1 < len(args) else None

        if not project_name:
            sys.stdout.write("Error: Project name is required.\n")
            sys.stdout.flush()
            return

        project_dir = os.path.join(os.getcwd(), project_name)
        os.makedirs(project_dir, exist_ok=True)
        sys.stdout.write(f"Created project directory: {project_dir}\n")
        sys.stdout.flush()
        
        subprocess.run(["R", "-e", f"renv::init('{project_name}')"], check=True)
        
        if requirements_file and os.path.isfile(requirements_file):
            subprocess.run(["R", "-e", f"renv::restore('{requirements_file}')"], check=True)
            sys.stdout.write(f"Installed dependencies from {requirements_file}\n")
            sys.stdout.flush()
        else:
            sys.stdout.write("No requirements file provided or file does not exist.\n")
            sys.stdout.flush()

        sys.stdout.write(f"R environment for {project_name} is set up.\n")
        sys.stdout.flush()
    except subprocess.CalledProcessError as e:
        sys.stdout.write(f"Error while executing R commands: {str(e)}\n")
        sys.stdout.flush()
    except Exception as e:
        sys.stdout.write(f"Error: {str(e)}\n")
        sys.stdout.flush()
