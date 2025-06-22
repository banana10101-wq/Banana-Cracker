import os
import sys
import subprocess

# ANSI renk kodları
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

def clear():
    os.system("clear")

def main():
    clear()
    print(f"""{YELLOW}
  ___                           
 | _ ) __ _ _ _  __ _ _ _  __ _ 
 | _ \/ _` | ' \/ _` | ' \/ _` |
 |___/\__,_|_||_\__,_|_||_\__,_|
{RESET}""")

    print("Hi user, I made this SSH and FTP password cracker, what do you want to select?")
    print(f"{RED}(1) FTP brute")
    print(f"(2) SSH brute")
    print(f"(00) Exit{RESET}")

    choice = input("Select: ").strip()

    current_dir = os.path.dirname(os.path.abspath(__file__))

    if choice == "1":
        ftp_script = os.path.join(current_dir, "Banana-cracker-ftp.py")
        if os.path.isfile(ftp_script):
            subprocess.run(["python", ftp_script])
        else:
            print("❌ Banana-cracker-ftp.py not found in the current directory.")
    elif choice == "2":
        ssh_script = os.path.join(current_dir, "Banana-cracker-ssh.py")
        if os.path.isfile(ssh_script):
            subprocess.run(["python", ssh_script])
        else:
            print("❌ Banana-cracker-ssh.py not found in the current directory.")
    elif choice == "00":
        print("Exiting... Goodbye!")
        sys.exit(0)
    else:
        print("Invalid choice. Try again.")

if __name__ == "__main__":
    while True:
        main()
        input("\nPress Enter to continue...")
