## ###################################################
## Name    :    Brian Karani                        ##
## Contact : ~                                      ##
## Email   : brayokara@gmail.com                    ##
## Github  : https://github.com/Raibn/rtic-tac-toe/ ##
## ###################################################


## Tic_Tac_Toe command line version 
## The Code the player

import math
import random as rn
import game



class player():
    def __init__(self,letter):
        # this will be the letter that the play is going tho play is going to represent
        # It's either an 'x' or 'o'
        # 'x' for cross and 'o' for knot 
        self.letter = letter
    # for the player to get their next move..
    def get_move(self,game):
        # Here we set a pass because this is the base player
        # because game can have two players
        pass

class CompPlayer(player):
    def __init__(self, letter):
         super().__init__(letter)

    def get_move(self, game):
        square = rn.choice(game.available_moves())

class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn.Input move (0-9): ')


            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid Square. Try Again.')






