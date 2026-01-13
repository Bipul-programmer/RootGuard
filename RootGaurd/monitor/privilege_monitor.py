import psutil
import time

def privilege_monitor():
    while True:
        for process in psutil.process_iter(['pid','username','uids','name']):
            try:
                if process.info['uids'] and process.info['uids'].effective == 0:
                    if process.info['username'] != 'root':
                        print(f"[ALERT] Privilege Escalation: {process.info}")
            except (psutil.NoSuchProcess, psutil.AccessDenied, KeyError):
                continue
        time.sleep(2)
