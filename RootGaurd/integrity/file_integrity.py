import hashlib, os

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
    with open(path,'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

baseline = {f: checksum(f) for f in critical}

while True:
    for f in critical:
        if checksum(f) != baseline[f]:
            print("[ALERT] Binary Modified:", f)

