import os
import json
from pathlib import Path

CONFIG_DIR = os.path.expanduser("~/.deepchat")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def ensure_config_dir():
    """Ensure configuration directory exists"""
    os.makedirs(CONFIG_DIR, exist_ok=True)

def load_config():
    """Load configuration"""
    ensure_config_dir()
    if not os.path.exists(CONFIG_FILE):
        return {}
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading config: {e}")
        return {}

def save_config(config):
    """Save configuration"""
    ensure_config_dir()
    try:
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving config: {e}")
        return False

def get_api_key():
    """Get API key"""
    config = load_config()
    return config.get('api_key')

def set_api_key(api_key):
    """Set API key"""
    config = load_config()
    config['api_key'] = api_key
    return save_config(config)