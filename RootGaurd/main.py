import threading
import subprocess
import time
import os

from monitor.privilege_monitor import privilege_monitor
from monitor.process_monitor import process_monitor
from monitor.network_monitor import network_monitor
from integrity.file_integrity import file_integrity_check

LOG_FILE = "logs/attacks.log"


def log_event(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {message}\n")


def start_kernel_check():
    try:
        log_event("Starting kernel integrity check")
        script_path = os.path.join(os.path.dirname(__file__), "integrity", "kernel_check.sh")
        subprocess.Popen(["bash", script_path], 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
    except Exception as e:
        log_event(f"Kernel check failed: {e}")


def start_thread(target, name):
    thread = threading.Thread(target=target, daemon=True, name=name)
    thread.start()
    log_event(f"{name} started")


if __name__ == "__main__":

    print("\n🔐 RootGuard Security System Starting...\n")
    log_event("RootGuard started")

    # Ensure logs directory exists
    os.makedirs("logs", exist_ok=True)

    # Start kernel-level checks
    start_kernel_check()

    # Start all monitoring modules
    start_thread(privilege_monitor, "Privilege Escalation Monitor")
    start_thread(process_monitor, "Hidden Process Monitor")
    start_thread(network_monitor, "Network Monitor")
    start_thread(file_integrity_check, "File Integrity Monitor")

    print("✅ All security modules are running")
    print("📡 Monitoring system for root malware and attacks...\n")

    # Keep main process alive
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        log_event("RootGuard stopped by user")
        print("\n🛑 RootGuard stopped")

