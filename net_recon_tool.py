import ipaddress
import socket
import concurrent.futures
import argparse

def is_host_up(ip, port=80, timeout=1):
    try:
        with socket.create_connection((str(ip), port), timeout=timeout):
            return str(ip)
    except:
        return None

def scan_port(ip, port, timeout=1):
    try:
        with socket.create_connection((ip, port), timeout=timeout) as sock:
            return port
    except:
        return None

def scan_ports_for_hosts(ip, ports):
    print(f"\n[~] Scanning ports on {ip}...")
    open_ports = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in ports}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                print(f"[+] Port {result} open on {ip}")
                open_ports.append(result)
    return open_ports

def scan_subnet(subnet, probe_port, port_range):
    print(f"\n[*] Scanning subnet {subnet} for live hosts...\n")
    network = ipaddress.IPv4Network(subnet, strict=False)
    live_hosts = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(is_host_up, str(ip), probe_port): ip for ip in network.hosts()}
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                print(f"[+] Host up: {result}")
                live_hosts.append(result)

    for ip in live_hosts:
        scan_ports_for_hosts(ip, port_range)

    print(f"\n[+] Recon complete. {len(live_hosts)} live host(s) scanned.\n")
    return live_hosts

def main():
    parser = argparse.ArgumentParser(description="Network Recon Tool (Host + Port Scanner)")
    parser.add_argument("subnet", help="Subnet to scan (e.g. 10.0.0.0/24)")
    parser.add_argument("-p", "--probe-port", type=int, default=80, help="Port used to test if hosts are up (default: 80)")
    parser.add_argument("--start-port", type=int, default=1, help="Start of port range to scan (default: 1)")
    parser.add_argument("--end-port", type=int, default=1024, help="End of port range to scan (default: 1024)")
    args = parser.parse_args()

    port_range = list(range(args.start_port, args.end_port + 1))
    scan_subnet(args.subnet, args.probe_port, port_range)

if __name__ == "__main__":
    main()
