import sqlite3

class DataBase:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS books (name TEXT, author TEXT)"
        )
        self.conn.commit()

    
    def fetch(self):
        self.c.execute("SELECT rowid, * FROM books")
        rows = self.c.fetchall()
        return rows

    
    def insert(self, name, author):
        self.c.execute("INSERT INTO books VALUES (?, ?)", (name, author))
        self.conn.commit()


    def remove(self, id):
        self.c.execute("DELETE FROM books WHERE rowid = :id", {'id': id})
        self.conn.commit()


    def update(self, id, name, author):
        self.c.execute("UPDATE books SET name = ?, author = ? WHERE rowid = ? ", (name, author, id))
        self.conn.commit()

    
    def __del__(self):
        self.conn.close()



# db = DataBase('shelf.db')
# db.insert('minset', 'Dr.Carol S. Dweck')
# db.insert('Obsidian Leviathan', 'Pongpop Sukanunta')
