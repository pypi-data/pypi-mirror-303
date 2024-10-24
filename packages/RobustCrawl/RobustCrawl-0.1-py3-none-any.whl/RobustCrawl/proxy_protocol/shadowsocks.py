import subprocess
class ShadowsocksProxyManager:
    def create_proxy_command(self, proxy, port):
        cmd = [
            "ss-local",
            "-s",
            proxy["server"],
            "-p",
            str(proxy["port"]),
            "-l",
            str(port),
            "-k",
            proxy["password"],
            "-m",
            proxy["cipher"],
        ]

        # 添加插件配置
        if "plugin" in proxy and "plugin-opts" in proxy:
            cmd.extend(
                [
                    "--plugin",
                    "obfs-local",
                    "--plugin-opts",
                    f"obfs={proxy['plugin-opts']['mode']};obfs-host={proxy['plugin-opts']['host']}",
                ]
            )
        return cmd

    def create_v2ray_config(self, proxy):
        outbound = {
            "protocol": "shadowsocks",
            "tag": proxy["name"],
            "settings": {
                "servers": [
                    {
                        "address": proxy["server"],
                        "port": proxy["port"],
                        "method": proxy["cipher"],
                        "password": proxy["password"],
                        "udp": proxy["udp"],
                    }
                ]
            },
        }
        return outbound