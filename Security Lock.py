import sqlite3
import security  # Our new security layer

DB_NAME = "secure_finance.db"

def setup_secure_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS secure_expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category BLOB NOT NULL,  -- Scrambled bytes
                date TEXT NOT NULL
            )
        ''')
        conn.commit()

def log_secure_expense(amount, category):
    # Encrypt the category before saving it to the database
    encrypted_category = security.encrypt_data(category)
    
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO secure_expenses (amount, category, date)
            VALUES (?, ?, '2026-05-23')
        ''', (amount, encrypted_category))
        conn.commit()

def get_secure_summary():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT category, amount FROM secure_expenses')
        rows = cursor.fetchall()
        
        # We must decrypt the categories in Python 
        # because the database engine doesn't have our secret key!
        decrypted_data = {}
        for encrypted_cat, amount in rows:
            real_cat = security.decrypt_data(encrypted_cat)
            decrypted_data[real_cat] = decrypted_data.get(real_cat, 0) + amount
            
        return decrypted_data.items()
