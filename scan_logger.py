import os
from datetime import datetime

target = input("Enter domain or IP to scan: ")
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"[{timestamp}) Scanned target: {target}\n"

with open("scan_history.txt", "a") as f:
    f.write(log_entry)

os.system(f"nmap -f {target}")
