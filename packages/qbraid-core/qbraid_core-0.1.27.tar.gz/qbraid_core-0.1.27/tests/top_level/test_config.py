# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for the load_config function in the configure app.

"""

import configparser
from pathlib import Path
from unittest.mock import patch

import pytest

from qbraid_core.config import ConfigError, load_config, save_config, update_config_option


@pytest.fixture
def config():
    config = configparser.ConfigParser()
    config.add_section("test_section")
    return config


def test_update_config_option_new_value(config):
    value = "new_value"
    result_config = update_config_option(config, "test_section", "test_option", value)
    assert result_config.get("test_section", "test_option") == value


def test_update_config_option_existing_value(config):
    value = "existing_value"
    config.set("test_section", "test_option", value)
    result_config = update_config_option(config, "test_section", "test_option", value)
    assert result_config.get("test_section", "test_option") == value


def test_update_config_option_update_value(config):
    initial_value = "initial_value"
    new_value = "new_value"
    config.set("test_section", "test_option", initial_value)
    result_config = update_config_option(config, "test_section", "test_option", new_value)
    assert result_config.get("test_section", "test_option") == new_value


def test_update_config_option_none_value(config):
    initial_value = "initial_value"
    config.set("test_section", "test_option", initial_value)
    result_config = update_config_option(config, "test_section", "test_option", None)
    assert result_config.get("test_section", "test_option") == initial_value


@patch("qbraid_core.config.str", side_effect=TypeError)
def test_update_config_option_invalid_value(mock_str, config):
    with pytest.raises(ValueError):
        update_config_option(config, "test_section", "test_option", 123)


def test_load_config_success():
    """Test loading configuration successfully."""
    # Call the function under test
    with (
        patch.object(Path, "home", return_value=Path("/fake/home")),
        patch.object(configparser.ConfigParser, "read"),
    ):
        config = load_config()
        # Assert the config is an instance of configparser.ConfigParser
        assert isinstance(config, configparser.ConfigParser), "Config should be loaded successfully"


def test_load_config_file_not_found_error():
    """Test loading configuration when the file is not found."""
    with (
        patch.object(Path, "home", return_value=Path("/fake/home")),
        patch.object(configparser.ConfigParser, "read") as mock_config_parser,
    ):
        mock_config_parser.side_effect = FileNotFoundError("File not found")

        # Assert QbraidException is raised when the config file is not found
        with pytest.raises(ConfigError):
            load_config()


def test_load_config_permission_error():
    """Test loading configuration when there's a permission error."""
    with (
        patch.object(Path, "home", return_value=Path("/fake/home")),
        patch.object(configparser.ConfigParser, "read") as mock_config_parser,
    ):
        mock_config_parser.side_effect = PermissionError("Permission denied")

        # Assert QbraidException is raised when there's a permission error
        with pytest.raises(ConfigError):
            load_config()


def test_load_config_parsing_error():
    """Test loading configuration when there's a parsing error."""
    with (
        patch.object(Path, "home", return_value=Path("/fake/home")),
        patch.object(configparser.ConfigParser, "read") as mock_config_parser,
    ):
        mock_config_parser.side_effect = configparser.Error("Parsing error")

        # Assert QbraidException is raised when there's a parsing error
        with pytest.raises(ConfigError):
            load_config()


@pytest.mark.parametrize("section,key,value", [("test", "qbraid", "cli")])
def test_save_config(section, key, value):
    """Test functionality of save configuration"""
    mock_config = configparser.ConfigParser()
    mock_config.add_section(section)
    mock_config.set(section, key, value)

    qbraid_path = Path.home() / ".qbraid"
    qbraidrc_path_tmp = qbraid_path / "qbraidrc.tmp"

    if qbraidrc_path_tmp.exists():
        qbraidrc_path_tmp.unlink()

    try:
        save_config(mock_config, filepath=qbraidrc_path_tmp)

        assert qbraid_path.exists(), "The .qbraid directory was not created."
        assert qbraidrc_path_tmp.exists(), "The qbraidrc file was not created."

        # Verify the contents of the qbraidrc file
        config_read_back = configparser.ConfigParser()
        config_read_back.read(qbraidrc_path_tmp)
        assert config_read_back.get(section, key) == value, "The file content is not as expected."
    finally:
        if qbraidrc_path_tmp.exists():
            qbraidrc_path_tmp.unlink()
