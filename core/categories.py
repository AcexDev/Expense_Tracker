import mysql.connector, time
from db_connection.database import db_init
from utilities.utils import category_menu, pause, os_clear


def category_table():
    conn = db_init()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE categories(
                        category_id INT PRIMARY KEY AUTO_INCREMENT,
                        name VARCHAR (255),
                        user_id INT,
                        FOREIGN KEY(user_id) REFERENCES users(user_id),
                        UNIQUE(user_id, name)
                        )""")
    conn.commit()
    conn.close()

#category_table()
def add_category(user_id):
    conn = db_init()
    cursor = conn.cursor()
    query = """INSERT INTO categories(
                name, user_id)
                VALUES(%s, %s) """
    while True:
        category_name = input("Enter Expense Category Name: ")
        print(f"Confirm creation of new category: {category_name}.\n\n1- To confirm\n*Any other key- Abort and retry")
        validation = input("> ")
        if validation != "1":
            print("Input cleared! Retry")
        else:
            print("Processing...\n")
            time.sleep(1)
            try:
                finals = (category_name, user_id)

                cursor.execute(query, finals)
                conn.commit()
                print(f"\nCategory: {category_name} successfully added!\n1- Add new Category\nAny other key- Menu")
                further_action = input("> ")
                if further_action != "1":
                    print("Returning to menu")
                    break
                else:
                    continue
            except mysql.connector.IntegrityError:
                print("⚠️Category already exists. Add a new category\n")



def view_category(user_id):
    conn = db_init()
    cursor = conn.cursor()
    query = "SELECT name FROM categories WHERE user_id = %s"
    cursor.execute(query, (user_id,))

    results = cursor.fetchall()
    print(f"{'-'*30}")
    print("Categories: ".center(30))
    print(f"{'-' * 30}")
    for i, field in enumerate(results):
        print(f"Category {i+1}: {field[0]}")
        conn.close()

def delete_category(user_id):
    conn = db_init()
    cursor = conn.cursor()
    query = "SELECT name FROM categories WHERE user_id = %s"
    cursor.execute(query,(user_id,))
    categories = [row[0] for row in cursor.fetchall()]
    print("Categories:\n")
    for i, category in enumerate(categories, start=1):
        print(f"{i}- {category}")
    while True:
        selection = input("Input Category name you wish to delete: ").strip()
        if selection not in categories:
            print("Category doesn't exist. Retry")
        else:
            query = "DELETE FROM categories WHERE name = %s AND user_id = %s"
            cursor.execute(query, (selection,user_id))
            print(f"{selection} successfully deleted.")
            conn.commit()
            break
#
# def delete_category1(user_id):
#     conn = db_init()
#     cursor = conn.cursor()
#     query = "SELECT name FROM categories WHERE user_id = %s"
#     cursor.execute(query, (user_id, ))
#     categories = [row[0] for row in cursor.fetchall()]
#     print("Categories:\n")
#     n = 0
#     for category in categories:
#         print(f"{n+1}- {category}")
#     while True:
#         selection = input("Input Category name you wish to delete: ").strip()
#         query = "DELETE FROM categories WHERE name = %s AND user_id =%s"
#         cursor.execute(query, (selection,))
#
#         if cursor.rowcount == 0:   #Use rowcount to determine if any row was deleted
#             print("Category doesn't exist. Retry")
#         else:
#             query = "DELETE FROM categories WHERE name = %s"
#             cursor.execute(query, (selection,))
#             print(f"{selection} successfully deleted.")
#             conn.commit()
#             break


def category_bundled(user_id):
    while True:
        os_clear()
        category_menu()
        choice = input("Enter choice: ").strip()
        print()
        if choice == "1":
            view_category(user_id)
            pause()
        elif choice == "2":
            add_category(user_id)
            pause()
        elif choice == "3":
            delete_category(user_id)
            pause()
        elif choice == "0":
            print("Returning to Main menu")
            break
        else:
            print("Invalid input!")

