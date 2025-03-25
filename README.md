**Network Packet Sniffer**

:pushpin:**Overview**

A network packet sniffer is a cybersecurity tool designed to monitor, capture, and analyze network traffic. This project implements a Python-based packet sniffer that records network activity and logs captured data for security analysis.

:pushpin:**Features**

* Real-time packet capturing

* Automatic logging in CSV format

* Packet analysis (IP, TCP, UDP, ICMP)

* Detection of suspicious network activity

* Automated storage of logs without manual input


:pushpin:**Prerequisites**

Python 3.x

:pushpin:**Required libraries:**

scapy

pandas

datetime

:pushpin:**Install dependencies using:**

pip install scapy pandas

:pushpin:**Installation**

**Clone the repository:**

git clone https://github.com/your-repo/network-sniffer.git

**Navigate to the project folder:**

cd network-sniffer

**Run the script:**

python sniffer.py

:pushpin:**Usage**

The script will automatically start capturing network traffic.

Captured packets are analyzed and logged.

The log file is saved automatically in the default location.

Press Ctrl + C to stop the sniffer.

:pushpin:**Future Enhancements**

Implement AI-based anomaly detection

Develop a GUI for better usability

Add automated alert notifications for suspicious traffic

**License**

This project is licensed under the MIT License.