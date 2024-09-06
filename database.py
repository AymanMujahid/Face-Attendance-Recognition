import sqlite3

def create_tables():
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id TEXT NOT NULL,
            entry_time TEXT,
            exit_time TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_entry_exit(employee_id, entry_time=None, exit_time=None):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()

    if entry_time:
        c.execute("INSERT INTO attendance (employee_id, entry_time) VALUES (?, ?)", (employee_id, entry_time))

    if exit_time:
        c.execute("UPDATE attendance SET exit_time=? WHERE employee_id=? AND exit_time IS NULL", (exit_time, employee_id))

    conn.commit()
    conn.close()
