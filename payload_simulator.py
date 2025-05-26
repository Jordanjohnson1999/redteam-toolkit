import os
import time
from datetime import datetime

PAYLOAD_PATH = os.path.expanduser("~/fake_payload.sh")
LOG_FILE = os.path.expanduser("~/payload_simulator_log.txt")

def drop_payload():
    with open(PAYLOAD_PATH, "w") as f:
        f.write("#!/bin/bash\necho 'Fake payload executed~'")
    os.chmod(PAYLOAD_PATH, 0o755)
    print(f"[+] Payload written to {PAYLOAD_PATH}")

def simulate_execution():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Simulated payload executed at {PAYLOAD_PATH}\n"
    with open(LOG_FILE, "a") as log:
        log.write(log_entry)
    print("[+] Simulated payload 'executed' and logged.")

def cleanup():
    if os.path.exists(PAYLOAD_PATH):
        os.remove(PAYLOAD_PATH)
        print("[+] No payload file to remove.")

def main():
    print("== Payload Simulator ==")
    print("[1] Drop payload")
    print("[2] Simulate execution")
    print("[3] Cleanup payload")
    choice = input("Choose an option: ")

    if choice == "1":
        drop_payload()
    elif choice == "2":
        simulate_execution()
    elif choice == "3":
        cleanup()
    else:
        print("[!] Invalid selection.")

if __name__ == "__main__":
    main()
