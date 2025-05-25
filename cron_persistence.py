import os

def check_existing_crontab():
    """Return current crontab content or empty string if none exists."""
    try:
        output = os.popen("crontab -l").read()
        return output
    except exception as e:
        print(f"[!] Error reading crontab: {e}")

def add_cron_job():
    """Add a harmless @reboot cron job if it doesn't already exist."""
    cron_job = "@reboot echo 'Cron-based persistence active!' >> ~/cron_persistence_log.txt"
    existing = check_existing_crontab()

    if cron_job in existing:
        print("[+] Cron job already exists")
    else:
        print("[+] Adding new cron job...")
        updated_crontab = existing + cron_job + "\n"
        os.system(f"(echo '{updated_crontab}') | crontab -")
        print("[!] Cron job added successfully.")

def remove_cron_job():
    """Remove the cron job if it exists."""
    cron_job = "@reboot echo 'Cron-based persistence active!' >> ~/cron_persistence_log.txt"
    existing = check_existing_crontab()

    if cron_job not in existing:
        print("[*] No matching cron job found to remove.")
    else:
        updated_crontab + "\n".join(line for line in existing.split.lines() if line.strip() != cron_job)
        os.system(f"(echo '{updated_crontab}') | crontab -")
        print("[+] Cron job removed successfully.")

def show_crontab():
    print("\n[*] Current crontab entires:")
    os.system("crontab -l")

def main():
    print("== Cron Persistence Simulator ==")
    print("[1] Add cron job")
    print("[2] Remove cron job")
    print("[3] View current crontab")
    choice = input("Select an option: ")

    if choice == "1":
        add_cron_job()
    elif choice == "2":
        remove_cron_job()
    elif choice == "3":
        show_crontab()
    else:
        print("[!] Invalid option.")

if __name__ == "__main__":
    main()
