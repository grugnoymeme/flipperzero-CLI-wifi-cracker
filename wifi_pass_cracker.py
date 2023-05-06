import pyshark
import subprocess

# Select the path (or better, the name in you are in the same directory of this script) of the .pcap file.
input_file = input("Select the .pcap file you want to use as input: ")

# Create a nu .pcap that only contains EAPOL packets.
output_file = "eapol.pcap"
capture = pyshark.FileCapture(input_file, display_filter="eapol", output_file=output_file)

# Convert the new .pcap in .hccapx
hccapx_file = "eapol.hccapx"
subprocess.run(["hcxpcaptool", "-o", hccapx_file, output_file])

# Importa the .hccapx file into hashcat and store the results in a file "risultati.txt" in the same directory of this script.
results_file = "risultati.txt"
subprocess.run(["hashcat", "-m", "2500", hccapx_file, "wordlist.txt", "-o", results_file])

print("You will find your results in " + results_file)