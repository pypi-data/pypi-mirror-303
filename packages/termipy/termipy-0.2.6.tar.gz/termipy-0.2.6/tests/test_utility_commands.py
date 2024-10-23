import pytest
from termipy.utility_commands import HelpCommand, CommandsCommand

def test_help_command(capsys):
    help_cmd = HelpCommand()
    help_cmd.execute([])
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out


def test_commands_command(capsys):
    commands_cmd = CommandsCommand()
    commands_cmd.execute([])
    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert "echo" in captured.out
    assert "getwd" in captured.out
    assert "setwd" in captured.out