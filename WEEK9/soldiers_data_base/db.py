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


def update(soldier_id: int, data: dict) -> bool:
    conn = get_connection()
    cursor = conn.cursor()
    set_parts = [f"{key} = %s" for key in data.keys()]
    set_clause = ", ".join(set_parts)
    sql = f"UPDATE soldiers SET {set_clause} WHERE id = %s"
    values = list(data.values()) + [soldier_id]
    cursor.execute(sql, values)
    conn.commit()
    changed = cursor.rowcount > 0 
    cursor.close()
    conn.close()
    return changed

def delete(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM soldiers WHERE id = %s", (id,))
    conn.commit()
    deleted = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return deleted

def get_names_and_ranks() -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, name, ranking FROM soldiers")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_by_rank(rank: str) -> list:
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM soldiers WHERE ranking = %s",(rank,))
    in_rank = cursor.fetchall()
    cursor.close()
    conn.close()
    return in_rank

def get_active(sort:str):
    if sort.lower() not in ['asc', 'desc']:
        sort = "asc"
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM soldiers WHERE active ORDER BY name {sort.upper()}")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def distinct_units():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT unit FROM soldiers")
    units = cursor.fetchall()
    cursor.close()
    conn.close()
    return [unit[0] for unit in units]

def search_by_name(name:str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM soldiers WHERE name LIKE %s",(f"%{name}%",))
    names = cursor.fetchall()
    cursor.close()
    conn.close()
    return names



