import json
import os

CONFIG_FILE = "config.json"

default_config = {
    "source_channels": [],
    "destination_channels": [],
    "prefix": "",
    "suffix": "",
    "clean_links": False
}

def load_config():
    if not os.path.exists(CONFIG_FILE):
        save_config(default_config)
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)

def update_config(key, value):
    config = load_config()
    config[key] = value
    save_config(config)
    return config
