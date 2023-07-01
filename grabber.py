import pyshark
import subprocess

# Select the input .pcap file
input_file = input("Insert input .pcap file's name: ")

# Create a new file .pcap conteining only EAPOL handshakes
output_file = "eapol.pcap"
capture = pyshark.FileCapture(input_file, display_filter="eapol", output_file=output_file)

# Convert the .pcap file in .hc22000
hc22000_file = "eapol.hc22000"
subprocess.run(["tshark", "-r", output_file, "-Y", "eapol", "-w", hc22000_file])

# Import the .hc22000 file into hashcat and save the results on a new file "risultati.txt"
results_file = "risultati.txt"
subprocess.run(["hashcat", "-m", "22000", hc22000_file, "wordlist.txt", "-o", results_file])

# Print a "Success" message
print("You'll find results in " + results_file)
