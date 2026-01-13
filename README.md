# RootGuard 🔐

A comprehensive cybersecurity monitoring system designed to detect and prevent root-level malware attacks, privilege escalations, and suspicious system activities.

## Features

- **Privilege Escalation Monitoring**: Detects unauthorized privilege escalations and processes running with root privileges
- **Network Monitoring**: Monitors network connections made by root processes to detect suspicious external communications
- **Process Monitoring**: Identifies hidden processes that may indicate rootkit presence
- **File Integrity Checking**: Monitors critical system files for unauthorized modifications
- **Kernel Integrity Checks**: Performs kernel-level security checks using shell scripts
- **Security Dashboard**: Web-based dashboard for monitoring security events (Flask-based)
- **Automated Logging**: Comprehensive logging of all security events and alerts

## Project Structure

```
RootGuard/
├── main.py                 # Main entry point
├── dashboard/
│   └── app.py             # Flask web dashboard
├── monitor/
│   ├── network_monitor.py      # Network connection monitoring
│   ├── privilege_monitor.py    # Privilege escalation detection
│   └── process_monitor.py      # Hidden process detection
├── integrity/
│   ├── file_integrity.py       # File integrity checking
│   └── kernel_check.sh         # Kernel-level security checks
├── response/
│   ├── alert.py                # Alert handling
│   └── auto_block.py           # Automated blocking mechanisms
└── logs/
    ├── attacks.log              # Attack logs
    └── audit.log               # Audit trail
```

## Requirements

- Python 3.6+
- psutil
- Flask

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Bipul-programmer/RootGuard.git
cd RootGuard
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Ensure you have the necessary permissions (some features may require root/sudo access):
```bash
sudo python3 main.py
```

## Usage

### Running RootGuard

Start the main monitoring system:
```bash
python3 main.py
```

Or with elevated privileges for full functionality:
```bash
sudo python3 main.py
```

### Accessing the Dashboard

The web dashboard runs on port 5000 by default:
```bash
# Dashboard will be available at:
http://localhost:5000
```

## Monitoring Modules

### Network Monitor
Monitors network connections made by root processes. Alerts when root processes connect to untrusted external IPs.

### Privilege Monitor
Continuously scans for processes that have escalated to root privileges without proper authorization.

### Process Monitor
Detects hidden processes that may indicate rootkit or malware presence.

### File Integrity Monitor
Monitors critical system files for unauthorized modifications and maintains integrity checksums.

## Logging

All security events are logged to:
- `logs/attacks.log` - Security alerts and detected attacks
- `logs/audit.log` - System audit trail

## Security Considerations

⚠️ **Important**: This tool requires elevated privileges to function effectively. Use responsibly and only on systems you own or have explicit permission to monitor.

- Some monitoring features require root/sudo access
- Network monitoring may trigger false positives for legitimate root processes
- Always review logs before taking automated actions

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

See LICENSE file for details.

## Author

**Bipul Kumar**
- GitHub: [@Bipul-programmer](https://github.com/Bipul-programmer)

## Disclaimer

This tool is for educational and authorized security testing purposes only. Users are responsible for ensuring they have proper authorization before monitoring any system.
