import socket
import subprocess

def get_ip(hostname):
	try:
		ip = socket.gethostbyname(hostname)
		print(f"[+} IP address of {hostname}: {ip}")
		return ip
	except socket.gaierror:
		print("[-] Unable to resolve hostname.")
		return None

def scan_common_ports(ip):
	print(f"[*] Scanning ports on {ip}...")
	common_ports = [22, 80, 443, 8080]
	for port in common_ports:
		result = subprocess.run(
			["nc", "-zv", ip str(port)],
			capture_output=True,
			text=True
		)
		if "succeeded" in result.strderr or "open" in result.strderr:
			print(f"[+] Port {port} is open.")
		else:
			print(f"[-] Port {port} is closed or filtered.")

def main():
	target = input("Enter a hostname or IP to scan: ")
	ip = get_ip(target)
	if ip:
		scan_common_ports(ip)

if__name__ == "__main__":
	main()
