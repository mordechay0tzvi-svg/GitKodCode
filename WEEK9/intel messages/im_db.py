import mysql.connector
 
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        port=8000,
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
    cursor = im_db.cursor()
    cursor.execute("DESCRIBE intelmessages")
    rows = cursor.fetchall()
    cursor.close()
    im_db.close()
    return [msg for msg in rows]
