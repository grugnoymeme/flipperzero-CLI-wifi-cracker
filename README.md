# FlipperZero CLI WiFi Cracker

To extract passwords from .pcap files extracted with your Flipper Zero (or other tools), this is an "all-in-one" tool. 
You'll just need to follow these steps:       

This is the CLI (Command Line Interface) version of my other script and repo [`flipperzero-GUI-wifi-cracker`](https://github.com/grugnoymeme/flipperzero-GUI-wifi-cracker), i just wanted to make the process easyest as possible, and this is the result.


* [Needed Tools](#Needed-Tools)
* [Usage](#Usage)
  - [For dictionary attack](#for-dictionary-attack)
  - [For bruteforce attack](#for-bruteforce-attack)
* [PCAP Extraction](#PCAP-Extraction)
* [Disclaimer](#Disclaimer)



## Needed-Tools        
(for both versions)         
python3   
hcxpcapngtool [included in hcxtools]                  
hashcat   

---
## Usage

### for-dictionary-attack:
```
git clone https://github.com/grugnoymeme/flipperzero-CLI-wifi-cracker.git
cd flipperzero-CLI-wifi-cracker
cd dictionary_attack
mv path/to/pcapfile.pcap path/to/flipperzero-CLI-wifi-cracker/dictionary_attack (optional) (if you not move it, specify the entire path when you'll be asked)    
mv path/to/yourwordlist.txt path/to/flipperzero-CLI-wifi-cracker/dictionary_attack (optional) (if you not move it, specify the entire path when you'll be asked)    
python3 dictionary_attack.py
```
### for-bruteforce-attack:    
* There are two different brute force script. One that run till the password is found, and the other in which you can set a timer that stop running the script if the password is not found in the time that you had set.
```
git clone https://github.com/grugnoymeme/flipperzero-CLI-wifi-cracker.git
cd flipperzero-CLI-wifi-cracker
cd bruteforce_attack   
// set the timer and the charset
python3 bruteforce_attack.py
```
* If you don't have a wordlist (password-list or a dictionary) to run the dictionary attack mode, you can easyly create one, executing these commands:
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
## PCAP-Extraction        
(with Flipper Zero & ESP32 Marauder)          
* You can simply upload the `EAPOLwifiSniffer.json` script into `/ext/apps_data/marauder/scripts` directory in your Flipper Zero and then you can directly run it through the [ESP32] Marauder application, under the Menu's voice "Scripts".

In alternative, if you want to do it yourself, because you need to modify the duration of the sniff, or the name of the script, or maybe adding some more stages or simply because you want to do it ALL by yourself: 
* You can automatize the extraction of .pcap files from flipper zero, using the [@0xchocolate](https://github.com/0xchocolate) 's companion app, of the [@JustCallMeKoKo's](https://github.com/justcallmekoko) ESP32marauder. Once you've connected the devboard,follow these instructions:

<ins>**ATTENTION:**</ins> *do not modify the duration of the deauth, because if you set it for more then one second, the risk is that you will not catch EAPOL packets and then, you woun't be able to extract WPA/WPA2 handshakes to analyze, and extract the password.*   
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

* In order to correctly save the "pcaps" files on the SD card of your Flipper Zero, you must have flashed the correct version of the "Marauder" firmware (esp32_marauder_vX_X_X_xxxxxxxx_flipper_sd_serial.bin), on your "Devboard" (whether official or handmade); and that you have set the saving of the pcaps on the Flipper Zero external memory (you can set this when you first start the [ESP32] Marauder app, or later, from the app's menu). 
  
---
## Disclaimer
This tool is not developed by the Flipper Zero staff.    
Please note that the code you find on this repo is only proposed for educational purposes and should NEVER be used for illegal activities.
