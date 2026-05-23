import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

# --- DATA LAYER ---
DB_NAME = "finance_manager.db"

def setup_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )
        ''')
        conn.commit()

def log_expense(amount, category):
    date_str = datetime.now().strftime("%Y-%m-%d")
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO expenses (amount, category, date)
            VALUES (?, ?, ?)
        ''', (amount, category, date_str))
        conn.commit()

def get_monthly_summary():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category')
        return cursor.fetchall()


# --- PRESENTATION LAYER ---
class FinanceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Capital Architect - Finance Dashboard")
        self.root.geometry("450x400")
        self.root.configure(bg="#1e272e") # Deep obsidian theme
        
        setup_db()
        self.create_widgets()
        self.refresh_dashboard()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="FINANCE DASHBOARD", font=("Helvetica", 16, "bold"), bg="#1e272e", fg="#0beedd")
        title.pack(pady=15)

        # Input Frame
        input_frame = tk.Frame(self.root, bg="#1e272e")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Amount ($):", bg="#1e272e", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.amount_entry = tk.Entry(input_frame, font=("Arial", 12), width=15)
        self.amount_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(input_frame, text="Category:", bg="#1e272e", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.category_box = ttk.Combobox(input_frame, values=["Food", "Rent", "Utilities", "Entertainment", "Other"], width=13, font=("Arial", 11))
        self.category_box.grid(row=1, column=1, padx=5, pady=5)
        self.category_box.current(0)

        # Action Button
        submit_btn = tk.Button(self.root, text="Log Expense", command=self.handle_submission, bg="#0beedd", fg="#1e272e", font=("Arial", 11, "bold"), height=1, width=15, relief="flat")
        submit_btn.pack(pady=10)

        # Summary Display Area
        self.summary_box = tk.Text(self.root, height=8, width=45, bg="#2f3640", fg="white", font=("Courier New", 11), bd=0, padx=10, pady=10)
        self.summary_box.pack(pady=15)

    def handle_submission(self):
        try:
            amount = float(self.amount_entry.get())
            category = self.category_box.get()
            
            if amount <= 0:
                raise ValueError
                
            log_expense(amount, category)
            self.amount_entry.delete(0, tk.END)
            self.refresh_dashboard()
            messagebox.showinfo("Success", "Transaction secured and logged.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive amount.")

    def refresh_dashboard(self):
        # Clear previous text
        self.summary_box.config(state=tk.NORMAL)
        self.summary_box.delete("1.0", tk.END)
        
        # Pull live aggregated data from SQL
        summary_data = get_monthly_summary()
        
        self.summary_box.insert(tk.END, f"{'CATEGORY':<20}{'TOTAL SPENT':>15}\n")
        self.summary_box.insert(tk.END, "—" * 35 + "\n")
        
        grand_total = 0
        for category, total in summary_data:
            self.summary_box.insert(tk.END, f"{category:<20}${total:>14,.2f}\n")
            grand_total += total
            
        self.summary_box.insert(tk.END, "—" * 35 + "\n")
        self.summary_box.insert(tk.END, f"{'GRAND TOTAL':<20}${grand_total:>14,.2f}")
        self.summary_box.config(state=tk.DISABLED)

# Launching System
if __name__ == "__main__":
    window = tk.Tk()
    app = FinanceApp(window)
    window.mainloop()
