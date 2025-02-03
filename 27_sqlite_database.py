# Working with SQLite database
import sqlite3

def create_connection(db_name):
    """Create a connection to the SQLite database."""
    return sqlite3.connect(db_name)

def create_table(conn):
    """Create a table if it doesn't already exist."""
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        )
    ''')
    conn.commit()

def insert_user(conn, name, age):
    """Insert a user into the database."""
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()

def fetch_users(conn):
    """Fetch all users from the database."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("Users in database:", users)

def main():
    db_name = "example.db"
    conn = create_connection(db_name)
    
    try:
        create_table(conn)
        insert_user(conn, "Alice", 25)
        insert_user(conn, "Bob", 30)
        fetch_users(conn)
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        conn.close()
        print("Database connection closed.")

if __name__ == "__main__":
    main()
