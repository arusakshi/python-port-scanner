# 🔎 Python TCP Port Scanner

A beginner-friendly **TCP port scanner written in Python** for learning network security, socket programming, and basic reconnaissance concepts.

## ✨ Features

- TCP port scanning using Python sockets
- Custom start and end port ranges
- Configurable connection timeout
- Concurrent scanning with a thread pool
- Basic TCP service-name detection
- DNS hostname resolution
- Command-line interface

## 🛠️ Technologies

- Python 3
- Socket Programming
- TCP/IP
- Networking Fundamentals
- Threading / Concurrent Execution

## 📥 Installation

Clone the repository:

```bash
git clone https://github.com/arusakshi/python-port-scanner.git
cd python-port-scanner
```

No external packages are required.

## 🚀 Usage

Scan the default ports 1–1024:

```bash
python port_scanner.py 127.0.0.1
```

Scan a custom range:

```bash
python port_scanner.py 127.0.0.1 --start 20 --end 100
```

Change the timeout:

```bash
python port_scanner.py 127.0.0.1 -s 1 -e 100 -t 1
```

## 📌 Example Output

```text
Target: localhost (127.0.0.1)
Scanning TCP ports 1-1024...
[+] 22/tcp OPEN - ssh
[+] 80/tcp OPEN - http

Scan complete. Open ports found: 2
```

## 🎯 Learning Objectives

This project demonstrates:

- TCP connection concepts
- Python socket programming
- Port and service identification
- Basic network reconnaissance
- Concurrent task execution
- Command-line argument handling

## ⚠️ Ethical Use

Use this scanner **only on systems you own or where you have explicit authorization to perform security testing**. Do not scan public, organizational, or third-party systems without permission.

## 👩‍💻 Author

**Sakshi Aru**  
Cybersecurity & Digital Forensics Student
