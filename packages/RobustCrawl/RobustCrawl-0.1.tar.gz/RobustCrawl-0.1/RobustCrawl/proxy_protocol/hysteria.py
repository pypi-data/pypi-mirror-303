import subprocess
import json
class HysteriaProxyManager:
    def create_v2ray_config(self, proxy):
        """    - { name: 日本H01直连Hysteria2, server: hyfnjp01.156786.xyz, port: 8081, udp: true, skip-cert-verify: false, sni: hyfnjp01.156786.xyz, type: hysteria2, password: 338764e4-661c-48e6-8036-c9956ff3afce }"""
        outbound = {
            "protocol": "hysteria2",
            "tag": proxy["name"],
            "settings": {
                "servers": [
                    {
                        "address": proxy["server"],
                        "port": proxy["port"],
                    }
                ]
            }
        }
        return outbound