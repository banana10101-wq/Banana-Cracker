import time
import os

print("Target IP:")
target_ip = input("> ")

print("Do you want to use passlist.txt? (y/n)")
use_list = input("> ").lower()

if use_list == "y":
    wordlist_path = "passlist.txt"
else:
    print("Type your password list path (relative to Banana-cracker/):")
    wordlist_path = input("> ")

# Dosya var mı kontrol et
if not os.path.isfile(wordlist_path):
    print("❌ File not found:", wordlist_path)
    exit()

# Şifreleri oku
with open(wordlist_path, "r", encoding="latin-1") as file:
    passwords = file.readlines()

print(f"\n🚀 Starting brute-force on {target_ip} using {len(passwords)} passwords...\n")

for password in passwords:
    password = password.strip()
    print(f"🔍 Trying password: {password}")
    time.sleep(0.05)

print("\n✅ Done.")
