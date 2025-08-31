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
          ██████ PASSWORD GUESSER ██████
""")

# ---------- Account Data ----------
account_data = {
    "username": "",
    "robux": 0,
    "password": "",
    "last_game": "",
    "robux_spent": 0,
    "last_gamepass": "",
    "recent_activity": []
}

# ---------- Startup: Enter Account Info ----------
def enter_account_info():
    banner()
    account_data["username"] = input("Enter username: ")
    account_data["robux"] = int(input("Enter Robux balance: "))
    account_data["last_game"] = input("Enter last game played: ")
    account_data["robux_spent"] = int(input("Enter Robux spent in last game: "))
    account_data["last_gamepass"] = input("Enter last gamepass purchased: ")
    pw = input("Enter password: ")
    account_data["password"] = pw
    account_data["recent_activity"] = [
        (f"Bought '{account_data['last_gamepass']}'", -account_data["robux_spent"]),
        (f"Played '{account_data['last_game']}'", 0),
        ("Daily Login Reward", +50)
    ]
    slow_print("\nInformation saved. Preparing password guessing...\n", 0.05)
    time.sleep(1)

# ---------- Password Guessing ----------
def password_guessing(username):
    clear_screen()
    slow_print(f"[+] Starting password guessing for {username}...\n")
    fake_passwords = [f"pass{i}{random.randint(100,999)}" for i in range(1, 100)]
    fake_passwords.append(account_data["password"])
    for i, pwd in enumerate(fake_passwords, 1):
        sys.stdout.write(f"\r[*] Trying password {i}/{len(fake_passwords)}: {pwd}  ")
        sys.stdout.flush()
        time.sleep(0.05)
    print(f"\n\n[+] Password found: {account_data['password']}\n")
    time.sleep(1)

# ---------- Authenticator / Email Step ----------
def auth_step():
    clear_screen()
    slow_print("[*] Verifying authenticator & email...\n")
    for i in range(30):
        bar = "#" * (i+1) + "-" * (30-i-1)
        sys.stdout.write(f"\r[{bar}] {i*3}%")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n[+] Verification successful!\n")
    time.sleep(1)

# ---------- Dashboard ----------
def dashboard():
    while True:
        clear_screen()
        banner()
        print(f"Username: {account_data['username']}")
        print(f"Robux Balance: {account_data['robux']} 🪙")
        print(f"Password: {account_data['password']}")
        print(f"Last Game Played: {account_data['last_game']}")
        print(f"Robux Spent Last Game: {account_data['robux_spent']}")
        print(f"Last Gamepass: {account_data['last_gamepass']}")
        print("\nRecent Activity:")
        for action, amt in account_data["recent_activity"]:
            sign = "+" if amt > 0 else "-" if amt < 0 else ""
            print(f"  {action:30} {sign}{abs(amt)} Robux" if amt != 0 else f"  {action}")
        print("\nOptions:")
        print("1) Change Password")
        print("2) Add Transaction / Gamepass")
        print("3) Exit Dashboard")
        choice = input("\nSelect option: ")
        if choice == "1":
            new_pw = input("Enter new password: ")
            account_data["password"] = new_pw
            slow_print("[+] Password changed successfully!\n", 0.05)
            time.sleep(1)
        elif choice == "2":
            desc = input("Transaction / Gamepass description: ")
            amt = int(input("Amount (+ gain / - spend): "))
            account_data["recent_activity"].insert(0, (desc, amt))
            account_data["robux"] += amt
            slow_print("[+] Transaction added!\n", 0.05)
            time.sleep(1)
        elif choice == "3":
            slow_print("[*] Logging out...\n", 0.05)
            time.sleep(1)
            break
        else:
            slow_print("[-] Invalid choice!\n", 0.05)
            time.sleep(1)

# ---------- Second Menu ----------
def second_menu():
    clear_screen()
    slow_print("=== Password Guessing Menu ===\n", 0.05)
    username = input("Enter username to guess password for: ")
    password_guessing(username)
    auth_step()
    dashboard()

# ---------- Main ----------
def main():
    clear_screen()
    banner()
    slow_print("Welcome to PasswordGuesser!\n", 0.05)
    time.sleep(1)
    enter_account_info()
    second_menu()
    slow_print("Thank you for using PasswordGuesser!\n", 0.05)

if __name__ == "__main__":
    main()
