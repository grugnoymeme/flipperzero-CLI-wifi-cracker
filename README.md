# (flipperzero)-CLI-wifi-cracker

To extract passwords from .pcap files extracted with your Flipper Zero (or other tools), this is an "all-in-one" tool. 
You'll just need to follow these steps:       
`* at the end of the page you can find a tip to catch pcap file with your Flipper Zero`

This is the CLI (Command Line Interface) version of my other script and repo [`flipperzero-GUI-wifi-cracker`](https://github.com/grugnoymeme/flipperzero-GUI-wifi-cracker), i just wanted to make the process easyest as possible, and this is the result.

---
## Dependecies     

### for dictionary attack:
os      
subprocess.run        
### for bruteforce attack:
os    
subprocess.run      
string     
itertools      
signal

## Used Tools (for both):
python3   
hcxpcapngtool [included in hcxtools]                  
hashcat   

---
## Usage

### for dictionary attack:
```
git clone https://github.com/grugnoymeme/flipperzero-CLI-wifi-cracker.git
cd flipperzero-CLI-wifi-cracker
cd dictionary_attack
pip install -r requirements.txt
mv path/to/pcapfile.pcap path/to/flipperzero-CLI-wifi-cracker/dictionary_attack (optional) (if you not move it, specify the entire path when you'll be asked)    
mv path/to/yourwordlist.txt path/to/flipperzero-CLI-wifi-cracker/dictionary_attack (optional) (if you not move it, specify the entire path when you'll be asked)    
python3 dictionary_attack.py
```

### for bruteforce attack:
```
git clone https://github.com/grugnoymeme/flipperzero-CLI-wifi-cracker.git
cd flipperzero-CLI-wifi-cracker
cd bruteforce_attack 
python3 bruteforce_attack.py
```

If you don't have a wordlist (password-list or a dictionary) to run the dictionary attack mode, you can easyly create one, executing these commands:
```
cd path/to/flipperzero-CLI-wifi-cracker
cd dictionary_attack (optional) (if you not create it, specify the entire path when you'll be asked)
nano wordlist.txt (and fill the file with all the possible passwords you want to try to find out the right ones)
^o (CTRL+o)
ENTER
^x (CTRL+x)
y (yes)
ENTER
```

---
## Extarcion of .pcap file with Flipper Zero & ESP32 Marauder  
You can automatize the extraction of .pcap files from flipper zero, using the [@0xchocolate](https://github.com/0xchocolate) 's companion app, of the [@JustCallMeKoKo's](https://github.com/justcallmekoko) ESP32marauder. Once you've connected the devboard and opened the app,follow these instructions:
```
Switch on the Flipper Zero
Press OK to enter the Menu       
Apps       
WIFI (for Xtreme) / GPIO (for Roguemaster) / GPIO EXTRA (for Unleashed)        
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
* Once create, to run the script, open [ESP32] Marauder App, Scan all the APs, select the target one, go down in the menu to "Scripts", click on your new script and press "Run". The script is gonna make all the work.     
Then go to the "apps_data" folder, from the root of your Flipper Zero's FS, "marauder", and finally "pcaps".
There you'll find the file you will need to run properly this tool.

** In order to correctly save the "pcaps" files on the SD card of your Flipper Zero, you must have flashed the correct version of the "Marauder" firmware (esp32_marauder_vX_X_X_xxxxxxxx_flipper_sd_serial.bin), on your "Devboard" (whether official or handmade); and that you have set the saving of the pcaps on the Flipper Zero external memory (you can set this when you first start the [ESP32] Marauder app, or later, from the app's menu). 
  
---
## Disclaimer
This tool is not developed by the Flipper Zero staff.    
Please note that the code you find on this repo is only proposed for educational purposes and should NEVER be used for illegal activities.
