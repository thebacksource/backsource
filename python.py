#!/usr/bin/env python3
import time, random, sys

# Fake password list
passwords = [
    "password123", "qwerty", "letmein", "roblox123", "gamer2025",
    "hunter2", "guest123", "dragonlord", "noobmaster69", "coolkid77"
]

# Fake Roblox account data
fake_account = {
    "username": "NoobSlayer9000",
    "robux": 5420,
    "password": "supersecure!",
    "recent_activity": [
        ("Bought 'Epic Sword'", -150),
        ("Sold 'Golden Crown'", +800),
        ("Gamepass Purchase: VIP Lounge", -500),
        ("Daily Login Reward", +100),
    ]
}

def guessing_animation():
    print("\n[+] Starting password guessing...\n")
    for i, pwd in enumerate(passwords, 1):
        sys.stdout.write(f"\r[*] Trying password {i}/{len(passwords)}: {pwd}...")
        sys.stdout.flush()
        time.sleep(0.6)
    print("\n\n[+] Password found:", fake_account["password"])
    time.sleep(1)

def show_dashboard():
    print("\n=== Roblox Account Dashboard ===")
    print(f"Username: {fake_account['username']}")
    print(f"Robux Balance: {fake_account['robux']} 🪙")
    print("\nRecent Activity:")
    for action, amount in fake_account["recent_activity"]:
        sign = "+" if amount > 0 else "-"
        print(f"  {action}   {sign}{abs(amount)} Robux")
    print("\nOptions:")
    print(" 1) Change Password")
    print(" 2) Add Fake Transaction")
    print(" 3) Logout")

def change_password():
    new_pwd = input("Enter new password: ")
    fake_account["password"] = new_pwd
    print("[+] Password changed successfully!\n")

def add_transaction():
    item = input("Enter transaction description: ")
    amt = int(input("Enter amount (positive or negative): "))
    fake_account["recent_activity"].insert(0, (item, amt))
    fake_account["robux"] += amt
    print("[+] Transaction added!\n")

def main():
    guessing_animation()
    while True:
        show_dashboard()
        choice = input("\nSelect option: ")
        if choice == "1":
            change_password()
        elif choice == "2":
            add_transaction()
        elif choice == "3":
            print("[*] Logging out...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
