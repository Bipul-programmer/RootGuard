import psutil
import socket
import time
import logging

# Trusted IPs / networks (can be extended)
TRUSTED_IPS = [
    "127.0.0.1",
    "192.168.",
    "10.",
    "172.16."
]

def is_trusted(ip):
    for net in TRUSTED_IPS:
        if ip.startswith(net):
            return True
    return False

def network_monitor():
    while True:
        try:
            for conn in psutil.net_connections(kind="inet"):
                try:
                    if conn.raddr and conn.pid:
                        proc = psutil.Process(conn.pid)
                        uid = proc.uids().effective
                        remote_ip, remote_port = conn.raddr

                        if uid == 0 and not is_trusted(remote_ip):
                            print(f"[ALERT] Root process making external connection")
                            print(f" PID       : {conn.pid}")
                            print(f" Process   : {proc.name()}")
                            print(f" Remote IP : {remote_ip}")
                            print(f" Port      : {remote_port}")
                            print("-" * 40)

                except (psutil.NoSuchProcess, psutil.AccessDenied):
                    continue
        except (psutil.AccessDenied, PermissionError) as e:
            print(f"[ERROR] Network monitor access denied: {e}")
            time.sleep(10)
            continue

        time.sleep(5)

