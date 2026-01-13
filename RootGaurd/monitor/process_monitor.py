import psutil

hidden = []
for pid in psutil.pids():
    try:
        psutil.Process(pid)
    except:
        hidden.append(pid)

if hidden:
    print("[ALERT] Hidden Processes Detected:", hidden)
