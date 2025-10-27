import time
from core.categories import category_bundled
from core.users import acct_menu
from utilities.utils import load_screen, tracker_main_menu, os_clear
from core.viewexpense import viewing
from utilities.settings import settings_navigation
from db_connection.setup import create_tables

def navigation(user_id):
    while True:
        print("\n")
        tracker_main_menu()
        choice = input("Enter choice: ").strip()
        if choice == "1":
            category_bundled(user_id)
        elif choice == "2":
            viewing(user_id)
        elif choice == "3":
            print("\n\nIN DEVELOPMENT")
            time.sleep(2)
        elif choice == "4":
            settings_navigation(user_id)
        elif choice == "0":
            break
        else:
            print("Invalid Choice(Enter between 0-4)")

user_id = None
def main():
    create_tables()
    os_clear()
    load_screen()
    user_details = acct_menu()
    if not user_details:
        print("Returning to Menu")
    else:
        user_id, name = user_details
        navigation(user_id)



if __name__ == "__main__":
    main()

#FIX ACCOUNT RECOVERY!