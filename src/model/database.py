import mariadb
import configparser

class Database:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.conn = mariadb.connect(
            user=config['database']['user'],
            password=config['database']['password'],
            host=config['database']['host'],
            database=config['database']['database']
        )
        self.cursor = self.conn.cursor()

    def add_user(self, pseudo, points=0):
        self.cursor.execute("INSERT INTO users (pseudo, points) VALUES (?, ?)", (pseudo, points))
        self.conn.commit()

    def add_challenge(self, name):
        self.cursor.execute("INSERT INTO challenges (name) VALUES (?)", (name,))
        self.conn.commit()

    def update_points(self, pseudo, points):
        self.cursor.execute("UPDATE users SET points = ? WHERE pseudo = ?", (points, pseudo))
        self.conn.commit()

    def solve_challenge(self, challenge_name, pseudo):
        self.cursor.execute("UPDATE challenges SET solved_by = ? WHERE name = ?", (pseudo, challenge_name))
        self.conn.commit()

    def get_user_points(self, pseudo):
        self.cursor.execute("SELECT points FROM users WHERE pseudo = ?", (pseudo,))
        return self.cursor.fetchone()[0]

    def get_solved_challenges(self, pseudo):
        self.cursor.execute("SELECT name FROM challenges WHERE solved_by = ?", (pseudo,))
        return [row[0] for row in self.cursor.fetchall()]

    def close(self):
        self.cursor.close()
        self.conn.close()
