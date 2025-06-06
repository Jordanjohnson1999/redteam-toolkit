# Port_reporter.py
# Save open port info with description and timestamp

from datetime import datetime

PORT_DESCRIPTIONS = {
    21: "FTP (File Transfer Protocol)",
    22: "SSh (Secure shell)",
    23: "Telnet (unencrypted remote login)",
    25: "SMTP (Email sending)",
    53: "DNS (Domain Name System)",
    80: "HTTP (Web traffic)",
    110: "POP3: (Email retrieval)",
    139: "NetBIOS (Windows file sharing)",
    143: "IMAP (Email retrieval)",
    443: "HTTPS (Secure web traffic)",
    445: "SMB (Windows file sharing)",
    3306: "MySQL database",
    3389: "RDP (Remote desktop)",
    8080: "HTTP alternate (proxy/web servers)",
    31337: "Backdoor/Easter egg in walware (Elite port)"
}

def generate_report(ports):
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"_port_report_{now}.txt"

    with open(filename , "w") as f:
        f.write("== Port Report ==\n")
        f.write(f"Generated: {now}\n\n")
        for port in ports:
            port = int(port)
            desc = PORT_DESCRIPTIONS.get(port, "Unknown or uncommon port")
            f.write(f"[{port}] > {desc}\n")

    print(f"\n[+] Report saved as: {filename}")

if __name__ == "__main__":
    user_input = input("Enter open ports (comma-seperated): ")
    try:
        ports = [p.strip() for p in user_input.split(",")]
        generate_report(ports)
    except ValueError:
        print("Invalid input. Please enter comma_seperated numbers.")
