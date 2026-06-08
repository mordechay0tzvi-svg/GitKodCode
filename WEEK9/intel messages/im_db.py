import mysql.connector
 
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="secret",
        database="soldiers_db")

def is_valid_classification():
    im_db = get_connection()
    cursor = im_db.cursor()
    cursor.execute("SHOW COLUMNS FROM intelmessages LIKE 'classification'")
    column_info = cursor.fetchone()
    return column_info

def get_schema() -> list:
    im_db = get_connection()
    cursor = im_db.cursor()
    cursor.execute("DESCRIBE intelmessages")
    rows = cursor.fetchall()
    cursor.close()
    im_db.close()
    return [{"column": row[0], "type": row[1]} for row in rows]

def get_all_messages():
    im_db = get_connection()
    cursor = im_db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM intelmessages")
    rows = cursor.fetchall()
    cursor.close()
    im_db.close()
    return rows

def add_message(unit:str, classification:str, content:str, source:str):
    im_db = get_connection()
    cursor = im_db.cursor()
    command = "INSERT INTO intelmessages (unit, classification, content, source) VALUES (%s, %s, %s, %s)"
    values = (unit, classification, content, source)
    cursor.execute(command, values)
    im_db.commit()
    cursor.close()
    im_db.close()
    return "messgae added"

def delete_message(id):
    im_db = get_connection()
    cursor = im_db.cursor()
    cursor.execute("DELETE FROM intelmessages WHERE id = %s" ,(id,))
    im_db.commit()
    deleted = cursor.rowcount > 0
    cursor.close()
    im_db.close()
    return deleted

def update_message(id, data):
    im_db = get_connection()
    cursor = im_db.cursor()
    query = "UPDATE intelmessages SET classification = %s, content = %s WHERE id = %s"
    values = (data["classification"],data["content"],id)
    cursor.execute(query, values)
    im_db.commit()
    changed = cursor.rowcount > 0
    cursor.close()
    im_db.close()
    return changed

def get_message(id):
    im_db = get_connection()
    cursor = im_db.cursor()
    cursor.execute("SELECT * FROM intelmessages WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    im_db.close()
    return row



