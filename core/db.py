import sqlite3

DB_PATH = "bot.db"


def get_db():
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_db() as db:
        cursor = db.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            language TEXT,
            authorized INTEGER DEFAULT 0
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS parses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            target TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        db.commit()
