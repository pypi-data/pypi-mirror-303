# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for qBraid core helper functions related to system executables.

"""
import os
import platform
import stat
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from qbraid_core.system.executables import (
    _extract_python_version,
    get_active_python_path,
    is_exe,
    python_paths_equivalent,
)


def test_get_active_python_path_same_as_sys_executable():
    """
    Test that get_active_python_path() matches sys.executable when executed with
    the same Python executable.

    """
    with (
        patch("qbraid_core.system.executables.sys.executable", "/opt/conda/bin/python"),
        patch("qbraid_core.system.executables.subprocess.run") as mock_run,
    ):
        mock_run.return_value = MagicMock(returncode=0, stdout="/opt/conda/bin/python\n")

        assert get_active_python_path() == Path(
            sys.executable
        ), "The path should match sys.executable"


def test_get_active_python_path_virtualenv():
    """
    Test that get_active_python_path() returns the same path as
    `which python` in a virtual environment.

    """
    virtual_env_path = "/home/jovyan/.qbraid/environments/mynewe_kc5ixd/pyenv/bin/python"
    with (
        patch("qbraid_core.system.executables.sys.executable", "/opt/conda/bin/python"),
        patch("qbraid_core.system.executables.subprocess.run") as mock_run,
    ):
        mock_run.return_value = MagicMock(returncode=0, stdout=f"{virtual_env_path}\n")

        active_path = get_active_python_path()
        expected_path = Path(virtual_env_path)
        assert str(active_path) == str(
            expected_path
        ), "The path should match the virtual environment's Python"


@pytest.mark.parametrize(
    "version_string, expected_version",
    [
        ("python", None),
        ("python2", 2),
        ("python2.7", 2),
        ("python3.8", 3),
        ("python 3.9", 3),
        ("python-3.10", 3),
    ],
)
def test_extract_python_version(version_string, expected_version):
    """Test that the Python version is correctly extracted from a string."""
    assert _extract_python_version(version_string) == expected_version


@pytest.mark.skipif(sys.platform == "win32", reason="Test only for Unix-like systems")
@pytest.mark.parametrize(
    "path1, path2, expected",
    [
        # Test cases where paths should be equivalent
        ("/usr/bin/python3.7", "/usr/bin/python", True),  # Not passing on Windows?
        (Path("/usr/bin/python3.7"), Path("/usr/bin/python"), True),
        ("/usr/bin/python3.7", Path("/usr/bin/python"), True),
        ("/opt/pythonista3/bin/python-3.8", "/opt/pythonista3/bin/python", True),
        # Test cases where paths should not be equivalent
        ("/usr/bin/python3.7", "/usr/local/bin/python", False),
        (Path("/usr/bin/python3.8"), "/usr/local/bin/python2.7", False),
        ("/opt/pythonista3/bin/python3.10", "/opt/pythonista3/bin/python2.7", False),
        ("/bin/python3.9-debug/bin/python3.9", "/bin/python-debug/bin/python2", False),
    ],
)
def test_python_paths_equivalence(path1, path2, expected):
    """Test that python paths are considered equivalent correctly."""
    assert python_paths_equivalent(path1, path2) == expected


def test_is_exe_file_does_not_exist(monkeypatch):
    # Setup: Ensure the file does not exist
    monkeypatch.setattr(Path, "exists", MagicMock(return_value=False))
    assert not is_exe("/nonexistent/file")


def test_is_exe_file_exists_but_is_directory(monkeypatch):
    """Test that is_exe returns False when the path is a directory."""
    monkeypatch.setattr(Path, "exists", MagicMock(return_value=True))
    monkeypatch.setattr(Path, "is_file", MagicMock(return_value=False))
    assert not is_exe("/path/to/directory")


def test_is_exe_no_access_rights(monkeypatch):
    """Test that is_exe returns False when the file has no access rights."""
    monkeypatch.setattr(Path, "exists", MagicMock(return_value=True))
    monkeypatch.setattr(Path, "is_file", MagicMock(return_value=True))
    with patch("os.access", return_value=False):
        assert not is_exe("/path/to/locked/file")


@pytest.mark.parametrize(
    "system, extension, expected",
    [
        ("Windows", ".exe", True),
        ("Windows", ".bat", True),
        ("Windows", ".cmd", True),
        ("Windows", ".sh", False),
        ("Linux", ".sh", True),
        ("Linux", ".exe", False),
    ],
)
def test_os_specific_checks(monkeypatch, system, extension, expected):
    """Test is_exe against different file extensions in varrying operating systems."""
    monkeypatch.setattr(Path, "exists", MagicMock(return_value=True))
    monkeypatch.setattr(Path, "is_file", MagicMock(return_value=True))
    monkeypatch.setattr(platform, "system", MagicMock(return_value=system))
    test_path = f"/fake/path/file{extension}"

    if system == "Windows":
        with patch("os.access", return_value=True):
            assert is_exe(test_path) is expected
    else:
        with patch("os.access") as mock_access:

            def side_effect(path, mode):
                if mode & os.X_OK:
                    return True
                if mode == os.F_OK:
                    return True
                return False

            mock_access.side_effect = side_effect

            # Mock stat result to simulate executable permission
            st_mode = stat.S_IXUSR if expected else 0
            with patch.object(Path, "stat", return_value=MagicMock(st_mode=st_mode)):
                assert is_exe(test_path) is expected


def test_executable_flag_check_unix(monkeypatch):
    """Test that is_exe returns True for an executable file on Unix."""
    monkeypatch.setattr(platform, "system", MagicMock(return_value="Linux"))
    monkeypatch.setattr(Path, "exists", MagicMock(return_value=True))
    monkeypatch.setattr(Path, "is_file", MagicMock(return_value=True))
    with (
        patch("os.access", return_value=True),
        patch.object(Path, "stat", return_value=MagicMock(st_mode=stat.S_IXUSR)),
    ):
        assert is_exe("/unix/executable/file")


def test_non_executable_file_unix(monkeypatch):
    """Test that is_exe returns False for a non-executable file on Unix."""
    monkeypatch.setattr(platform, "system", MagicMock(return_value="Linux"))
    monkeypatch.setattr(Path, "exists", MagicMock(return_value=True))
    monkeypatch.setattr(Path, "is_file", MagicMock(return_value=True))
    with patch("os.access", return_value=False):
        assert not is_exe("/unix/non-executable/file")
