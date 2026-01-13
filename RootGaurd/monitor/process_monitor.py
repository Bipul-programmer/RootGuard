import psutil
import time

def process_monitor():
    while True:
        hidden = []
        for pid in psutil.pids():
            try:
                psutil.Process(pid)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                hidden.append(pid)
        
        if hidden:
            print("[ALERT] Hidden Processes Detected:", hidden)
        
        time.sleep(5)
