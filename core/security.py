from db_connection.database import db_init
from utilities.utils import password_validation, email_input
import bcrypt

secret_questions = {
    "q1" : "What was the name of your first pet?",
    "q2" : "What is your mother’s maiden name?",
    "q3" : "In what city were you born?",
    "q4" : "What was your first school’s name?",
    "q5" : "What is your favorite food?"
}



def email_validation():
    conn = db_init()
    cursor = conn.cursor()
    while True:
        email = email_input()
        cursor.execute("SELECT user_id FROM users WHERE email = %s", (email,))
        result = cursor.fetchone()
        try:
            user_id = result[0]
            return user_id

        except TypeError:
            print("Entered email isn't valid!\n")

def question_list():
    print(f"""{'='*35}\nWelcome to Password reset setup \n{'='*35} \nChoose Reset Question:\n
             1- {secret_questions["q1"]}
             2- {secret_questions["q2"]}
             3- {secret_questions["q3"]}
             4- {secret_questions["q4"]}
             5- {secret_questions["q5"]}""")

def password_reset():
    question_list()
    while True:
        try:
            choice = int(input("Choose Question number: ").strip())
            if 1 <= choice <= 5:
                return choice
            else:
                print("Invalid! You can only choose between 1 and 5.")
        except ValueError:
            print("Invalid input")

def question_match(choice):
    if choice == 1:
        print(secret_questions["q1"])
    elif choice == 2:
        print(secret_questions["q2"])
    elif choice == 3:
        print(secret_questions["q3"])
    elif choice == 4:
        print(secret_questions["q4"])
    elif choice == 5:
        print(secret_questions["q5"])

def answers():
    choice = password_reset()
    question_match(choice)
    while True:
        answer = input("> ").strip().lower()
        print("Confirm answer")
        confirm_answer = input("> ").strip().lower()
        if answer != confirm_answer:
            print("Entries do not match! Retry")
        else:
            print("Processing")
            break

    hashed_answer = bcrypt.hashpw(answer.encode(), bcrypt.gensalt())
    return choice, hashed_answer

def security_question_final_ops():
    conn = db_init()
    cursor = conn.cursor()
    user_id = email_validation()
    query = """UPDATE users SET 
                security_question = %s, security_answer_hash = %s WHERE user_id = %s"""
    choice, hashed_answer = answers()
    params = (choice, hashed_answer, user_id)
    cursor.execute(query, params)
    conn.commit()
    print("Secret answer successfully set!")



def validate_answer():
    conn = db_init()
    cursor = conn.cursor()
    user_id = email_validation()
    cursor.execute("SELECT security_question, security_answer_hash FROM users WHERE user_id = %s", (user_id, ))
    results = cursor.fetchall()
    question_no = None
    answer_hashed = None
    for result in results:
        question_no = result[0]
        answer_hashed = result[1]
    if not question_match(question_no):
        print("Account recovery method not set!")
        return
    answer = input("> ").strip().lower()
    if bcrypt.checkpw(answer.encode(), answer_hashed.encode()):
        print("Match found!")
        return user_id
    else:
        print("Answer mismatch")

def change_password(user_id):
    conn = db_init()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE user_id = %s", (user_id,))
    results = cursor.fetchone()
    password = results[0]
    current_password = input("Enter Current Password: ").strip()
    if bcrypt.checkpw(current_password.encode(), password.encode()):
        print("Verification Successful")
        query = "UPDATE users SET password = %s WHERE user_id = %s"
        print(f"{'-' * 20} \nSet New Password \n{'-' * 20}")
        hashed_password = password_validation()
        params = (hashed_password.decode(), user_id)
        cursor.execute(query, params)
        conn.commit()
        print("Password Changed successfully!")
    else:
        print("Incorrect password")



def set_new_password():
    user_id = validate_answer()
    if not user_id:
        return False
    conn = db_init()
    cursor = conn.cursor()
    query = "UPDATE users SET password = %s WHERE user_id = %s"
    print(f"{'-' * 20} \nSet New Password \n{'-' * 20}")
    hashed_password = password_validation()
    params = (hashed_password.decode(), user_id)
    cursor.execute(query, params)
    conn.commit()
    print("Password Changed successfully!")
    return True


