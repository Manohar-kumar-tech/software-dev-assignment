import sqlite3

class DBHandler():
    def __init__(self, db_name= "Library.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.createTable()
        
    def createTable(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS books(
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    is_available INTEGER DEFAULT 1
                )                              
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    user_id TEXT NOT NULL                    
                )                              
            """)
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS borrowed_books(
                    user_id TEXT,
                    book_id INTEGER,
                    FOREIGN KEY (user_id) REFERENCES users(user_id),
                    FOREIGN KEY (book_id) REFERENCES books(id)
                    
                )                              
            """)
            
    
    def executeQuery(self, query, params=None):
        with self.conn:
            if params:
                self.conn.execute(query, params)
            else:
                self.conn.execute(query)
    
    def fetch_query(self, query, params=None):
        cursor = self.conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()
    
    def fetchAll(self, query):
        with self.conn:
            return self.conn.execute(query).fetchall()
        
    def fetchOne(self, query, params=None):
        with self.conn:
            return self.conn.execute(query, params).fetchone()