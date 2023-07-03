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
print("          WiFi-Grabber Tool • © 2023 • 47lecoste • https://github.com/grugnoymeme")
print("")
print("")
print("  _____________________________________________________________________________________________\n")
print("* If files you select aren't in the same directory of the script, please write their entire path.")
print("")
print("** Type ^C (CTRL + c) to stop the script, if you want to exit before the end of the operation.")
print("  _____________________________________________________________________________________________\n")
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

print("  _____________________________________________________________________________________________\n")
print("  ---------------------------------------------------------------------------------------------\n")

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
