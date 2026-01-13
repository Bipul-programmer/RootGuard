import hashlib
import os
import time

critical = [
    # Authentication & Privilege Escalation
    "/bin/su",
    "/usr/bin/sudo",
    "/bin/login",
    "/usr/bin/passwd",
    "/usr/bin/chsh",
    "/usr/bin/chfn",

    # Shells (Persistence & Root Shells)
    "/bin/bash",
    "/bin/sh",
    "/usr/bin/zsh",

    # Process & System Visibility (Often Trojanized)
    "/bin/ps",
    "/bin/ls",
    "/bin/netstat",
    "/usr/bin/top",
    "/usr/bin/htop",
    "/usr/bin/id",
    "/usr/bin/whoami",

    # Process & Permission Control
    "/bin/kill",
    "/bin/chmod",
    "/bin/chown",
    "/bin/mount",
    "/bin/umount",

    # Remote Access & Data Movement
    "/usr/bin/ssh",
    "/usr/bin/scp",

    # Persistence & Automation
    "/usr/bin/crontab",

    # Scripting Runtimes (Payload Execution)
    "/usr/bin/python3",
    "/usr/bin/perl"
]

def checksum(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

def file_integrity_check():
    baseline = {}
    for f in critical:
        try:
            if os.path.exists(f):
                baseline[f] = checksum(f)
        except (FileNotFoundError, PermissionError) as e:
            print(f"[WARNING] Cannot create baseline for {f}: {e}")

    while True:
        for f in critical:
            try:
                if f in baseline and os.path.exists(f):
                    current_checksum = checksum(f)
                    if current_checksum != baseline[f]:
                        print(f"[ALERT] Binary Modified: {f}")
                        print(f"  Old hash: {baseline[f][:16]}...")
                        print(f"  New hash: {current_checksum[:16]}...")
            except (FileNotFoundError, PermissionError):
                continue
        time.sleep(10)

