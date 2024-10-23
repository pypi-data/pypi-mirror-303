import pytest
from unittest.mock import patch, MagicMock
from twilio.rest import Client as TwilioRestClient
from strideutils.twilio_connector import TwilioClient
from strideutils.stride_config import Environment as e

@pytest.fixture(autouse=True)
def reset_twilio_client():
    TwilioClient._instance = None
    yield
    TwilioClient._instance = None

@pytest.fixture
def mock_twilio_rest_client():
    with patch('strideutils.twilio_connector.Client') as mock:
        mock_instance = MagicMock()
        mock.return_value = mock_instance
        yield mock_instance

@pytest.fixture(autouse=True)
def mock_env_vars():
    with patch('strideutils.twilio_connector.get_env_or_raise') as mock_get_env:
        def side_effect(arg):
            if arg == e.TWILIO_ACCOUNT_ID:
                return 'fake_account_id'
            elif arg == e.TWILIO_API_TOKEN:
                return 'fake_api_token'
            elif arg == e.TWILIO_ALERTS_NUMBER:
                return 'fake_alert_numbers'
            return 'dummy_value'
        mock_get_env.side_effect = side_effect
        yield mock_get_env

@pytest.fixture
def twilio_client(mock_twilio_rest_client, mock_env_vars):
    client = TwilioClient()
    return client

def test_twilio_client_singleton():
    client1 = TwilioClient()
    client2 = TwilioClient()
    assert client1 is client2

def test_twilio_client_initialization(twilio_client, mock_env_vars):
    assert twilio_client.account_id == 'fake_account_id'
    assert twilio_client.api_token == 'fake_api_token'
    assert twilio_client.alert_numbers == 'fake_alert_numbers'
    assert isinstance(twilio_client.client, MagicMock)

def test_call_single_recipient(twilio_client, mock_twilio_rest_client):
    with patch('strideutils.twilio_connector.config') as mock_config:
        mock_config.PHONE_NUMBERS = {'recipient': '+12223334444'}
        mock_config.TWILIO_ALERTS_NUMBER = '+15556667777'

        twilio_client.call("Test message", "recipient")

        expected_twiml = "<Response><Say>Test message</Say></Response>"
        mock_twilio_rest_client.calls.create.assert_called_once_with(
            to='+12223334444',
            from_='+15556667777',
            twiml=expected_twiml
        )

def test_call_multiple_recipients(twilio_client, mock_twilio_rest_client):
    with patch('strideutils.twilio_connector.config') as mock_config:
        mock_config.PHONE_NUMBERS = {
            'recipient1': '+12223334444',
            'recipient2': '+13334445555'
        }
        mock_config.TWILIO_ALERTS_NUMBER = '+15556667777'

        twilio_client.call("Test message", ["recipient1", "recipient2"])

        expected_twiml = "<Response><Say>Test message</Say></Response>"
        assert mock_twilio_rest_client.calls.create.call_count == 2
        mock_twilio_rest_client.calls.create.assert_any_call(
            to='+12223334444',
            from_='+15556667777',
            twiml=expected_twiml
        )
        mock_twilio_rest_client.calls.create.assert_any_call(
            to='+13334445555',
            from_='+15556667777',
            twiml=expected_twiml
        )

def test_call_invalid_recipient(twilio_client, mock_twilio_rest_client):
    with patch('strideutils.twilio_connector.config') as mock_config:
        mock_config.PHONE_NUMBERS = {}

        with pytest.raises(KeyError):
            twilio_client.call("Test message", "invalid_recipient")
