from db_connection.database import db_init



#from users import user_id, name
def expense_table():
    conn = db_init()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE expenses(
                        expense_id INT PRIMARY KEY AUTO_INCREMENT,
                        user_id INT,
                        category_id INT,
                        amount DECIMAL(10,2),
                        description VARCHAR(255),
                        date DATE,
                        FOREIGN KEY(user_id) REFERENCES users(user_id),
                        FOREIGN KEY(category_id) REFERENCES categories(category_id)
                        )
                        """)
    conn.commit()
    conn.close()

