import pytest
from termipy import ResourceUsageCommand

def test_resource_usage_command_init():
    cmd = ResourceUsageCommand()
    assert isinstance(cmd, ResourceUsageCommand)

def test_resource_usage_command_execute(capsys):
    cmd = ResourceUsageCommand()
    result = cmd.execute([])
    assert result is True
    captured = capsys.readouterr()
    assert "CPU Usage" in captured.out
    assert "Memory Usage" in captured.out
    assert "Disk Usage" in captured.out
    assert "Network Usage" in captured.out
    assert "Process Usage" in captured.out