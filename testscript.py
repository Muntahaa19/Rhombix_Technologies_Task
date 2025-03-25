import os

# Get Desktop path
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Ask for filename
filename = input("📁 Enter a name for the log file (without extension): ").strip()

if not filename:
    print("❌ No filename entered. Exiting...")
    exit()

log_file_path = os.path.join(desktop_path, f"{filename}.csv")

# Print path to confirm
print(f"📄 Trying to save file at: {log_file_path}")

# Try writing a test file
try:
    with open(log_file_path, "w", encoding="utf-8") as f:
        f.write("Test log file. If you see this, saving works!\n")
    print(f"✅ Test file successfully saved at: {log_file_path}")
except Exception as e:
    print(f"❌ Error saving test file: {e}")
