import sqlite3
from datetime import datetime

DB_NAME = "finance_manager.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def setup_db():
    """Initializes the database structure."""
    with get_connection() as conn:
        cursor = conn.cursor()
        # Create Expenses Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                description TEXT,
                date TEXT NOT NULL
            )
        ''')
        conn.commit()

def log_expense(amount, category, description):
    """Inserts a new expense record safely."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO expenses (amount, category, description, date)
            VALUES (?, ?, ?, ?)
        ''', (amount, category, description, date_str))
        conn.commit()

def get_monthly_summary():
    """Uses SQL math (SUM and GROUP BY) to calculate totals per category."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT category, SUM(amount) 
            FROM expenses 
            GROUP BY category
        ''')
        return cursor.fetchall()
