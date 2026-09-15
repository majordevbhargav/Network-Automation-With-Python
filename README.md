# Network Automation with Python

A practical learning repository for automating network operations with Python, with a strong focus on Cisco infrastructure, device interaction, data collection, and repeatable automation workflows.

## Focus Areas

- Python for network engineers
- Cisco IOS / IOS-XE automation
- SSH-based device interaction
- Netmiko and network APIs
- Operational and configuration commands
- Structured network data
- Automation and error handling
- Cisco DevNet-oriented workflows

## Learning Path

```text
Python Fundamentals
        ↓
Networking Fundamentals
        ↓
Netmiko / Device APIs
        ↓
Structured Output
        ↓
Configuration Automation
        ↓
Ansible
        ↓
REST / Cisco APIs
        ↓
Testing + Parallel Operations
        ↓
Telemetry + Network Platforms
```

## Getting Started

Clone the repository and install the dependencies used by the individual exercises.

```bash
git clone https://github.com/majordevbhargav/Network-Automation-With-Python.git
cd Network-Automation-With-Python
pip install -r requirements.txt
```

Some exercises may require access to a lab or authorized network device. Never hardcode production credentials.

## Development Principles

The goal is to move from one-off scripts toward automation that is repeatable, observable, safe, and easy to maintain.

## Future Direction

- Network telemetry and streaming data
- Parallel device operations
- Automated configuration validation
- Cisco API integrations
- Network anomaly detection
- Security analytics
- Infrastructure management platforms

## Security

Use lab or explicitly authorized infrastructure. Store credentials through environment variables, secure credential stores, or Ansible Vault rather than source files.

## Author

**Dev Bhargav**

- GitHub: https://github.com/majordevbhargav
- LinkedIn: https://www.linkedin.com/in/devbhargav100
