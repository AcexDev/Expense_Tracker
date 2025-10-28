from db_connection.database import db_init
import getpass, bcrypt
import time
import sys
import os
from colorama import Fore, Style, init
import re, pwinput
# from core.categories import category_bundled
# from core.viewexpense import viewing


# initialize colorama
init(autoreset=True)

def dashboard(name):
    print(f"Welcome {name}!")
    print("""\nOptions:
        •	1. Add new expense
        •	2. View all expenses
        •	3. Filter by category/date
        •	4. View summary (monthly/weekly total)
        •	5. Manage categories
        •	6. Logout
""")

def password_validation():
    while True:
        password = pwinput.pwinput("Password: ", mask="*").strip()
        if len(password) < 6:
            print("Password length is minimum of 6 characters")
        else:
            confirm_password = input("Confirm Password: ").strip()
            if password != confirm_password:
                print("Entries do not match! Retry")
            else:
                hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
                return hashed_password


def load_screen():
    os_clear()
    print(f"{'=' * 40}")
    print("WELCOME TO PERSONAL FINANCE TRACKER".center(40))
    print(f"{'=' * 40}\n")
    print("Loading app... Please wait")

    bar = "■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■"
    for i in range(1, len(bar) + 1):
        sys.stdout.write(f"\r[{bar[:i]:<35}] {int((i/len(bar))*100)}%")
        sys.stdout.flush()
        time.sleep(0.08)

    time.sleep(1)
    print("\n✨ Your productivity, your control! ✨")

def os_clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def email_input():
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    while True:
        email = input("Email: ")
        if bool(re.match(pattern, email)):
            return email
        else:
            print("Invalid email address format \nRetry")

def pause():
    input("\nPress Enter to return to menu...")
    print()

#MENUS
def tracker_main_menu(name):
    os_clear()
    print(f"{'='*30}")
    print("FINANCE TRACKER MENU".center(30))
    print(f"{'='*30}")
    print(f"Welcome {name}!\n")
    print("[1] Category Options \n[2] Expense Options\n[3] Reports/Analytics(In development)")
    print("[4] Settings \n[0] Logout")

def category_menu():
    print(f"{'-'*30}")
    print("CATEGORY OPTIONS".center(30))
    print(f"{'-' * 30}")
    print("[1] View All Categories \n[2] Add New Category")
    print("[3] Delete Category \n[0] Back to Main Menu")

def expenses_menu():
    print(f"{'-' * 30}")
    print("EXPENSE OPTIONS".center(30))
    print(f"{'-' * 30}")
    print("[1] Add New Expense \n[2] View All Expenses \n[3] Filter by Category")
    print("[4] Filter by Date \n[5] Total for a Month \n[0] Back to Main Menu")

def settings_menu():
    print(f"{'-' * 30}")
    print("SETTINGS".center(30))
    print(f"{'-' * 30}")
    print("[1] Change Password \n[2] Update Profile \n[3] Reset Data \n[0] Back to Main Menu")

def logout_menu():
    print(f"{'-' * 30}")
    print("LOGOUT CONFIRMATION".center(30))
    print(f"{'-' * 30}")
    print("Are you sure you want to logout?\n")
    print("[1] Yes, Logout \n[2]No,Return to Menu")


