# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for qBraid magic commands.

"""

import os
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from IPython.testing.globalipapp import get_ipython

from qbraid_core.system.magic import SysMagics


@pytest.fixture(scope="module")
def ipython():
    """Return an instance of the IPython shell."""
    return get_ipython()


@pytest.fixture
def sys_magics(ipython):
    """Return an instance of the SysMagics class."""
    return SysMagics(shell=ipython)


def test_qbraid_magic(sys_magics):
    """Test the qbraid magic command."""
    test_command = "--version"
    expected_command = ["qbraid", "--version"]
    mock_path = Path("/test/path")

    with patch.dict("os.environ", {}, clear=True):
        with patch("subprocess.run") as mock_run:
            mock_run.return_value = MagicMock(returncode=0)

            with patch("os.getenv", side_effect=lambda k: str(mock_path) if k == "PATH" else None):
                with patch("os.environ.pop") as mock_pop:
                    sys_magics.qbraid(test_command)

                    mock_run.assert_called_once_with(expected_command, check=True)

                    mock_pop.assert_any_call("QBRAID_CLI_SHOW_PROGRESS", None)

                    assert os.environ["PATH"] == str(mock_path)
                    assert os.environ["QBRAID_CLI_SHOW_PROGRESS"] == "false"
