from Game import Game


class Application:

    def play_game(self, number_of_game_rounds):
         my_Game = Game(number_of_game_rounds)
         my_Game.start()

    def run(self):
        #Starting the game to run for 5 rounds
        self.play_game(5)
        

if __name__ == "__main__":
    app = Application()
    app.run()

