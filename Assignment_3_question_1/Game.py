from Player import Player
import random

class Game:
    Player_list = [Player("Muhammad"), Player("Mustafa"), Player("Ayesha")]
    def __init__(self, number_of_game_rounds):
        self.number_of_game_rounds = number_of_game_rounds
        self.guess = 0

    #Compares the guess with each player’s roll. If a player's roll matches the guess, their score is incremented.
    def match(self, player_dice_value, player_number):
        if self.guess == player_dice_value:
            self.Player_list[player_number].score += 1
            print(f'{self.Player_list[player_number].player_name} score is {self.Player_list[player_number].score}')


    
    def start(self):
            #Running the number of rounds for the game
            for i in range(self.number_of_game_rounds):
                #Generating the guess value for each round
                self.guess = random.randint(1, 6)
                print(f'Round {i + 1} has Guess value of: {self.guess}')
                #Rolling the dice for each player
                for player_number in range (len(self.Player_list)):
                    player_dice_value = self.Player_list[player_number].roll()
                    print(f'The dice value for {self.Player_list[player_number].player_name} is {player_dice_value}') 
                    #Calling the match method to compare if the Player dice value is the same as guess value
                    self.match(player_dice_value, player_number)
             #Printing the finalscore for each player 
            for player_number in range (len(self.Player_list)):
                print(f'{self.Player_list[player_number].player_name} final score is {self.Player_list[player_number].score}')
            #If Player 1 is the winner
            if  (self.Player_list[0].score >  self.Player_list[1].score) and  (self.Player_list[0].score >  self.Player_list[2].score):
                 print(f'{self.Player_list[0].player_name} with final score of {self.Player_list[0].score} is the winner')

            #If Player 2 is the winner
            if  (self.Player_list[1].score >  self.Player_list[0].score) and  (self.Player_list[1].score >  self.Player_list[2].score):
                 print(f'{self.Player_list[1].player_name} with final score of {self.Player_list[1].score} is the winner')

            #If Player 3 is the winner
            if  (self.Player_list[2].score >  self.Player_list[0].score) and  (self.Player_list[2].score >  self.Player_list[1].score):
                 print(f'{self.Player_list[2].player_name} with final score of {self.Player_list[2].score} is the winner')


            #If Player 1 and Player 2 have a tie
            if  (self.Player_list[0].score ==  self.Player_list[1].score) and  (self.Player_list[0].score >  self.Player_list[2].score):
                 print(f'{self.Player_list[0].player_name} and {self.Player_list[1].player_name} with final score of {self.Player_list[0].score} has a tie')

    
            #If Player 1 and Player 3 have a tie
            if  (self.Player_list[0].score ==  self.Player_list[2].score) and  (self.Player_list[0].score >  self.Player_list[1].score):
                 print(f'{self.Player_list[0].player_name} and {self.Player_list[2].player_name} with final score of {self.Player_list[2].score} has a tie')

            #If Player 2 and Player 3 have a tie
            if  (self.Player_list[1].score ==  self.Player_list[2].score) and  (self.Player_list[1].score >  self.Player_list[0].score):
                 print(f'{self.Player_list[1].player_name} and {self.Player_list[2].player_name} with final score of {self.Player_list[2].score} has a tie')


            #If Player 1 and Player 2 and Player 3 have a tie
            if  (self.Player_list[0].score ==  self.Player_list[1].score) and  (self.Player_list[0].score ==  self.Player_list[2].score):
                 print(f'{self.Player_list[0].player_name}, {self.Player_list[1].player_name} and {self.Player_list[2].player_name} with final score of {self.Player_list[2].score} has a tie')
