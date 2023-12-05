import os
import subprocess
import string
import itertools

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

hc22000_file = "wpa_crack.hc22000"
subprocess.run(["hcxpcapngtool", "-o", hc22000_file, input_file])

print("  _____________________________________________________________________________________________\n")
print("  ---------------------------------------------------------------------------------------------\n")

# Brute force attack
charset = string.printable  # Define the character set to be used (e.g. "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPRSTUVWXYZ"), string.printable contains all kind of printable characters

password_found = False
password_length = 1

while not password_found:
    for password in itertools.product(charset, repeat=password_length):
        password = ''.join(password)
        result = subprocess.run(["hashcat", "-m", "22000", hc22000_file, password], capture_output=True)
        if "Cracked" in result.stdout.decode():
            print(f"Password found: {password}")
            password_found = True
            break
    password_length += 1

# Delete the hc22000 file
os.remove(hc22000_file)
