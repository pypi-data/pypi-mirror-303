import pytest
from termipy.utility_commands import HelpCommand, AboutCommand, CommandsCommand

def test_help_command(capsys):
    help_cmd = HelpCommand()
    help_cmd.execute([])
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out

def test_about_command(capsys, tmpdir):
    about_cmd = AboutCommand()
    test_file = tmpdir.join("test_file.txt")
    test_file.write("Test content")
    about_cmd.execute([str(test_file)])
    captured = capsys.readouterr()
    assert "File:" in captured.out
    assert "Size:" in captured.out
    assert "Permissions:" in captured.out
    assert "Last modified:" in captured.out

def test_commands_command(capsys):
    commands_cmd = CommandsCommand()
    commands_cmd.execute([])
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert "echo" in captured.out
    assert "getwd" in captured.out
    assert "setwd" in captured.out