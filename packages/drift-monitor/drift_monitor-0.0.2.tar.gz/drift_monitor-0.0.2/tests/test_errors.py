"""Test example module."""

import pytest


def test_concept_context(monitor):
    """Test the method concept raises out of context error."""
    with pytest.raises(RuntimeError) as excinfo:
        monitor.concept(True, {"threshold": 0.5})
    assert str(excinfo.value) == "Drift monitor context not started."


def test_data_context(monitor):
    """Test the method concept raises out of context error."""
    with pytest.raises(RuntimeError) as excinfo:
        monitor.data(True, {"threshold": 0.5})
    assert str(excinfo.value) == "Drift monitor context not started."
