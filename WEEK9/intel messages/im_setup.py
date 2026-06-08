import mysql.connector
im_db =  mysql.connector.connect(host="localhost",
                                 port=3306,
                                 user='root',
                                 password='secret',
                                 database="soldiers_db")

cursor = im_db.cursor()
create_new_table = """
CREATE TABLE IF NOT EXISTS intelmessages (
    id INT PRIMARY KEY AUTO_INCREMENT,
    unit VARCHAR(100) NOT NULL,
    classification ENUM('unclassified','confidential','secret','top_secret'),
    content TEXT NOT NULL,
    source VARCHAR(100),
    created_at DATETIME DEFAULT NOW())
"""
cursor.execute(create_new_table)
im_db.commit()
print("Table created successfully")
cursor.close()
im_db.close()
