import json

from reconfigure.configs import AjentiConfig
from tests.configs.config_base_test import BaseConfigTest


class AjentiConfigTest (BaseConfigTest):
    sources = {
        None: """{
    "authentication": false,
    "bind": {
        "host": "0.0.0.0",
        "port": 8000
    },
    "language": null,
    "enable_feedback": true,
    "installation_id": null,
    "users": {
        "test": {
            "configs": { "a": "{}" },
            "password": "sha512",
            "permissions": [
                "section:Dash"
            ]
        }
    },
    "ssl": {
        "enable": false,
        "certificate_path": ""
    }
}
"""
    }
    result = {
        'authentication': False,
        'enable_feedback': True,
        'installation_id': None,
        'language': None,
        'http_binding': {'host': '0.0.0.0', 'port': 8000},
        'ssl': {'certificate_path': '', 'enable': False},
        'users': {'test': {
            'configs': {'a': {'data': {}, 'name': 'a'}},
            'email': None,
            'name': 'test',
            'password': 'sha512',
            'permissions': ['section:Dash']
        }}
    }

    config = AjentiConfig

    stringify_filter = staticmethod(lambda x: json.loads(str(x)))


del BaseConfigTest
