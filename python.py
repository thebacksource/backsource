#!/usr/bin/env python3
import os, time, sys, random

# Fake account template
fake_account = {
    "username": "",
    "robux": 1000,
    "password": "",
    "recent_activity": [
        ("Bought 'Starter Pack Gamepass'", -100),
        ("Daily Login Bonus", +50),
        ("Played 'Adopt Me!'", 0)
    ]
}

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def main_menu():
    clear_screen()
    print("=== Roblox Security Simulator ===")
    print("1) Start password guessing")
    print("2) Exit")
    choice = input("Select: ")
    return choice

def guessing_animation(username, password_list):
    clear_screen()
    print(f"[+] Starting password guessing for user: {username}\n")
    for i, pwd in enumerate(password_list, 1):
        sys.stdout.write(f"\r[*] Trying password {i}/{len(password_list)}: {pwd}...")
        sys.stdout.flush()
        time.sleep(0.5)
    correct = password_list[-1]
    print(f"\n\n[+] Password found: {correct}\n")
    fake_account["username"] = username
    fake_account["password"] = correct
    time.sleep(1)

def show_dashboard():
    clear_screen()
    print(f"=== Roblox Account Dashboard ===\n")
    print(f"Username: {fake_account['username']}")
    print(f"Robux Balance: {fake_account['robux']} 🪙")
    print(f"Password: {fake_account['password']}")
    print("\nRecent Activity:")
    for action, amt in fake_account["recent_activity"]:
        sign = "+" if amt > 0 else "-" if amt < 0 else ""
        print(f"  {action:30} {sign}{abs(amt)} Robux" if amt != 0 else f"  {action}")
    print("\nOptions:")
    print(" 1) Change Password")
    print(" 2) Add Fake Transaction")
    print(" 3) Logout")

def change_password():
    new_pwd = input("Enter new password: ")
    fake_account["password"] = new_pwd
    print("[+] Password changed successfully!")
    time.sleep(1)

def add_transaction():
    item = input("Enter transaction description: ")
    amt = int(input("Enter amount (+ for gain, - for spend): "))
    fake_account["recent_activity"].insert(0, (item, amt))
    fake_account["robux"] += amt
    print("[+] Transaction added!\n")
    time.sleep(1)

def guessing_flow():
    username = input("Enter username: ")
    pw_input = input("Enter passwords (comma-separated, last is correct): ")
    password_list = [p.strip() for p in pw_input.split(",") if p.strip()]
    if not password_list:
        print("[-] No passwords entered!")
        time.sleep(2)
        return
    guessing_animation(username, password_list)
    while True:
        show_dashboard()
        choice = input("\nSelect option: ")
        if choice == "1":
            change_password()
        elif choice == "2":
            add_transaction()
        elif choice == "3":
            print("[*] Logging out...")
            time.sleep(1)
            break
        else:
            print("Invalid choice!")
            time.sleep(1)

def main():
    while True:
        choice = main_menu()
        if choice == "1":
            guessing_flow()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
            time.sleep(1)

if __name__ == "__main__":
    main()
