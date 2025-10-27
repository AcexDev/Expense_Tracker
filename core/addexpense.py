from db_connection.database import db_init
from datetime import datetime

def required_lists(conn, cursor, user_id):
    search = "SELECT * FROM categories WHERE user_id = %s"

    bundle = (user_id, )
    cursor.execute(search, bundle)
    result1 = cursor.fetchall()
    category_id_list = []
    name_list = []
    current_user_id_list = []

    for x in result1:
        category_id = x[0]
        name = x[1]
        currentuser_id = x[2]

        category_id_list.append(category_id)
        name_list.append(name)
        current_user_id_list.append(currentuser_id)
    return category_id_list, name_list, current_user_id_list, result1

def add_expense_ops(conn, cursor, user_id):
    category_idlist, name_list, currentuser_id_list, result1 = required_lists(conn, cursor, user_id)
    query1 = """INSERT INTO expenses(
                    user_id, category_id, amount, description, date)
                    VALUES(%s, %s, %s, %s, %s)"""
    print("ADD NEW EXPENSE: \n")
    while True:
        category = input("Enter expense category name(must be an existing name): ").strip()
        if category not in name_list:
            print("Category doesn't exist. Retry")
        else:
            break
    description = input("Enter description if any: ")
    date = input("Enter date(press Enter for today): ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    category_id = None
    for y in result1:
        if category == y[1]:
            category_id = y[0]
    amount = None
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Amount is strictly in figures. Retry")
    query1_params = (user_id, category_id, amount, description, date)
    cursor.execute(query1, query1_params)
    conn.commit()
    print("Expense successfully recorded")

def add_expenses(user_id):
    conn = db_init()
    cursor = conn.cursor()
    add_expense_ops(conn, cursor, user_id)

def category_check(user_id):
    conn = db_init()
    cursor = conn.cursor()

    while True:
        category = input("Enter expense category name (must be an existing name): ").strip()
        cursor.execute(
            "SELECT name FROM categories WHERE user_id = %s AND name = %s",
            (user_id, category)
        )
        result = cursor.fetchone()
        category_name = result[0]
        if result:
            cursor.close()
            conn.close()
            return category_name
        else:
            print("Category doesn't exist ⚠️ Try again.")

def inputs(user_id):
    category_name = category_check(user_id)
    description = input("Enter description if any: ")
    date = input("Enter date(press Enter for today): ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    amount = None
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Amount is strictly in figures. Retry")
    parameters = (user_id, amount, description, date)
    return parameters

def add_expense(user_id):
    conn = db_init()
    cursor = conn.cursor()
    parameters = inputs(user_id)
    query = """INSERT INTO expenses(
                user_id, amount, description, date)
               VALUES(%s, %s, %s, %s, %s)"""
    cursor.execute(query, parameters)
    conn.commit()

