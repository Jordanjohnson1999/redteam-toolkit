import os
import subprocess
import csv
from datetime import datetime

def ping_sweep(subnet, filename="ping_results.csv"):
        results = []
        print(f"Pinging {subnet}.0/24 at {datetime.now()}")
        for i in range(1, 255):
            ip = f"{subnet}.{i}"
            try:
                response = subprocess.run(
                    ["ping", "-c", "1", "W", "1", ip],
                    capture_output=True,
                    text=True)

                status = "up" if response.returncode == 0 else "down"
                print(f"{ip}: {status}")
                results.append([ip, status, str(datetime.now())])
            except Exception as e:
                print(f"Error pinging {ip}: {e}")

        try:
            with open(filename, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["IP", "Status", "Time"])
                writer.writerows(results)
            print(f"Saved to {filename}")
        except Exception as e:
            print(f"Error saving: {e}")

if __name__ == "__main__":
    subnet = input("Enter subnet (e.g., 192.168.1): ")
    ping_sweep(subnet)
