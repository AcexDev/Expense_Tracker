from db_connection.database import db_init
def create_tables():
    try:
        conn = db_init()
        cursor = conn.cursor()


        with open("db_connection/schema.sql", "r") as f:
            sql_script = f.read()

        # ✅ Execute statements one by one
        for statement in sql_script.split(";"):
            stmt = statement.strip()
            if stmt:
                cursor.execute(stmt)
        conn.commit()
    except Exception as e:
        print(f"Startup unsuccessful: {e}")
    finally:
        conn.close()
    print("✅ All tables created and verified successfully.")
