import sqlite3

DB_NAME = "tasks.db"

def connect():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def add_task(name):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tasks (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()

def get_tasks():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return rows