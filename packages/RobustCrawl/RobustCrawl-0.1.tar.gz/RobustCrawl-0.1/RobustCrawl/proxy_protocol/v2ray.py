import subprocess
import json
class V2rayProxyManager:
    def create_v2ray_config(self, proxy):
        outbound = {
            "tag": proxy["name"],
            "protocol": "vmess",
            "settings": {
                "vnext": [
                    {
                        "address": proxy["server"],
                        "port": proxy["port"],
                        "users": [
                            {
                                "id": proxy["uuid"],
                                "alterId": proxy["alterId"],
                                "security": proxy["cipher"],
                            }
                        ]
                    }
                ]
            },
        }
        return outbound
