from reconfigure.configs import NSDConfig
from tests.configs.config_base_test import BaseConfigTest


class NSDConfigTest (BaseConfigTest):
    sources = {
        None: """
zone:
        name: "example.net"
        zonefile: "example.net.signed.zone"
        notify-retry: 5
"""
    }
    result = {
        "zones": [
            {
                "name": "example.net",
                "file": "example.net.signed.zone"
            }
        ]
    }

    config = NSDConfig


del BaseConfigTest
