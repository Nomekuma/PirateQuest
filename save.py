import sqlite3


class SaveGame:
    def __init__(self):
        self.conn = sqlite3.connect('save.db')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS save (max_level, max_health, cur_health, coins)''')
        self.conn.commit()

    def save(self, max_level, max_health, cur_health, coins):
        self.c.execute('''INSERT INTO save VALUES (?, ?, ?, ?)''', (max_level, max_health, cur_health, coins))
        self.conn.commit()

    def load(self):
        self.c.execute('''SELECT * FROM save''')
        return self.c.fetchone()

    def close(self):
        self.conn.close()
