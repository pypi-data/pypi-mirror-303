"""Test example module."""

import pytest


@pytest.mark.usefixtures("with_context")
def test_running_drift(request_mock, endpoint, token):
    """Test the POST request to create a drift run was sent to server."""
    assert request_mock.post.call_count == 1
    url = f"{endpoint}/drift"
    assert request_mock.post.call_args[1]["url"] == url
    assert request_mock.post.call_args[1]["headers"] == {
        "Authorization": f"Bearer {token}"
    }
    assert request_mock.post.call_args[1]["json"] == {
        "model_id": "model_1",
        "status": "Running",
    }


@pytest.mark.usefixtures("after_context")
def test_completed_drift(request_mock, endpoint, token, monitor):
    """Test the PUT request to complete a drift run was sent to server."""
    assert request_mock.put.call_count == 1
    url = f"{endpoint}/drift/{monitor.drift['id']}"
    assert request_mock.put.call_args[1]["url"] == url
    assert request_mock.put.call_args[1]["headers"] == {
        "Authorization": f"Bearer {token}"
    }
    assert request_mock.put.call_args[1]["json"] == {
        **monitor.drift,
        "status": "Completed",
        "concept_drift": {"drift": True, "parameters": {"threshold": 0.5}},
        "data_drift": {"drift": True, "parameters": {"threshold": 0.5}},
    }


@pytest.mark.usefixtures("error_context")
def test_failed_drift(request_mock, endpoint, token, monitor):
    """Test the PUT request to fail a drift run was sent to server."""
    assert request_mock.put.call_count == 1
    url = f"{endpoint}/drift/{monitor.drift['id']}"
    assert request_mock.put.call_args[1]["url"] == url
    assert request_mock.put.call_args[1]["headers"] == {
        "Authorization": f"Bearer {token}"
    }
    assert request_mock.put.call_args[1]["json"] == {
        **monitor.drift,
        "status": "Failed",
    }
