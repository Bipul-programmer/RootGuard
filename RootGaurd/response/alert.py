from datetime import datetime

def alert(msg):
    with open("logs/attacks.log","a") as f:
        f.write(f"{datetime.now()} - {msg}\n")