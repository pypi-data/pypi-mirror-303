import os
import pytest
from termipy.file_commands import (
    TreeCommand, CreateCommand, SearchCommand, DeleteCommand, RenameCommand,
    PermissionsCommand
)

@pytest.fixture
def temp_dir(tmpdir):
    return tmpdir.mkdir("test_dir")

def test_tree_command(temp_dir, capsys):
    tree_cmd = TreeCommand()
    tree_cmd.execute([str(temp_dir)])
    captured = capsys.readouterr()
    assert str(temp_dir) in captured.out
    assert "└──" in captured.out

def test_create_command(temp_dir):
    create_cmd = CreateCommand()
    file_path = os.path.join(temp_dir, "test_file.txt")
    create_cmd.execute([file_path])
    assert os.path.exists(file_path)

def test_search_command(temp_dir, capsys):
    # Create a file to search for
    file_path = os.path.join(temp_dir, "searchable.txt")
    with open(file_path, 'w') as f:
        f.write("Test content")

    search_cmd = SearchCommand()
    search_cmd.execute(["searchable.txt"])
    captured = capsys.readouterr()
    assert file_path in captured.out

def test_delete_command(temp_dir):
    # Create a file to delete
    file_path = os.path.join(temp_dir, "to_delete.txt")
    with open(file_path, 'w') as f:
        f.write("Delete me")

    delete_cmd = DeleteCommand()
    delete_cmd.execute([file_path])
    assert not os.path.exists(file_path)

def test_rename_command(temp_dir):
    # Create a file to rename
    old_path = os.path.join(temp_dir, "old_name.txt")
    new_path = os.path.join(temp_dir, "new_name.txt")
    with open(old_path, 'w') as f:
        f.write("Rename me")

    rename_cmd = RenameCommand()
    rename_cmd.execute([old_path, new_path])
    assert not os.path.exists(old_path)
    assert os.path.exists(new_path)

def test_permissions_command(temp_dir, capsys):
    # Create a file to check permissions
    file_path = os.path.join(temp_dir, "check_perms.txt")
    with open(file_path, 'w') as f:
        f.write("Check my permissions")

    permissions_cmd = PermissionsCommand()
    permissions_cmd.execute([file_path])
    captured = capsys.readouterr()
    assert "Permissions for" in captured.out
    assert file_path in captured.out