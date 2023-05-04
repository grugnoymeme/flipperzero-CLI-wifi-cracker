# (flipperzero)-wifi-password-grabber

To extract passwords you need from un-analyzed .pcap files, you need to follow these steps:

### Dependecies
hcxpcaptool    
tshark     

[tshark is used running the `tahark_alternative.pt` if `hcxpcaptools` is resulting some kind of `ERROR`, cause `hcxpcaptool` may not working properly, cause has a little problem of mismatch between the release and the OS where it is installed]

```
pip install -r requirements.txt
git clone https://github.com/grugnoymeme/flipperzero-wifi-password-grabber
mv path/to/pcapfile.pcap flipperzero-wifi-password-grabber
sudo nano wordlist.txt (and fill the file with all the possible passwords you want to try to find out the right ones)
CTRL+o
ENTER
CTRL+x
y
ENTER

OR
mv path/to/yourwordlist.txt flipperzero-wifi-password-grabber

sudo python3 wifi_pass_cracker.py

OR
sudo python3 tshark_alternative.py
```
now you will be asked your root password to give the root priveleges to the script, type it (even if you don't see nothing appear), then follow the instructions of the script (remember to put the .pcap file and the wordlist.txt file in the same directory of this script)

passwords will stored in a new file in the directory "risultati.txt"

### Disclaimer

Please note that this payload is for educational purposes only and should not be used for illegal activities.
