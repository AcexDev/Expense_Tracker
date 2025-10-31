import bcrypt, time, sys, pwinput
from db_connection.database import db_init
from core.security import security_question_final_ops, set_new_password
from utilities.utils import password_validation, os_clear, email_input
from colorama import Fore, Style, init

# initialize colorama
init(autoreset=True)

def user_table():
    conn = db_init()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                        user_id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR(255),
                        email VARCHAR(100) UNIQUE,
                        password VARCHAR(255),
                        security_question VARCHAR(255),
                        security_answer_hash VARCHAR(255)""")
    conn.commit()
    conn.close()

def check_email():
    conn = db_init()
    cursor = conn.cursor()
    while True:
        email = email_input()
        cursor.execute("SELECT user_id from users WHERE email = %s", (email,))
        result = cursor.fetchone()
        try:
            user = result[0]
            print("Email already in use. Try another!")
        except TypeError:
            return email

def register_user():
    try:
        conn = db_init()
        cursor = conn.cursor()
        inserts = "INSERT INTO users(name, email, password) VALUES(%s, %s, %s)"
        name = input("Full name: ")
        email = check_email()
        hashed_password = password_validation()
        cursor.execute(inserts, (name, email, hashed_password.decode()))
        conn.commit()
        print(f"Account successfully created for {name}")
        post_register_ops()
    except Exception as e:
        print(f"Connection error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def post_register_ops():
    while True:
        print(f"\n{Fore.CYAN}Set up account recovery now?\n1- Yes \n2- Skip")
        choice = input("> ").strip()
        if choice == "1":
            security_question_final_ops()
            break
        elif choice == "2":
            return
        else:
            print("Invalid choice!")



def login_params(stored_pw, result, count):
    while True:
        password = pwinput.pwinput("Password: ",mask="*").strip()
        if len(password) < 6:
            print("Password length is minimum of 6 characters")
        else:
            print("\n(Verifying credentials...)")
            password = password.encode()
            if bcrypt.checkpw(password, stored_pw.encode()):
                print("✅ Login Successful! Redirecting to main menu...")
                return None
            else:
                count -= 1
                print(f"Invalid password.{count} retrie(s) left")
                if count <= 0:
                    print("Trial limit reached. Login aborted!")
                    return None

def user_login():
    try:
        conn = db_init()
        cursor = conn.cursor()
        while True:
            email = email_input()
            cursor.execute("SELECT user_id, name, password FROM users WHERE email = %s", (email,))
            count = 3
            try:
                result = cursor.fetchone()
                stored_pw = result[2]
                login_params(stored_pw, result, count)
                user_id, name = result[0], result[1]
                return user_id, name
            except TypeError:
                print("No account for entered email address")
    except Exception as e:
        print(f"Connection error: {e}")


def acct_menu():
    time.sleep(2.5)
    os_clear()
    print(f"{'='*30}")
    print("LOGIN PORTAL".center(30))
    print(f"{'=' * 30}")
    print("Options:\n[1] Login to Existing Account \n[2] Create New Account")
    print("[3] Account Recovery \n[0] Exit")
    user_choice = input("> ")
    if user_choice == "1":
        os_clear()
        print(f"{'-' * 30}")
        print("USER LOGIN".center(30))
        print(f"{'-' * 30}")
        return user_login()
    elif user_choice == "2":
        os_clear()
        print(f"{'-'*30}")
        print("CREATE NEW ACCOUNT".center(30))
        print(f"{'-' * 30}")
        register_user()
        print("\nRedirecting to Login...\n")
        time.sleep(1)
        return user_login()
    elif user_choice == "3":
        os_clear()
        print(f"{'-'*30}")
        print("ACCOUNT RECOVERY PORTAL".center(30))
        print(f"{'-' * 30}")
        if set_new_password():
            return user_login()
        else:
            return acct_menu()
    elif user_choice == "0":
        sys.exit("Program terminated")
    else:
        print("Invalid input!")


