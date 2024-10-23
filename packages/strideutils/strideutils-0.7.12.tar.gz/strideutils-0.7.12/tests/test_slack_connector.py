import pytest
from unittest.mock import patch, MagicMock
from slack_sdk.errors import SlackApiError

from strideutils.slack_connector import SlackClient


@pytest.fixture
def mock_webclient():
    with patch('strideutils.slack_connector.WebClient') as mock_client:
        yield mock_client.return_value


@pytest.fixture
def slack_client(mock_webclient):
    with patch('strideutils.slack_connector.get_env_or_raise', return_value='fake_token'):
        client = SlackClient()
        client.client = mock_webclient  # Replaced the real WebClient with a mock, to not send to slack at all.
        yield client


def test_slack_client_singleton():
    with patch('strideutils.slack_connector.WebClient'):
        client1 = SlackClient()
        client2 = SlackClient()
        assert client1 is client2


def test_post_message_string(slack_client, mock_webclient):
    mock_webclient.chat_postMessage.return_value = {"ts": "1234567890.123456"}

    thread_ts = slack_client.post_message("Hello, World!", "#alerts-debug")

    mock_webclient.chat_postMessage.assert_called_once_with(
        channel="#alerts-debug",
        text="Hello, World!",
        thread_ts=None,
        username=None
    )
    assert thread_ts == "1234567890.123456"


def test_post_message_list(slack_client, mock_webclient):
    mock_webclient.chat_postMessage.side_effect = [
        {"ts": "1234567890.123456"},
        {"ts": "1234567890.123457"},
        {"ts": "1234567890.123458"}
    ]

    thread_ts = slack_client.post_message(["Message 1", "Message 2", "Message 3"], "#alerts-debug")

    assert mock_webclient.chat_postMessage.call_count == 3
    assert thread_ts == "1234567890.123456"


def test_upload_file(slack_client, mock_webclient):
    mock_webclient.files_upload_v2.return_value = {
        "file": {"permalink": "https://slack.com/file/123456"}
    }

    file_link = slack_client.upload_file("test.txt", "Hello, World!")

    mock_webclient.files_upload_v2.assert_called_once_with(
        filename="test.txt",
        content="Hello, World!"
    )
    assert file_link == "https://slack.com/file/123456"


def test_post_message_error(slack_client, mock_webclient):
    mock_webclient.chat_postMessage.side_effect = SlackApiError("Error", {"error": "invalid_auth"})

    with pytest.raises(SlackApiError):
        slack_client.post_message("Hello, World!", "#alerts-debug")


@patch('strideutils.slack_connector.os.environ.get')
def test_channel_override(mock_environ_get, slack_client, mock_webclient):
    mock_environ_get.return_value = "#override-channel"
    mock_webclient.chat_postMessage.return_value = {"ts": "1234567890.123456"}

    slack_client.post_message("Hello, World!", "#alerts-debug")

    mock_webclient.chat_postMessage.assert_called_once_with(
        channel="#override-channel",
        text="Hello, World!",
        thread_ts=None,
        username=None
    )
