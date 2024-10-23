"""
This module serves as the entry point for the TermiPy shell.
"""

from termipy.shell import TermiPy
from termipy.utils import setup_readline

def main():
    setup_readline()
    TermiPy().run()

if __name__ == "__main__":
    main()