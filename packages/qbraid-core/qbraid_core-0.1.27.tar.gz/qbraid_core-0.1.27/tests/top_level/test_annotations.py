# Copyright (c) 2024, qBraid Development Team
# All rights reserved.

"""
Unit tests for annotations (i.e. decorators).

"""
import pytest

from qbraid_core.annotations import deprecated


@deprecated
def mock_deprecated_function() -> None:
    """A mock function that does nothing."""
    pass


@deprecated("Please use another_function() instead.")
def mock_deprecated_function_with_message() -> None:
    """A mock function that does nothing."""
    pass


def test_deprecated_decorator():
    """Test that the deprecated decorator emits a warning."""
    with pytest.warns(
        DeprecationWarning, match="Call to deprecated function mock_deprecated_function."
    ):
        mock_deprecated_function()


def test_deprecated_decorator_with_message():
    """Test that the deprecated decorator emits a warning with a custom message."""
    expected_warning = r"Call to deprecated function mock_deprecated_function_with_message\. Please use another_function\(\) instead\."
    with pytest.warns(DeprecationWarning, match=expected_warning):
        mock_deprecated_function_with_message()
