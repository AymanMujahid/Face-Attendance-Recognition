import sqlite3
import pandas as pd

def export_attendance_to_excel(file_path):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()

    c.execute("SELECT * FROM attendance")
    rows = c.fetchall()

    columns = [desc[0] for desc in c.description]

    df = pd.DataFrame(rows, columns=columns)

    df.to_excel(file_path, index=False)

    conn.close()

if __name__ == "__main__":
    export_attendance_to_excel("employee_attendance.xlsx")
