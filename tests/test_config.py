import os
import json
import pytest
from unittest.mock import patch, mock_open
from src.config.config import (
    ensure_config_dir,
    load_config,
    save_config,
    get_api_key,
    set_api_key
)

@pytest.fixture
def mock_config_dir():
    """Create temporary configuration directory"""
    test_dir = os.path.join(os.path.dirname(__file__), './.tmp/')
    with patch('src.config.config.CONFIG_DIR', test_dir):
        with patch('src.config.config.CONFIG_FILE', os.path.join(test_dir, 'config.json')):
            yield test_dir

def test_ensure_config_dir(mock_config_dir):
    """Test ensuring configuration directory exists"""
    ensure_config_dir()
    assert os.path.exists(mock_config_dir)

def test_load_config_empty():
    """Test loading non-existent configuration file"""
    with patch('os.path.exists', return_value=False):
        config = load_config()
        assert config == {}

def test_load_config_with_data():
    """Test loading existing configuration file"""
    mock_data = {"api_key": "test-key"}
    mock_file = mock_open(read_data=json.dumps(mock_data))
    with patch('os.path.exists', return_value=True):
        with patch('builtins.open', mock_file):
            config = load_config()
            assert config == mock_data

def test_save_config_success(mock_config_dir):
    """Test successful configuration save"""
    config_data = {"api_key": "new-test-key"}
    assert save_config(config_data) == True
    config_file = os.path.join(mock_config_dir, 'config.json')
    assert os.path.exists(config_file)
    with open(config_file, 'r') as f:
        saved_data = json.load(f)
    assert saved_data == config_data

def test_get_api_key_not_set():
    """Test getting unset API key"""
    with patch('src.config.config.load_config', return_value={}):
        assert get_api_key() is None

def test_get_api_key_set():
    """Test getting set API key"""
    test_key = "test-api-key"
    with patch('src.config.config.load_config', return_value={"api_key": test_key}):
        assert get_api_key() == test_key

def test_set_api_key_success():
    """Test successful API key setting"""
    test_key = "new-api-key"
    with patch('src.config.config.save_config', return_value=True):
        assert set_api_key(test_key) == True

def test_set_api_key_failure():
    """Test API key setting failure"""
    test_key = "new-api-key"
    with patch('src.config.config.save_config', return_value=False):
        assert set_api_key(test_key) == False