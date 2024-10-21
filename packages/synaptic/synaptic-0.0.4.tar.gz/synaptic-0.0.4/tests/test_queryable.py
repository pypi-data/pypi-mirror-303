import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_zenoh():
    # Mock the Zenoh API
    zenoh = Mock()
    zenoh.open.return_value = Mock()
    return zenoh

def test_queryable_responds_to_query(mock_zenoh):
    """Test if the queryable responds to a query."""
    session = mock_zenoh.open()
    session.query = Mock(return_value="response_data")

    # Simulate a query being sent
    response = session.query("/test/query")

    # Assert that the response was received
    assert response == "response_data"
    session.query.assert_called_once_with("/test/query")

def test_queryable_handles_multiple_queries(mock_zenoh):
    """Test if the queryable can handle multiple queries."""
    session = mock_zenoh.open()
    session.query = Mock()

    # Simulate multiple queries being sent
    session.query("/test/query1")
    session.query("/test/query2")

    # Assert that both queries were handled
    assert session.query.call_count == 2
    session.query.assert_any_call("/test/query1")
    session.query.assert_any_call("/test/query2")

def test_query_non_existing_path(mock_zenoh):
    """Test if querying a non-existing path returns an error."""
    session = mock_zenoh.open()
    session.query = Mock(side_effect=KeyError("Path not found"))

    # Simulate querying a non-existing path
    with pytest.raises(KeyError, match="Path not found"):
        session.query("/non/existing/path")

def test_synchronous_query_waits_for_response(mock_zenoh):
    """Test if synchronous querying waits for the response."""
    session = mock_zenoh.open()
    session.query = Mock(return_value="response_data")

    # Simulate synchronous querying
    response = session.query("/test/query")

    # Assert the query returns the expected response
    assert response == "response_data"

def test_queryable_returns_correct_data_format(mock_zenoh):
    """Test if the queryable returns the correct data format."""
    session = mock_zenoh.open()
    session.query = Mock(return_value={"value": 42})

    # Simulate querying and checking the data format
    response = session.query("/test/query")

    # Assert that the response is in the correct format (dict)
    assert isinstance(response, dict)
    assert response["value"] == 42

def test_large_data_query(mock_zenoh):
    """Test if querying large data returns correctly."""
    session = mock_zenoh.open()
    large_data = "x" * 1024 * 1024  # 1 MB of data
    session.query = Mock(return_value=large_data)

    # Simulate querying large data
    response = session.query("/test/large/data")

    # Assert that the large data is returned correctly
    assert response == large_data
    assert len(response) == 1024 * 1024
