# (flipperzero)-wifi-password-grabber

To extract passwords from .pcap files extracted with your flipper zero (or others) without using wireshark and others analyzers. You'll need to follow these steps:

### Dependecies     
subprocess.run   
`pip install subprocess.run`

### Necessary Tools
python3   
hcxtools / hcxpcapngtool    
tshark *        
hashcat *  
` * Not really needed, cause ran throught subprocess.run `

### Usage 
```
pip install -r requirements.txt
git clone https://github.com/grugnoymeme/flipperzero-wifi-password-grabber.git
mv path/to/pcapfile.pcap flipperzero-wifi-password-grabber
mv path/to/yourwordlist.txt flipperzero-wifi-password-grabber
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
### Tips
*Remember to rename "wordlist.txt" the word list or the dictionary you are using to crack the password.  
passwords will stored in a new file in the directory "risultati.txt"

### Extarcion of .pcap file.  
You can automatize the extraction of .pcap files from flipper zero, using the @0xchocolate 's companion app, of the @justcallmekoko 's ESP32marauder.
Once you've connected the devboard and opened the app,follow these instructions:    
```
Menu    
Apps    
GPIO    
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

### Disclaimer

Please note that this payload is for educational purposes only and should not be used for illegal activities.
