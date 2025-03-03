import random

class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.score = 0


    def roll(self):
        return random.randint(1,6)
        