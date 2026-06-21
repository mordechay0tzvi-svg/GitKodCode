import mysql.connector
from logging import Logger


class IntelMessagesDAL:
    VALID_CLASSIFICATIONS = ('unclassified', 'confidential', 'secret','top_secret')
    def __init__(self, host: str, user: str, port:int, password: str, database: str, logger: Logger|None=None):
        self.host = host
        self.user = user
        self.port = port
        self.password  = password
        self.database = database
        self.logger = logger

    def get_conn(self):
        connection = mysql.connector.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
        return connection

    def setup(self) -> None:
        conn = self.get_conn()
        cursor = conn.cursor()
        create_new_table = """CREATE TABLE IF NOT EXISTS intelmessages (
                            id INT PRIMARY KEY AUTO_INCREMENT,
                            unit VARCHAR(100) NOT NULL,
                            classification ENUM('unclassified','confidential','secret','top_secret'),
                            content TEXT NOT NULL,
                            source VARCHAR(100),
                            created_at DATETIME DEFAULT NOW())"""
        cursor.execute(create_new_table)
        conn.commit()
        cursor.close()
        conn.close()

    def get_schema(self) -> list[dict]:
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute("DESCRIBE intelmessages")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return [{"column": row[0], "type": row[1]} for row in rows]

    def get_all(self) -> list[dict]:
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM intelmessages")
        all = cursor.fetchall()
        cursor.close()
        conn.close()
        return all

    def get_by_id(self, message_id: int) -> dict | None:
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM intelmessages WHERE id = %s", (message_id,))
        message = cursor.fetchone()
        cursor.close()
        conn.close()
        return message
    
    def create(self, unit: str, classification: str, content: str, source: str | None) -> int:
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        command = "INSERT INTO intelmessages (unit, classification, content, source) VALUES (%s, %s, %s, %s)"
        values = (unit, classification, content, source)
        cursor.execute(command, values)
        message_id = cursor.lastrowid
        conn.commit()
        cursor.close()
        conn.close()
        return message_id

    def update(self, message_id: int, data: dict) -> bool:
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        query = "UPDATE intelmessages SET classification = %s, content = %s WHERE id = %s"
        values = (data["classification"],data["content"],message_id)
        cursor.execute(query, values)
        conn.commit()
        updated:True|False  = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return updated
    
    def delete(self, message_id: int) -> bool:
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("DELETE FROM intelmessages WHERE id = %s" ,(message_id,))
        conn.commit()
        deleted:True|False = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return deleted

    def get_by_unit(self, unit: str) -> list[dict]:
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM intelmessages WHERE unit = %s" ,(unit,))
        from_unit = cursor.fetchall()
        cursor.close()
        conn.close()
        return from_unit
    
    def get_by_classification(self, classification: str) -> list[dict]:
        if classification not in IntelMessagesDAL.VALID_CLASSIFICATIONS:
            return
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM intelmessages WHERE classification = %s" ,(classification,))
        in_classification = cursor.fetchall()
        cursor.close()
        conn.close()
        return in_classification

    def get_by_unit_and_classification(self, unit: str, classification: str) -> list[dict]:
        if classification not in IntelMessagesDAL.VALID_CLASSIFICATIONS:
            return
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM intelmessages WHERE classification = %s AND unit = %s" ,(classification, unit))
        unit_classification = cursor.fetchall()
        cursor.close()
        conn.close()
        return unit_classification

    def get_distinct_units(self) -> list[str]:
        conn = self.get_conn()
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT unit FROM intelmessages")
        units = cursor.fetchall()
        cursor.close()
        conn.close()
        return [unit[0] for unit in units]

    def search_content(self, term: str) -> list[dict]:
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM intelmessages WHERE content LIKE %s", (f"%{term}%",))
        contains_term = cursor.fetchall()
        cursor.close()
        conn.close()
        return contains_term
    
    def get_missing_source(self) -> list[dict]:
        conn = self.get_conn()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM intelmessages WHERE source IS NULL")
        no_source = cursor.fetchall()
        cursor.close()
        conn.close()
        return no_source    
