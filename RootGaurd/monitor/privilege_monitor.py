import psutil
import time

while True:
    for process in psutil.process_iter(['pid','username','uids','name']):
        try:
            if p.info['uids'] and p.info['uids'].effective == 0:
                if p.info['username'] != 'root':
                    print(f"[ALERT] Privilege Escalation: {p.info}")
        except:
            pass
    time.sleep(2)
