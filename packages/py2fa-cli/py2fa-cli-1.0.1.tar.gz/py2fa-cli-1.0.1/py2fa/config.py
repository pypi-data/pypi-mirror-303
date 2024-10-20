"""Configuration module for py2fa."""

import json
import os
import stat

from xdg import BaseDirectory


def _is_world_accessible(path):
    return os.stat(path).st_mode & stat.S_IRWXO


def load_secrets():
    """Load TOTP secrets from a configuration file."""

    cfg_path = BaseDirectory.load_first_config('py2fa/secrets.json')
    if cfg_path is None:
        print('ERR: Secrets file does not exist!')
        return None

    if _is_world_accessible(cfg_path):
        print('ERR: Secrets file is world-accessible, change its permissions first.')
        return None

    try:
        with open(cfg_path, encoding='utf-8') as cfg:
            return json.load(cfg)
    except PermissionError:
        print('ERR: Not permitted to access secrets file, verify permissions!')
        return None
    except json.JSONDecodeError:
        print('ERR: Failed to decode secrets file, verify JSON format!')
        return None
