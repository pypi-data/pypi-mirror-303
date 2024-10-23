# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for create_local_venv function to test the
creation of the local virtual environment.

"""
import sys
from unittest.mock import patch

from qbraid_core.services.environments.create import create_local_venv


def test_create_local_venv_success(tmp_path):
    """Test the successful creation of a virtual environment and PS1 name swap."""
    prompt = "test_env"
    slug_path = tmp_path / "test_slug"
    slug_path.mkdir()

    with (
        patch("qbraid_core.services.environments.create.subprocess.run") as mock_run,
        patch("qbraid_core.services.environments.create.replace_str") as mock_replace_str,
        patch(
            "qbraid_core.services.environments.create.set_include_sys_site_pkgs_value"
        ) as mock_set_include_sys_site_pkgs_value,
        patch("qbraid_core.services.environments.create.update_state_json") as mock_update_state,
    ):
        create_local_venv(slug_path, prompt)
        venv_path = slug_path / "pyenv"

        # Verify subprocess was called correctly
        mock_run.assert_called_once_with([sys.executable, "-m", "venv", str(venv_path)], check=True)
        mock_set_include_sys_site_pkgs_value.assert_called_once_with(True, venv_path / "pyvenv.cfg")

        # Verify PS1 name was attempted to be replaced
        scripts_path = venv_path / ("Scripts" if sys.platform == "win32" else "bin")
        activate_files = (
            ["activate.bat", "Activate.ps1"]
            if sys.platform == "win32"
            else ["activate", "activate.csh", "activate.fish"]
        )
        for file in activate_files:
            if (scripts_path / file).exists():
                mock_replace_str.assert_any_call("(pyenv)", f"({prompt})", str(scripts_path / file))

        # Verify update_install_status was called with success
        mock_update_state.assert_called_once_with(slug_path, 1, 1)


def test_create_local_venv_failure(tmp_path):
    """Test the behavior when subprocess fails to create the virtual environment."""
    prompt = "test_env"
    slug_path = tmp_path / "test_slug"
    slug_path.mkdir()

    with (
        patch("qbraid_core.services.environments.create.subprocess.run") as mock_run,
        patch("qbraid_core.services.environments.create.logger.error") as mock_logger_error,
        patch("qbraid_core.services.environments.create.update_state_json") as mock_update_state,
    ):
        mock_run.side_effect = Exception("Test Error")

        create_local_venv(slug_path, prompt)

        # Verify logger captured the exception
        mock_logger_error.assert_called_once()

        # Verify update_install_status was called with failure
        mock_update_state.assert_called_once_with(slug_path, 1, 0, message="Test Error")
