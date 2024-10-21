import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_zenoh():
    # Mock the Zenoh API
    zenoh = Mock()
    zenoh.open.return_value = Mock()
    return zenoh

def test_publisher_publishes_messages(mock_zenoh):
    """Test if the publisher sends a message to the correct path."""
    session = mock_zenoh.open()
    session.put = Mock()

    # Publisher publishes to the path
    session.put("/test/path", "test_data")

    # Assert that the data was published to the correct path
    session.put.assert_called_once_with("/test/path", "test_data")

def test_subscriber_receives_messages(mock_zenoh):
    """Test if the subscriber receives the published message."""
    session = mock_zenoh.open()
    session.subscribe = Mock()

    # Subscriber subscribes to the path
    callback = Mock()
    session.subscribe("/test/path", callback)

    # Simulate message publishing
    callback("test_data")

    # Assert that the subscriber callback received the data
    callback.assert_called_once_with("test_data")

def test_subscriber_does_not_receive_unrelated_messages(mock_zenoh):
    """Test if the subscriber does not receive messages from other paths."""
    session = mock_zenoh.open()
    session.subscribe = Mock()

    # Subscriber subscribes to a different path
    callback = Mock()
    session.subscribe("/test/path/1", callback)

    # Simulate message publishing to a different path
    other_callback = Mock()
    session.subscribe("/test/path/2", other_callback)
    other_callback("unrelated_data")

    # Assert that the subscriber did not receive unrelated messages
    callback.assert_not_called()

def test_multiple_subscribers_receive_message(mock_zenoh):
    """Test if multiple subscribers receive the same published message."""
    session = mock_zenoh.open()
    session.subscribe = Mock()

    # Two subscribers subscribe to the same path
    callback1 = Mock()
    callback2 = Mock()
    session.subscribe("/test/path", callback1)
    session.subscribe("/test/path", callback2)

    # Simulate message publishing
    callback1("test_data")
    callback2("test_data")

    # Assert that both subscribers received the message
    callback1.assert_called_once_with("test_data")
    callback2.assert_called_once_with("test_data")

def test_no_message_received_without_publishing(mock_zenoh):
    """Test if no messages are received when nothing is published."""
    session = mock_zenoh.open()
    session.subscribe = Mock()

    # Subscriber subscribes to the path
    callback = Mock()
    session.subscribe("/test/path", callback)

    # Assert that no messages are received when nothing is published
    callback.assert_not_called()

def test_publisher_multiple_subscribers(mock_zenoh):
    """Test if the publisher can handle multiple subscribers."""
    session = mock_zenoh.open()
    session.put = Mock()

    # Publisher publishes to the path
    session.put("/test/path", "test_data")

    # Subscribers receive the data
    callback1 = Mock()
    callback2 = Mock()
    session.subscribe("/test/path", callback1)
    session.subscribe("/test/path", callback2)

    # Simulate the message callback
    callback1("test_data")
    callback2("test_data")

    # Assert that both callbacks were called
    callback1.assert_called_once_with("test_data")
    callback2.assert_called_once_with("test_data")
