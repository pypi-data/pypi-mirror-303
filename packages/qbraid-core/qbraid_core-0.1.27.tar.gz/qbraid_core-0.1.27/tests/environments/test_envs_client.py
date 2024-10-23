# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for the EnvironmentManagerClient class.

"""
from unittest.mock import MagicMock, patch

import pytest

from qbraid_core.exceptions import RequestsApiError
from qbraid_core.services.environments.client import EnvironmentManagerClient
from qbraid_core.services.environments.exceptions import EnvironmentServiceRequestError


@pytest.fixture
def mock_qbraid_session():
    """A fixture to mock qBraid session."""
    with patch("qbraid_core.session.QbraidSession", autospec=True) as mock:
        # Mock the necessary session methods here, e.g., get_user
        mock.return_value.get_user.return_value = {
            "personalInformation": {"organization": "qbraid", "role": "guest"}
        }
        yield mock


def test_create_environment_success():
    """Test successful environment creation."""
    client = EnvironmentManagerClient()
    environment_name = "TestEnv"
    environment_description = "A test environment."

    with (
        patch("qbraid_core.services.environments.is_valid_env_name", return_value=True),
        patch.object(client.session, "post") as mock_post,
    ):
        mock_post.return_value.json.return_value = {
            "slug": "test-env-slug",
            "name": environment_name,
            "description": environment_description,
        }

        result = client.create_environment(environment_name, environment_description)

        mock_post.assert_called_once()
        assert result["name"] == environment_name
        assert result["description"] == environment_description


def test_create_environment_invalid_name():
    """Test environment creation with an invalid name."""
    client = EnvironmentManagerClient()
    invalid_environment_name = "Invalid Name"

    with patch("qbraid_core.services.environments.is_valid_env_name", return_value=False):
        with pytest.raises(ValueError) as exc_info:
            client.create_environment(invalid_environment_name)

        assert "Invalid environment name" in str(exc_info.value)


def test_create_environment_description_too_long():
    """Test environment creation with a too long description."""
    client = EnvironmentManagerClient()
    environment_name = "ValidName"
    long_description = "x" * 301  # 301 characters long

    with patch("qbraid_core.services.environments.is_valid_env_name", return_value=True):
        with pytest.raises(ValueError) as exc_info:
            client.create_environment(environment_name, long_description)

        assert "Description is too long" in str(exc_info.value)


def test_create_environment_api_failure():
    """Test API failure during environment creation."""
    client = EnvironmentManagerClient()
    environment_name = "ValidName"

    with (
        patch("qbraid_core.services.environments.is_valid_env_name", return_value=True),
        patch.object(client.session, "post", side_effect=RequestsApiError),
    ):
        with pytest.raises(EnvironmentServiceRequestError) as exc_info:
            client.create_environment(environment_name)

        assert "Create environment request failed" in str(exc_info.value)


def test_create_environment_invalid_api_response():
    """Test invalid or incomplete data returned by the API."""
    client = EnvironmentManagerClient()
    environment_name = "ValidName"

    with (
        patch("qbraid_core.services.environments.is_valid_env_name", return_value=True),
        patch.object(client.session, "post") as mock_post,
    ):
        mock_post.return_value.json.return_value = {}  # Empty response

        with pytest.raises(EnvironmentServiceRequestError) as exc_info:
            client.create_environment(environment_name)

        assert "invalid environment data" in str(exc_info.value)


def test_delete_environment_with_valid_session():
    """Test deleting an environment with a valid session."""
    with patch("requests.Session.delete") as mock_delete:
        # Assuming delete_environment method successfully calls the session's delete method
        mock_delete.return_value = MagicMock(status_code=204)  # Simulate successful deletion

        client = EnvironmentManagerClient()  # Initializes with a valid mocked QbraidSession
        slug = "valid_slug12"
        client.delete_environment(slug)  # Attempt to delete an environment

        mock_delete.assert_called_once_with(f"/environments/{slug}")


def test_delete_environment_request_failure():
    """Test environment deletion handling when the delete request fails."""
    slug = "valid_slug12"
    with patch("requests.Session.delete") as mock_delete:
        mock_delete.side_effect = RequestsApiError("API request failed")

        client = EnvironmentManagerClient()  # Initializes with a valid mocked QbraidSession
        with pytest.raises(EnvironmentServiceRequestError):
            client.delete_environment(slug)

        mock_delete.assert_called_once_with(f"/environments/{slug}")
