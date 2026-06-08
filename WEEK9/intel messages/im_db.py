import mysql.connector
 
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="secret",
        database="soldiers_db")

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
    cursor.execute("SELET * FROM intelmessages")
    rows = cursor.fetchall()
    cursor.close()
    im_db.close()
    return rows

def add_message(unit:str, classification:str, content:str, scource:str):
    im_db = get_connection()
    cursor = im_db.cursor()
    command = "INSERT INTO intelmessages (unit, classification, content, scource) VALUES (%s, %s, %s, %s)"
    values = (unit, classification, content, scource)
    cursor.execute(command, values)
    cursor.close()
    im_db.close()
    return "messgae added"

def delete_message(id):
    im_db = get_connection()
    cursor = im_db.cursor()
    cursor.execute("DELETE FROM intelmessages WHERE id  =%s" ,(id))
    cursor.close()
    im_db.close()
    return "messgae deleted"

def update_message(id, data):
    im_db = get_connection()
    cursor = im_db.cursor()
    cursor.execute("SELECT FROM intelmessages WHERE id  =%s" ,(id))
    cursor.close()
    im_db.close()
    return "messgae updated"

def message_by_id(id):
    im_db = get_connection()
    cursor = im_db.cursor()
    cursor.execute("SELECT * FROM soldiers WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    im_db.close()
    return row



