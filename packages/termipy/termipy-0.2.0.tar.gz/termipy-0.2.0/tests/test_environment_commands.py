import os
import pytest
from termipy.environment_commands import SetPyEnvCommand, SetREnvCommand

@pytest.mark.skip(reason="Requires system-level changes")
def test_setpyenv_command(tmpdir):
    setpyenv_cmd = SetPyEnvCommand()
    env_name = "test_env"
    setpyenv_cmd.execute([env_name])
    assert os.path.exists(os.path.join(str(tmpdir), env_name, "bin", "python"))

@pytest.mark.skip(reason="Requires R installation")
def test_setrenv_command(tmpdir):
    setrenv_cmd = SetREnvCommand()
    env_name = "test_r_env"
    setrenv_cmd.execute([env_name])
    assert os.path.exists(os.path.join(str(tmpdir), env_name, ".Rprofile"))