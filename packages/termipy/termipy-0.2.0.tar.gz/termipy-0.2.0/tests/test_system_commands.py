import os
import pytest
from termipy.system_commands import (
    EchoCommand, GetWdCommand, SetWdCommand, TypeOfCommand, ClearCommand,
    DiskUsageCommand, ExitCommand
)

def test_echo_command(capsys):
    echo_cmd = EchoCommand()
    echo_cmd.execute(["Hello", "World"])
    captured = capsys.readouterr()
    assert "Hello World" in captured.out

def test_getwd_command(capsys):
    getwd_cmd = GetWdCommand()
    getwd_cmd.execute([])
    captured = capsys.readouterr()
    assert os.getcwd() in captured.out

def test_setwd_command(tmpdir):
    setwd_cmd = SetWdCommand()
    original_dir = os.getcwd()
    setwd_cmd.execute([str(tmpdir)])
    assert os.getcwd() == str(tmpdir)
    os.chdir(original_dir)  # Change back to the original directory

def test_typeof_command(capsys):
    typeof_cmd = TypeOfCommand()
    typeof_cmd.execute(["echo"])
    captured = capsys.readouterr()
    assert "echo is a shell builtin" in captured.out

def test_clear_command(capsys):
    clear_cmd = ClearCommand()
    clear_cmd.execute([])
    captured = capsys.readouterr()
    assert "\033[2J\033[H" in captured.out  # ANSI escape sequence for clearing screen

def test_diskusage_command(capsys, tmpdir):
    diskusage_cmd = DiskUsageCommand()
    diskusage_cmd.execute([str(tmpdir)])
    captured = capsys.readouterr()
    assert "Disk usage for" in captured.out
    assert "Total:" in captured.out
    assert "Used:" in captured.out
    assert "Free:" in captured.out

def test_exit_command():
    exit_cmd = ExitCommand()
    assert exit_cmd.execute([]) is False