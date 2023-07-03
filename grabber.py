import os
import subprocess

# ASCII Art
ascii_art = """
██╗    ██╗██╗███████╗██╗     ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
██║    ██║██║██╔════╝██║    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║ █╗ ██║██║█████╗  ██║    ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
██║███╗██║██║██╔══╝  ██║    ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
╚███╔███╔╝██║██║     ██║    ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
 ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝
"""

print(ascii_art)
print("© 2023 • 47lecoste • https://github.com/grugnoymeme")
print("")
print("* if files you select are not in the same directory of the script, specify the entire path, or the script will not work properly.")
print("")
print("")

# Select input .pcap file
input_file = ""
while True:
    input_file = input("Insert input .pcap file's NAME or PATH: ")
    if input_file.endswith((".pcap", ".cap", ".pcapng")) and os.path.isfile(input_file):
        break
    else:
        print("Invalid input file. Please make sure the file exists and has a valid format.")

# Convert the .pcap file into .hc22000
hc22000_file = "wpa_crack.hc22000"
subprocess.run(["hcxpcapngtool", "-o", hc22000_file, input_file])

# Prompt for wordlist file
wordlist_file = ""
while True:
    wordlist_file = input("Now insert wordlist file's NAME or PATH: ")
    if wordlist_file.endswith(".txt") and os.path.isfile(wordlist_file):
        break
    else:
        print("Invalid wordlist file. Please make sure the file exists and has a valid format.")

# Import the .hc22000 file into hashcat, find out the password, and show it
subprocess.run(["hashcat", "-m", "22000", hc22000_file, wordlist_file, "--show"])

# Delete the hc22000 file
os.remove(hc22000_file)
