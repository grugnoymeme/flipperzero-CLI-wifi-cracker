import subprocess

# Select input .pcap file
input_file = input("Insert input .pcap file's name: ")

# Convert the .pcap file in .hc22000
hc22000_file = "wpa_crack.hc22000"
subprocess.run(["hcxpcapngtool", "-o", hc22000_file, input_file])

# Import the .hc22000 file into hashcat, find out the password and show it
subprocess.run(["hashcat", "-m", "22000", hc22000_file, "wordlist.txt", "--show"])
