import MySQLdb
import sys

def create_database():
    try:
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            port=3306
        )
        cursor = db.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if 'db' in locals():
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python MySQLServer.py <username> <password>")
    else:
        create_database()