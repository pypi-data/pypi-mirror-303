# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for functions that get environment path(s) data.

"""
import json
import os
from pathlib import Path
from unittest.mock import MagicMock, patch

from qbraid_core.services.environments.paths import get_default_envs_paths, installed_envs_data

skip_remote_tests: bool = os.getenv("QBRAID_RUN_REMOTE_TESTS", "False").lower() != "true"
REASON = "QBRAID_RUN_REMOTE_TESTS not set (requires configuration of qBraid storage)"


def test_get_default_envs_paths_with_env_var_set(monkeypatch):
    """Test the get_qbraid_envs_paths function when QBRAID_ENVS_PATH is set."""
    # Mocking QBRAID_ENVS_PATH with two paths for the test
    mock_path_1, mock_path_2 = "/path/to/envs1", "/path/to/envs2"
    mock_envs_path = mock_path_1 + os.pathsep + mock_path_2
    monkeypatch.setenv("QBRAID_ENVS_PATH", mock_envs_path)

    expected_paths = [Path(mock_path_1), Path(mock_path_2)]
    default_paths = get_default_envs_paths()
    assert (
        default_paths == expected_paths
    ), "Should return paths from QBRAID_ENVS_PATH environment variable"


def test_get_qbraid_envs_paths_with_no_env_var_set(monkeypatch):
    """Test the get_qbraid_envs_paths function when QBRAID_ENVS_PATH is not set."""
    # Removing QBRAID_ENVS_PATH to simulate it not being set
    monkeypatch.delenv("QBRAID_ENVS_PATH", raising=False)

    expected_paths = [str(Path.home() / ".qbraid" / "environments")]
    default_paths = [str(path) for path in get_default_envs_paths()]
    assert (
        default_paths == expected_paths
    ), "Should return the default path when QBRAID_ENVS_PATH is not set"


def mock_path_iterdir(paths):
    """Helper to create a mock for Path.iterdir, returning mock Path objects for a list of paths."""
    return [MagicMock(spec=Path, name=path, is_dir=MagicMock(return_value=True)) for path in paths]


def test_no_environments_installed():
    """Test when no environments are installed."""
    mock_paths = [MagicMock(spec=Path, iterdir=MagicMock(return_value=[]))]
    with patch(
        "qbraid_core.services.environments.paths.get_default_envs_paths", return_value=mock_paths
    ):
        installed, aliases = installed_envs_data()
        assert not installed, "Installed environments should be empty"
        assert not aliases, "Aliases should be empty"


def test_installed_envs_data_basic():
    """Test gettting installed environments data"""
    mock_env_paths = [Path("/path/to/qbraid/envs/qbraid_000000"), Path("/path/to/qbraid/envs/env2")]
    mock_dir_entry1 = MagicMock(is_dir=MagicMock(return_value=True), name="qbraid_000000")
    mock_dir_entry2 = MagicMock(is_dir=MagicMock(return_value=True), name="env2")

    with (
        patch(
            "qbraid_core.services.environments.paths.get_default_envs_paths",
            return_value=mock_env_paths,
        ),
        patch("pathlib.Path.iterdir", side_effect=[[mock_dir_entry1], [mock_dir_entry2]]),
        patch("qbraid_core.services.environments.paths.is_valid_slug", return_value=True),
        patch("builtins.open", MagicMock()),
        patch("json.load", MagicMock(return_value={"name": "alias_for_env2"})),
    ):
        installed, aliases = installed_envs_data()
        # pylint: disable-next=protected-access
        installed_names_list = [value._mock_name for value in installed.values()]
        aliases_names_list = list(aliases.keys())
        assert "qbraid_000000" in installed_names_list
        assert "alias_for_env2" in aliases_names_list


def test_installed_envs_data_state_json_handling():
    """Test handling of state.json files in installed environments."""
    mock_env_path = Path("/path/to/qbraid/envs/env1")
    mock_dir_entry = MagicMock(is_dir=MagicMock(return_value=True), name="env_with_state")
    mock_state_json_path = MagicMock(exists=MagicMock(return_value=True))

    with (
        patch(
            "qbraid_core.services.environments.paths.get_default_envs_paths",
            return_value=[mock_env_path],
        ),
        patch("pathlib.Path.iterdir", return_value=[mock_dir_entry]),
        patch("qbraid_core.services.environments.paths.is_valid_slug", return_value=True),
        patch("builtins.open", MagicMock()) as mock_open,
        patch(
            "json.load", MagicMock(side_effect=json.JSONDecodeError("Expecting value", "", 0))
        ) as mock_json_load,
        patch.object(Path, "exists", return_value=True),
        patch.object(Path, "__truediv__", return_value=mock_state_json_path),
    ):
        installed, _ = installed_envs_data()

        mock_open.assert_called()
        mock_json_load.assert_called()
        # pylint: disable-next=protected-access
        installed_names_list = [value._mock_name for value in installed.values()]
        # Check fallback alias naming when JSON parsing fails
        assert (
            "env_with_state" in installed_names_list
        ), "Should fallback to name based on dir when JSON parsing fails"
