

from reconfigure.configs import BIND9Config
from tests.configs.config_base_test import BaseConfigTest


class BIND9ConfigTest (BaseConfigTest):
    sources = {
        None: """
zone "asd" {
    type master;
    file "/file";
};

"""
    }
    result = {
        "zones": [
            {
                "type": "master",
                "name": "asd",
                "file": "/file"
            }
        ]
    }

    config = BIND9Config


del BaseConfigTest
