import os

def kill(pid) :
    os.system(f"sudo kill -9 {pid}")