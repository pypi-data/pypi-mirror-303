import pytest
from unittest.mock import patch, MagicMock
from strideutils.redis_connector import RedisClient

@pytest.fixture(autouse=True)
def reset_redis_client():
    RedisClient._reset()
    yield
    RedisClient._reset()

@pytest.fixture
def mock_redis():
    with patch('strideutils.redis_connector.redis.Redis') as mock:
        mock_instance = MagicMock()
        mock.return_value = mock_instance
        yield mock_instance

@pytest.fixture(autouse=True)
def mock_env_vars():
    """
       This function is a patch for `get_env_or_raise` to make it return a dummy value and random port.
       for the new environment variables added to `stride_config.py`.
       So anywhere we do a call to `get_env_or_raise` in these tests, it will return
       a `dummy_value`.
    """
    with patch('strideutils.redis_connector.get_env_or_raise') as mock_get_env:
        def side_effect(arg):
            if 'PORT' in arg:
                return '6379'  # Default Redis port
            return 'dummy_value'
        mock_get_env.side_effect = side_effect
        yield mock_get_env

@pytest.fixture
def redis_client(mock_redis, mock_env_vars):
    client = RedisClient()
    return client

def test_redis_client_singleton():
    client1 = RedisClient()
    client2 = RedisClient()
    assert client1 is client2

def test_init_with_specific_dbs():
    client = RedisClient(['public', 'frontend'])
    assert set(client._dbs.keys()) == {'public', 'frontend'}

def test_init_with_invalid_db():
    with pytest.raises(ValueError, match="Invalid Redis database names"):
        RedisClient(['invalid_db'])

def test_get_db(redis_client):
    assert isinstance(redis_client.get_db('public'), MagicMock)

def test_get_db_no_name_single_db():
    client = RedisClient(['public'])
    assert client.get_db() == client._dbs['public']

def test_get_db_no_name_multiple_dbs():
    client = RedisClient(['public', 'frontend'])
    with pytest.raises(ValueError, match="Database name must be specified if multiple databases are configured"):
        client.get_db()

def test_get(redis_client, mock_redis):
    mock_redis.get.return_value = 'test_value'
    assert redis_client.get('test_key', 'public') == 'test_value'

def test_get_multiple_keys(redis_client, mock_redis):
    mock_redis.mget.return_value = ['value1', 'value2']
    assert redis_client.get_multiple_keys(['key1', 'key2'], 'public') == ['value1', 'value2']

def test_get_all_keys(redis_client, mock_redis):
    mock_redis.scan.side_effect = [(1, ['key1']), (0, ['key2'])]
    assert redis_client.get_all_keys('public') == ['key1', 'key2']

def test_set(redis_client, mock_redis):
    redis_client.set('test_key', 'test_value', 'public')
    redis_client._dbs['public'].set.assert_called_once_with('test_key', 'test_value')

def test_set_keys(redis_client, mock_redis):
    test_dict = {'key1': 'value1', 'key2': 'value2'}
    mock_pipeline = MagicMock()
    redis_client._dbs['public'].pipeline.return_value.__enter__.return_value = mock_pipeline
    redis_client.set_keys(test_dict, 'public', 'prefix_')
    mock_pipeline.set.assert_any_call('prefix_key1', 'value1')
    mock_pipeline.set.assert_any_call('prefix_key2', 'value2')
    mock_pipeline.execute.assert_called_once()
