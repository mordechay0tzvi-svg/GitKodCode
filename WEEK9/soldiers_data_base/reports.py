import db

def count_by_unit() -> list:
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
    SELECT unit,
    COUNT(*) AS total
    FROM soldiers
    GROUP BY unit
    ORDER BY total DESC
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{row['unit']:row["total"]} for row in rows]

def get_summary() -> dict:
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT COUNT(*) AS total FROM soldiers")
    total = cursor.fetchone()["total"]
    cursor.execute("SELECT COUNT(*) AS active FROM soldiers WHERE active")
    active = cursor.fetchone()["active"]
    cursor.close()
    conn.close()
    return {"total": total, "active": active, "inactive": total - active}

def get_missing_data():
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE ranking IS NULL")
    not_ranked = cursor.fetchall()
    cursor.close() 
    conn.close()
    return not_ranked

def get_units_with_multiple_soldiers():
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT unit, COUNT(*) AS total FROM soldiers GROUP BY unit HAVING total > 1")
    units = cursor.fetchall()
    cursor.close()
    conn.close()
    return units


print(get_missing_data())