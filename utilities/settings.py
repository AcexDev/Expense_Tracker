from core.security import change_password
from utilities.utils import email_input, settings_menu, pause, os_clear
from db_connection.database import db_init
from core.security import change_password

def update_profile(user_id):
    conn = db_init()
    cursor = conn.cursor()
    print(f"\n{'-' * 30}")
    print("PROFILE UPDATE".center(30))
    print(f"{'-' * 30}")
    print("\n[1] Update Name \n[2] Update Email \n[3] Update Name and Email")
    cursor.execute("SELECT name, email FROM users WHERE user_id = %s", (user_id,))
    results = cursor.fetchone()
    current_name, current_email = results
    choice = input("Enter choice:")
    if choice == "1":
        new_name = input("Enter Full Name: ").strip()
        current_name = new_name
    elif choice == "2":
        email = email_input()
        current_email = email
    elif choice == "3":
        new_name = input("Enter Full Name: ").strip()
        email = email_input()
        current_email = email
        current_name = new_name
    try:
        cursor.execute("""UPDATE users
                            SET name = %s, email = %s WHERE user_id = %s""",
                       (current_name, current_email, user_id))
        conn.commit()
        print("Profile Updated successfully!")
    except Exception as e:
        print(f"Not Successful! Error:{e}")

def reset_data(user_id):
    print(f"\n{'-' * 30}")
    print("DATA RESET".center(30))
    print(f"{'-' * 30}")
    confirm = input("⚠️This will delete all your Data. Enter 'CONFIRM' to Proceed: ").lower()
    if confirm != 'confirm':
        print("Reset Cancelled.")
    else:
        try:
            conn = db_init()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM expenses WHERE user_id = %s", (user_id,))
            cursor.execute("DELETE FROM categories WHERE user_id = %s", (user_id,))
            conn.commit()
            print("Data Reset Successfully!")
        except Exception as e:
            print(f"Error while resetting data: {e}")


def settings_navigation(user_id):
    while True:
        os_clear()
        settings_menu()
        choice = input("Enter Choice: ").strip()
        print()
        if choice == "1":
            change_password(user_id)
            pause()
        elif choice == "2":
            update_profile(user_id)
            pause()
        elif choice == "3":
            reset_data(user_id)
            pause()
        elif choice == "0":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")


