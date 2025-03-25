import scapy.all as scapy
import pandas as pd
import datetime
import os
import csv

# ✅ Set Default Save Location (Desktop)
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# ✅ Generate a Timestamped Filename
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
default_filename = f"captured_packets_{timestamp}.csv"
save_path = os.path.join(desktop_path, default_filename)

# ✅ Define CSV Headers
csv_headers = ["Timestamp", "Source IP", "Destination IP", "Protocol", "Source Port", "Destination Port", "Packet Size", "Suspicious"]

# ✅ Create and Initialize CSV File with Headers
with open(save_path, mode="w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)
    writer.writerow(csv_headers)  # Write column headers

def analyze_packet(packet):
    """Captures packets and writes them directly to a CSV file in real-time."""
    try:
        if packet.haslayer(scapy.IP):
            src_ip = packet[scapy.IP].src
            dst_ip = packet[scapy.IP].dst
            packet_size = len(packet)
            protocol = "OTHER"

            if packet.haslayer(scapy.TCP):
                protocol = "TCP"
                src_port = packet[scapy.TCP].sport
                dst_port = packet[scapy.TCP].dport
            elif packet.haslayer(scapy.UDP):
                protocol = "UDP"
                src_port = packet[scapy.UDP].sport
                dst_port = packet[scapy.UDP].dport
            elif packet.haslayer(scapy.ICMP):
                protocol = "ICMP"
                src_port = dst_port = None
            else:
                src_port = dst_port = None

            # ✅ Detect Suspicious Activity
            suspicious = "Normal"
            if protocol == "TCP" and dst_port in [80, 443]:
                suspicious = "Possible HTTP/HTTPS traffic"
            elif protocol == "ICMP":
                suspicious = "Possible Ping Sweep detected"
            elif packet_size > 1000:
                suspicious = "Large packet size detected"

            # ✅ Store packet details
            packet_info = [
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                src_ip, dst_ip, protocol, src_port, dst_port, packet_size, suspicious
            ]

            # ✅ Append packet data to CSV in real-time
            with open(save_path, mode="a", newline="", encoding="utf-8-sig") as file:
                writer = csv.writer(file)
                writer.writerow(packet_info)

            # ✅ Print packet details in terminal
            print(f"[{packet_info[0]}] {src_ip}:{src_port} -> {dst_ip}:{dst_port} | Protocol: {protocol} | Size: {packet_size} bytes | {suspicious}")

    except Exception as e:
        print(f"❌ Error analyzing packet: {e}")

# ✅ Start Packet Sniffing
print(f"🔍 Starting Network Sniffer... Capturing packets. Data is being saved in: {r"C:\Users\Munnii\Desktop"}")
print("Press Ctrl+C to stop capturing packets.")

try:
    scapy.sniff(prn=analyze_packet, store=False)  # Sniff packets and analyze in real-time
except KeyboardInterrupt:
    print("\n⏹️  Stopping Sniffer... Packets saved successfully.")
    print(f"✅ Captured packets saved at: {r"C:\Users\Munnii\Desktop"}")
