import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from model.database import Database

class BotController:
    def __init__(self):
        self.db = Database()

    def add_new_user(self, pseudo):
        self.db.add_user(pseudo)

    def add_new_challenge(self, name):
        self.db.add_challenge(name)

    def update_user_points(self, pseudo, points):
        self.db.update_points(pseudo, points)

    def solve_challenge(self, challenge_name, pseudo):
        self.db.solve_challenge(challenge_name, pseudo)

    def show_user_points(self, pseudo):
        points = self.db.get_user_points(pseudo)
        return points

    def show_solved_challenges(self, pseudo):
        challenges = self.db.get_solved_challenges(pseudo)
        return challenges

    def close(self):
        self.db.close()
