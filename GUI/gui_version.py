import tkinter as tk
from tkinter import filedialog
import subprocess

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PCAP Files", "*.pcap *.cap *.pcapng")])
    if file_path:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, file_path)
        grab_button.config(state=tk.NORMAL)

def execute_script():
    input_file = file_entry.get()
    hc22000_file = "wpa_crack.hc22000"
    subprocess.run(["hcxpcapngtool", "-o", hc22000_file, input_file])
    result = subprocess.run(["hashcat", "-m", "22000", hc22000_file, "wordlist.txt", "--show"], capture_output=True)
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, result.stdout.decode("utf-8"))
    output_text.config(state=tk.DISABLED)

root = tk.Tk()
root.title("WPA/WPA2 Crack Tool GUI")
root.geometry("500x600")
root.configure(bg="black")

title_label = tk.Label(root, text="Select .pcap file:", bg="black", fg="white", font=("Arial", 32))
title_label.place(relx=0.5, rely=0.15, anchor=tk.CENTER)

select_button = tk.Button(root, text="Select input file", command=select_file)
select_button.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

file_entry = tk.Entry(root, width=40)
file_entry.place(relx=0.5, rely=0.35, anchor=tk.CENTER)

grab_button = tk.Button(root, text="GRAB", state=tk.DISABLED, command=execute_script, width=15, height=2, font=("Arial", 25, "bold"))
grab_button.place(relx=0.5, rely=0.55, anchor=tk.CENTER)

output_text = tk.Text(root, width=50, height=8, state=tk.DISABLED)
output_text.place(relx=0.5, rely=0.775, anchor=tk.CENTER)

output_margin = tk.Frame(root, bg="black", width=500, height=25)
output_margin.place(relx=0.5, rely=0.8875, anchor=tk.CENTER)

root.mainloop()
