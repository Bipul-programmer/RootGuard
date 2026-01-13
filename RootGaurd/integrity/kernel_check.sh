#!/bin/bash

echo "[*] Checking loaded kernel modules..."
lsmod > /tmp/lsmod_out.txt

echo "[*] Checking /proc/modules..."
cat /proc/modules > /tmp/proc_modules_out.txt

echo "[*] Comparing module lists..."
diff /tmp/lsmod_out.txt /tmp/proc_modules_out.txt && \
echo "[OK] No hidden kernel modules detected" || \
echo "[ALERT] Possible hidden kernel module detected"

echo "[*] Checking dmesg for kernel warnings..."
dmesg | tail -20