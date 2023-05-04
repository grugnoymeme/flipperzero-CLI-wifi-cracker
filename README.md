# (flipperzero)-wifi-password-grabber

To extract passwords you need from un-analyzed .pcap files, you need to follow these steps:

### Dependecies
hcxpcaptool    
tahark     

[tshark is used running the `alternative_script.pt` if `hcxpcaptools` is resulting some kind of `ERROR`, cause `hcxpcaptool` may not working properly, cause has a little problem of mismatch between the release and the OS where it is installed]

```
pip install -r requirements.txt
git clone https://github.com/grugnoymeme/wifi-password-grabber
mv path/to/pcapfile.pcap wifi-password-grabber
sudo nano wordlist.txt (and fill the file with all the possible passwords you want to try to find out the right ones)
OR
mv path/to/yourwordlist.txt wifi-password-grabber
python3 wifi_pass_cracker.py
```
then follow the instructions of the script (remember to put the .pcap file and the wordlist.txt file in the same directory of this script)

passwords will stored in a new file in the directory "risultati.txt"

### Disclaimer

Please note that this payload is for educational purposes only and should not be used for illegal activities.
