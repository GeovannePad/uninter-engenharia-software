import sqlite3

class DBProxy:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            '''
                CREATE TABLE IF NOT EXISTS dados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    name TEXT NOT NULL, 
                    score INTEGER NOT NULL, 
                    date TEXT NOT NULL
                );
            '''
        )

    #def execute_query(self, query, score_dict):
        #self.conn.cursor().execute(query, score_dict)

    def save(self, score_dict):
        self.cursor.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date);', score_dict)
        self.conn.commit()

    def retrive_top10(self):
        return self.cursor.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        return self.conn.close()