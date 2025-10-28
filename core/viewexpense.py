from db_connection.database import db_init
from colorama import Fore, Style, init
from tabulate import tabulate
from utilities.utils import expenses_menu,pause, os_clear
from core.addexpense import add_expenses
import time

def view_all(user_id):
    join_query = """SELECT e.description, e.amount, e.date, c.name 
                        FROM expenses e JOIN categories c 
                        ON e.category_id = c.category_id 
                        WHERE e.user_id = %s"""
    main_query_params = (user_id,)
    return main_query_params, join_query
def filter_by_category(user_id):
    n = 0
    bundle = [user_id]
    while True:
        category_1 = input(f"Enter Category {n + 1}(Press Enter to finish selection):")
        if not category_1:
            break
        bundle.append(category_1)
        n += 1
    if n == 0:
        print("No Categories entered. Operation Aborted!")

    command = "%s"
    main_query_params = tuple(bundle)
    join_query = f"""SELECT e.description, e.amount, e.date, c.name 
                            FROM expenses e JOIN categories c 
                            ON e.category_id = c.category_id 
                            WHERE e.user_id = %s AND c.name IN ({','.join([command] * n)})"""
    return main_query_params, join_query

def filter_by_date(user_id):
    join_query = """SELECT e.description, e.amount, e.date, c.name 
                            FROM expenses e JOIN categories c 
                            ON e.category_id = c.category_id 
                            WHERE e.user_id = %s AND e.date BETWEEN %s AND %s"""

    date_initial = input("Enter Start date(Year-Month-Day: ")
    date_final = input("Enter End date(Year-Month-Day: ")
    main_query_params = (user_id, date_initial, date_final)
    return main_query_params, join_query

months = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

def month_input():
    global month_name
    while True:
        user_input = input("Enter month: ").strip().title()
        if user_input in months:
            month_number = int(f"{months[user_input]:02}")
            month_name = user_input
            return user_input, month_number

        else:
            print("Invalid. Retry!")

def total_by_month_params(user_id):
    query = """SELECT SUM(amount) FROM expenses
                WHERE user_id = %s AND date BETWEEN %s AND %s"""
    while True:
        try:
            year = input("Enter year: ")
            year = int(year)
            if 2000 <= year <= 2025:
                break
            else:
                print("Year specified is out of range.")
        except ValueError:
            print("Invalid input!")
    month, month_fig = month_input()
    initial_date = f"{year}-{month_fig}-01"
    final_date = f"{year}-{month_fig}-31"
    params_bundled = (user_id, initial_date, final_date)
    return query, params_bundled


def total__by_month(user_id):
    conn = db_init()
    cursor = conn.cursor()
    query, params = total_by_month_params(user_id)
    cursor.execute(query, params)
    results = cursor.fetchone()
    try:
        total = results[0]
        if total == None:
            print(f"No recorded expenses for the month {month_name}")
        else:
            print(f"Total for the month {month_name} is #{total}")
    except TypeError:
        print(f"No recorded expenses for the month {month_name}")

def view_action(main_query_params, join_query):
    conn = db_init()
    cursor = conn.cursor()
    cursor.execute(join_query, main_query_params)
    results = cursor.fetchall()
    for i, result in enumerate(results):
        description = result[0]
        amount = result[1]
        date = result[2]
        category_name = result[3]
        print(f"{i + 1:<3}- Category: {category_name:<10}| Description: {description:<30}| Amount: {amount:<7}| Date: {date}")


def viewing(user_id):
    while True:
        os_clear()
        expenses_menu()
        choice = input("Enter Choice: ").strip()
        print()
        if choice == "1":
            add_expenses(user_id)
            pause()
        if choice == "2":
            main_query_params, join_query = view_all(user_id)
            view_action(main_query_params, join_query)
            pause()
        elif choice == "3":
            main_query_params, join_query = filter_by_category(user_id)
            view_action(main_query_params, join_query)
            pause()
        elif choice == "4":
            main_query_params, join_query = filter_by_date(user_id)
            view_action(main_query_params, join_query)
            pause()
        elif choice == "5":
            total__by_month(user_id)
            pause()
        elif choice == "0":
            break
        else:
            print("Invalid Choice(choice between 0-5)")



