# TermiPy
```
████████╗███████╗██████╗ ███╗   ███╗██╗██████╗ ██╗   ██╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║██╔══██╗╚██╗ ██╔╝
   ██║   █████╗  ██████╔╝██╔████╔██║██║██████╔╝ ╚████╔╝ 
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██╔═══╝   ╚██╔╝  
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║        ██║   
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝        ╚═╝   
```

[![PyPI version](https://badge.fury.io/py/termipy.svg)](https://badge.fury.io/py/termipy)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/termipy.svg)](https://pypi.org/project/termipy/)


TermiPy is a simple command-line shell providing essential shell functionalities such as directory navigation, file listing, and command execution. It is designed to be minimal, lightweight, and highly extensible for users looking to interact with their file systems through a custom terminal interface.

## 🚀 Features

- 📂 **File and Directory Operations**: Navigate directories, list files, create, delete, and rename files/directories.
- 🖥️ **Command Execution**: Execute shell commands directly through TermiPy.
- 📊 **System Resource Monitoring**: View real-time CPU, memory, disk, and network usage statistics.
- 🐍 **Environment Setup**: Set up Python and R environments easily.
- 🌐 **Cross-Platform**: Works on Linux, macOS, and Windows.

## 📦 Installation
1. Clone the repository or download the script and then install using,

   ```bash
   pip install .
   ```

2. Run the script using Python 3:

   ```bash
   termipy
   ```

   or 

   ```bash
   PATH="/usr/bin:/usr/local/bin" termipy
   ```

## 🚀 Usage

Run TermiPy using the following command:

```shellscript
termipy
```

If you encounter any PATH issues, you can use:

```shellscript
PATH="/usr/bin:/usr/local/bin" termipy
```

## 📚 Available Commands

| Command | Description
|-----|-----
| `echo <message>` | Print a message to the terminal
| `getwd`, `ls` | Get current working directory
| `setwd <directory>` | Change directory
| `typeof <command>` | Show command type
| `clear` (aliases: `cls`, `clr`) | Clear the screen
| `tree [directory]` | Show directory structure
| `create <path>` | Create file or directory
| `search <filename>` | Search for a file
| `setpyenv [name] [version]` | Create Python virtual environment
| `setrenv [name]` | Initialize R environment
| `about <file>` | Show file details
| `commands` | List all available commands
| `delete <path>` | Delete file or directory
| `rename <old> <new>` | Rename file or directory
| `diskusage [path]` | Show disk usage
| `permissions <file>` | Show file permissions
| `resource`, `resources`, `stats` | Show system resource usage
| `help` | Display help information
| `exit` | Exit TermiPy


For more information on a specific command, use: `<command> -h`

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check [issues page](https://github.com/pr2tik1/termipy/issues).

## 📝 License

This project is [MIT](https://opensource.org/licenses/MIT) licensed.

## 👤 Author

**Pratik Kumar**

- Website: [pr2tik1](https://bento.me/pr2tik1)
- Twitter: [@pr2tik1](https://twitter.com/pr2tik1)
- Github: [@pr2tik1](https://github.com/pr2tik1)
- LinkedIn: [@pratik-kumar](https://linkedin.com/in/pratik-kumar04)


## 🙏 Show your support

Give a ⭐️ if this project helped you!