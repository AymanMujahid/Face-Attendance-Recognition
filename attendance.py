import sqlite3
from datetime import datetime

def log_entry_exit(employee_id, entry_time=None, exit_time=None):
    try:
        conn = sqlite3.connect('attendance.db')
        c = conn.cursor()

        if entry_time:
            c.execute("SELECT id, exit_time FROM attendance WHERE employee_id=? AND date(entry_time)=date(?)", (employee_id, entry_time))
            record = c.fetchone()
            
            if not record:
                c.execute("INSERT INTO attendance (employee_id, entry_time) VALUES (?, ?)", (employee_id, entry_time))
            elif record and record[1]:
                c.execute("UPDATE attendance SET exit_time=NULL WHERE id=?", (record[0],))

        if exit_time:
            c.execute("UPDATE attendance SET exit_time=? WHERE employee_id=? AND exit_time IS NULL", (exit_time, employee_id))

        conn.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()
