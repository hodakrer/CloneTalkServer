import sqlite3

DB_PATH = 'users.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            phone_number TEXT UNIQUE,
            password_hash TEXT
        )''')
        conn.commit()


def save_user(phone_number, password_hash):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO users (phone_number, password_hash) VALUES (?, ?)",
                    (phone_number, password_hash))
        conn.commit()

def find_user_by_phone(phone_number):
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.cursor()
        cur.execute("SELECT password_hash FROM users WHERE phone_number = ?", (phone_number,))
        row = cur.fetchone()
        return row  # None or (password_hash,)