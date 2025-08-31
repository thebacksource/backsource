#!/usr/bin/env python3
import os, sys, time, random

# ---------- Helper Functions ----------
def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def slow_print(text, delay=0.03):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    clear_screen()
    print(r"""
██████╗  █████╗ ███████╗███████╗███████╗███████╗███████╗███████╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
██████╔╝███████║███████╗███████╗█████╗  █████╗  █████╗  █████╗  
██╔═══╝ ██╔══██║╚════██║╚════██║██╔══╝  ██╔══╝  ██╔══╝  ██╔══╝  
██║     ██║  ██║███████║███████║███████╗███████╗███████╗███████╗
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝
          ██████ SIMULATOR ██████
""")

# ---------- Fake Account Data ----------
fake_account = {
    "username": "",
    "robux": 0,
    "password": "",
    "last_game": "",
    "robux_spent": 0,
    "last_gamepass": "",
    "recent_activity": []
}

# ---------- Startup: Enter Fake Data ----------
def enter_fake_data():
    banner()
    fake_account["username"] = input("Enter fake username: ")
    fake_account["robux"] = int(input("Enter fake Robux balance: "))
    fake_account["last_game"] = input("Enter last game played: ")
    fake_account["robux_spent"] = int(input("Enter Robux spent in last game: "))
    fake_account["last_gamepass"] = input("Enter last gamepass purchased: ")
    pw = input("Enter the password (will be 'guessed'): ")
    fake_account["password"] = pw
    fake_account["recent_activity"] = [
        (f"Bought '{fake_account['last_gamepass']}'", -fake_account["robux_spent"]),
        (f"Played '{fake_account['last_game']}'", 0),
        ("Daily Login Reward", +50)
    ]
    slow_print("\nFake account data saved! Preparing password guess simulation...\n", 0.05)
    time.sleep(1)

# ---------- Password Guess Simulation ----------
def password_guessing():
    clear_screen()
    slow_print(f"[+] Starting password guessing for {fake_account['username']}...\n")
    fake_passwords = [f"pass{i}{random.randint(100,999)}" for i in range(1, 100)]
    fake_passwords.append(fake_account["password"])  # Last one is correct
    for i, pwd in enumerate(fake_passwords, 1):
        sys.stdout.write(f"\r[*] Trying password {i}/{len(fake_passwords)}: {pwd}  ")
        sys.stdout.flush()
        time.sleep(0.05)
    print(f"\n\n[+] Password found: {fake_account['password']}\n")
    time.sleep(1)

# ---------- Fake Authenticator / Email Guess ----------
def auth_guess():
    clear_screen()
    slow_print("[*] Attempting authenticator & email verification...\n")
    for i in range(30):
        bar = "#" * (i+1) + "-" * (30-i-1)
        sys.stdout.write(f"\r[{bar}] {i*3}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n[+] Authenticator & email verified successfully!\n")
    time.sleep(1)

# ---------- Fake Dashboard ----------
def show_dashboard():
    while True:
        clear_screen()
        banner()
        print(f"Username: {fake_account['username']}")
        print(f"Robux Balance: {fake_account['robux']} 🪙")
        print(f"Password: {fake_account['password']}")
        print(f"Last Game Played: {fake_account['last_game']}")
        print(f"Robux Spent Last Game: {fake_account['robux_spent']}")
        print(f"Last Gamepass: {fake_account['last_gamepass']}")
        print("\nRecent Activity:")
        for action, amt in fake_account["recent_activity"]:
            sign = "+" if amt > 0 else "-" if amt < 0 else ""
            print(f"  {action:30} {sign}{abs(amt)} Robux" if amt != 0 else f"  {action}")
        print("\nOptions:")
        print("1) Change Password")
        print("2) Add Fake Transaction / Gamepass")
        print("3) Exit Dashboard")
        choice = input("\nSelect option: ")
        if choice == "1":
            new_pw = input("Enter new password: ")
            fake_account["password"] = new_pw
            slow_print("[+] Password changed successfully!\n", 0.05)
            time.sleep(1)
        elif choice == "2":
            desc = input("Transaction / Gamepass description: ")
            amt = int(input("Amount (+ for gain, - for spend): "))
            fake_account["recent_activity"].insert(0, (desc, amt))
            fake_account["robux"] += amt
            slow_print("[+] Transaction added!\n", 0.05)
            time.sleep(1)
        elif choice == "3":
            slow_print("[*] Logging out of dashboard...\n", 0.05)
            time.sleep(1)
            break
        else:
            slow_print("[-] Invalid choice!\n", 0.05)
            time.sleep(1)

# ---------- Main Flow ----------
def main():
    clear_screen()
    banner()
    slow_print("Welcome to PasswordGuesser Simulator!\n", 0.05)
    time.sleep(1)
    enter_fake_data()
    password_guessing()
    auth_guess()
    show_dashboard()
    slow_print("Thank you for using PasswordGuesser Simulator!\n", 0.05)

if __name__ == "__main__":
    main()
