import sqlite3


class SaveGame:
    def __init__(self):
        self.conn = sqlite3.connect('save.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS save (max_level, max_health, cur_health, coins,id INTEGER PRIMARY KEY AUTOINCREMENT)''')
        # add name to creatr table if you want name
        self.conn.commit()

    def save(self, max_level, max_health, cur_health, coins,id):
        self.c.execute('''INSERT INTO save VALUES (?, ?, ?, ?,?)''', (max_level, max_health, cur_health, coins,id))# add name if you want user name and (?, ?, ?, ?,?,?)
        self.conn.commit()

    def load(self):
        self.c.execute('''SELECT * FROM save''')
        return self.c.fetchone()

    def close(self):
        self.conn.close()


