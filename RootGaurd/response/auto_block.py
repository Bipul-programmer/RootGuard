import os
import signal

def kill(pid):
    """Kill a process by PID. Requires appropriate permissions."""
    try:
        os.kill(int(pid), signal.SIGTERM)  # Try graceful termination first
        print(f"[INFO] Sent SIGTERM to process {pid}")
    except ProcessLookupError:
        print(f"[WARNING] Process {pid} not found")
    except PermissionError:
        print(f"[ERROR] Permission denied to kill process {pid}")
    except ValueError:
        print(f"[ERROR] Invalid PID: {pid}")