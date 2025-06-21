import time
import os

print("Target IP:")
target_ip = input("> ")

print("Do you want a ready-made password list (rockyou.txt)? (y/n)")
use_rockyou = input("> ").lower()

if use_rockyou == "y":
    wordlist_path = "passlist/rockyou.txt"
else:
    print("Type your password list path (relative to Banana-cracker/):")
    wordlist_path = input("> ")

# Dosya var mı kontrolü
if not os.path.isfile(wordlist_path):
    print("❌ File not found:", wordlist_path)
    exit()

# Dosyayı oku
with open(wordlist_path, "r", encoding="latin-1") as file:
    passwords = file.readlines()

print(f"\n🚀 Starting brute-force on {target_ip} using {len(passwords)} passwords...\n")

# Şifreleri sırayla dene (simülasyon)
for password in passwords:
    password = password.strip()
    print(f"🔍 Trying password: {password}")
    time.sleep(0.05)

print("\n✅ Done. (Simülasyon tamamlandı)")
