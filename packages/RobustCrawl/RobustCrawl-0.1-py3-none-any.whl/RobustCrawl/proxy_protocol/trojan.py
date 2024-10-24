import subprocess
import json


class TrojanProxyManager:
    def create_v2ray_config(self, proxy):
        outbound = {
            "protocol": "trojan",
            "tag": proxy["name"],
            "settings": {
                "servers": [
                    {
                        "address": proxy["server"],
                        "port": proxy["port"],
                        "password": proxy["password"],
                    }
                ]
            },
        }
        return outbound
