# (flipperzero)-CLI-wifi-cracker

To extract passwords from .pcap files extracted with your Flipper Zero (or other tools), this is an "all-in-one" tool. 
You'll just need to follow these steps:       
`* at the end of the page you can find a tip to catch pcap file with your Flipper Zero`

This is the CLI (Command Line Interface) version of my other script and repo [`flipperzero-GUI-wifi-grabber`](https://github.com/grugnoymeme/flipperzero-GUI-wifi-grabber), i just wanted to make the process easyest as possible, and this is the result.

---
### Dependecies     
subprocess.run   
os

### Used Tools
python3   
hcxpcapngtool [included in hcxtools]                  
hashcat   

---
### Usage 
```
pip install -r requirements.txt
git clone https://github.com/grugnoymeme/flipperzero-wifi-password-grabber.git
mv path/to/pcapfile.pcap flipperzero-wifi-password-grabber (optional) (if not, specify the entire path)     
mv path/to/yourwordlist.txt flipperzero-wifi-password-grabber (optional) (if not, specify the entire path)     
sudo python3 grabber.py
```
If you don't have a wordlist, a pass-list or a dictionary, you can easyly create one doing this:
```
nano wordlist.txt (and fill the file with all the possible passwords you want to try to find out the right ones)
^o (CTRL+o)
ENTER
^x (CTRL+x)
y (yes)
ENTER
```

---
### Extarcion of .pcap file.  
You can automatize the extraction of .pcap files from flipper zero, using the [@0xchocolate](https://github.com/0xchocolate) 's companion app, of the [@JustCallMeKoKo's](https://github.com/justcallmekoko) ESP32marauder. Once you've connected the devboard and opened the app,follow these instructions:
```
Menu       
Apps       
WIFI / GPIO / GPIO EXTRA        
[ESP32] WiFi Marauder       
Scripts   
[+]ADD SCRIPT    
< Enter a name for your script >   
Save    
< Select your script >    
[+]EDIT STAGES    
[+]ADD STAGE    
[+]Deauth     
< Select Deauth >     
Timeout 1    
Save    
Back    
[+]ADD STAGE    
[+]Sniff RAW     
< Select Sniff RAW >    
Timeout 15 (or 10, maybe also 5 is ok)     
Save    
Back     
Back     
[*]SAVE
```
  
---
# Disclaimer
This tool is not developed by the Flipper Zero staff.    
Please note that the code you find on this repo is only proposed for educational purposes and should NEVER be used for illegal activities.
