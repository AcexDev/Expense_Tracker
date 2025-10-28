import mysql.connector
from dotenv import load_dotenv
import os
# def db_init():
#      return mysql.connector.connect(
#          host="sql7.freesqldatabase.com",
#          user="sql7804420",
#          password="2wZcwsbZum",
#          database="sql7804420",
#          port=3306
#      )

load_dotenv()
def db_init():
    try:
        return mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=os.getenv("DB_PORT")
        )
    except Exception as e:
        print(f"Connection error: {e}")