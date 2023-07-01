import pyshark
import subprocess

# Seleziona il file .pcap di input
input_file = input("Inserisci il nome del file .pcap di input: ")

# Crea un nuovo file .pcap contenente solo i pacchetti EAPOL
output_file = "eapol.pcap"
capture = pyshark.FileCapture(input_file, display_filter="eapol", output_file=output_file)

# Converte il file .pcap in .hccapx
hccapx_file = "eapol.hccapx"
subprocess.run(["tshark", "-r", hccapx_file, "-Y", "eapol", "-w", output_file])

# Importa il file .hccapx in hashcat e salva i risultati su un file "risultati.txt"
results_file = "risultati.txt"
subprocess.run(["hashcat", "-m", "2500", hccapx_file, "wordlist.txt", "-o", results_file])

# Stampa un messaggio di conferma
print("I risultati sono stati scritti su " + results_file)
