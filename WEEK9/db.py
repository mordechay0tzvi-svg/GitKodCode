import mysql.connector

def get_connection():
    return mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="secret",
    database="soldiers_db"
    )
def get_schema() -> list:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DESCRIBE soldiers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [{"column": row[0], "type": row[1]} for row in rows]

def get_all() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


def get_by_id(id)-> dict | None:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row


def create(name: str, ranking: str, unit: str, active=True):
    conn = get_connection()
    cursor = conn.cursor()
    command = "INSERT INTO soldiers (name, ranking, unit, active) VALUES (%s, %s, %s, %s)"
    values = (name, ranking, unit, active)
    cursor.execute(command, values)
    conn.commit()
    new_id = cursor.lastrowid 
    cursor.close()
    conn.close()
    return new_id

def update(id, data):
    pass

def delete(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM soldiers WHERE id = %s", (id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return "deleted"




