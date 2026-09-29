#!/usr/bin/env python3
"""
Educational TCP port scanner.

Use only against systems you own or have explicit permission to test.
"""

import argparse
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


def scan_port(host, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            if sock.connect_ex((host, port)) == 0:
                try:
                    service = socket.getservbyport(port, "tcp")
                except OSError:
                    service = "unknown"
                return port, service
    except (socket.timeout, OSError):
        pass
    return None


def main():
    parser = argparse.ArgumentParser(
        description="Scan a TCP port range on an authorized host."
    )
    parser.add_argument("host", help="Hostname or IP address to scan")
    parser.add_argument("-s", "--start", type=int, default=1, help="Starting port")
    parser.add_argument("-e", "--end", type=int, default=1024, help="Ending port")
    parser.add_argument("-t", "--timeout", type=float, default=0.5, help="Timeout in seconds")
    parser.add_argument("-w", "--workers", type=int, default=50, help="Concurrent workers")
    args = parser.parse_args()

    if not (1 <= args.start <= args.end <= 65535):
        parser.error("Ports must satisfy 1 <= start <= end <= 65535.")

    try:
        ip = socket.gethostbyname(args.host)
    except socket.gaierror:
        parser.error(f"Could not resolve host: {args.host}")

    print(f"Target: {args.host} ({ip})")
    print(f"Scanning TCP ports {args.start}-{args.end}...")

    open_ports = []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(scan_port, ip, port, args.timeout): port
            for port in range(args.start, args.end + 1)
        }
        for future in as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)

    for port, service in sorted(open_ports):
        print(f"[+] {port}/tcp OPEN - {service}")

    print(f"\nScan complete. Open ports found: {len(open_ports)}")


if __name__ == "__main__":
    main()
