import pyshark
import subprocess.run

# Select the input .pcap file
input_file = input("Inserisci il nome del file .pcap di input: ")

# Create a new file .pcap conteining only EAPOL handshakes
output_file = "eapol.pcap"
capture = pyshark.FileCapture(input_file, display_filter="eapol", output_file=output_file)

# Convert the .pcap file in .hccapx
hccapx_file = "eapol.hccapx"
subprocess.run(["tshark", "-r", hccapx_file, "-Y", "eapol", "-w", output_file])

# Import the .hccapx file into hashcat and save the results on a new file "risultati.txt"
results_file = "risultati.txt"
subprocess.run(["hashcat", "-m", "22000", hccapx_file, "wordlist.txt", "-o", results_file])

# Print a "Success" message
print("I risultati sono stati scritti su " + results_file)
