## ###########################################################
## Name    :    Brian Karani                                ##
## Contact : ~                                              ##
## Email   : brayokara@gmail.com                            ##
## Github  : https://github.com/Raibn/Projects/tic-tac-toe/ ##
## ###########################################################


## Tic_Tac_Toe command line version 
## The Code the player

import math
import random as rn
from warnings import catch_warnings



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
        self.valid_square = True
        try:
            square = rn.choice(game.available_moves())
        except IndexError:
            print('It\'s a Tie ...')
            game.print_board()
            exit()            
        return square 
class HumanPlayer(player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        self.valid_square = False
        val = None
        while not self.valid_square :
            square = input(self.letter + '\'s turn.Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                self.valid_square = True 
            except ValueError:
                print('Invalid Square. Try Again.')
        return val
class HumanOp(player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        self.valid_square = False
        val = None
        while not self.valid_square:
            square = input(self.letter + '\'s turn.Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError                    
                self.valid_square = True 
            except ValueError:
                print('Invalid Square. Try Again.')
        return val

class bot(player):
    def __init__(self, letter):
        super().__init__(letter)  
              
    def minimax(self, state, player):
        
        max_player = self.letter
        if player == 'O':
            other_player = 'X'
        elif player == 'X':
            other_player =  'O'
        ## First we check if previous move was winner ..
        ## This gon be our base case i.e At the end of things where are we at ...
        if state.current_winner == other_player:
            ## we should return position and score because we need to keep track of the score for minimax to work ...
            return {
                'position' : None,
                'score' : 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (state.num_empty_squares() + 1)
            }
        elif not state.num_empty_squares():  ## If there's no empty squares 
            return {
                'position' : None,
                'score' : 0
            }
        if player == max_player:
            ## we gon initialize a variable (dict) thats going to save the best position to move 
            best = {'position' : None, 'score' : -math.inf}  ## Each score should maximamize (Be larger)
        elif player == other_player:
            best = {'position' : None, 'score' : -math.inf}  ## Each score should minimize (Be Smaller)
        for posible_move in state.available_moves():
            #posible_move = int(i)
            ## Step 1 : Make that move 
            state.make_move(posible_move, player) 
            ## Step 2 : Recurse using minimax to simulate a game after making the move 
            ##        ;o see what happens from there on after making that move ...
            simulate_score = {'position' : None, 'score' : -math.inf}
            simulate_score = self.minimax(state, other_player)
            ## Step 3 : Unodo that move so we can try the next move
            #try:
            state.board[posible_move] = ' '
            state.current_winner = None
            #try:
            simulate_score['position'] = posible_move 
            #except TypeError:
                #continue
            ## Step 4 : Update the dictionarry if nessesary 
            if player == max_player:
                #print(simulate_score)
                if simulate_score['score'] > best['score']:
                    best = simulate_score
            elif player == other_player:
                if simulate_score['score'] < best['score']:
                    best = simulate_score

        #print('This is best ....')
        #print(best['position'])
        if (best['position'] != None) or (best['position'] == (i for i in state.available_moves())):
            return best
        else:
            print('Sim .......')
            #return self.minimax(state,player)
            rn.choice(state.available_moves())
        
            
            
        #self.minimax(state,max_player)

    def get_move(self, game):
        ## This was default ... -->return super().get_move(game)
        if len(game.available_moves()) == 8:
            square = rn.choice(game.available_moves()) # Randomly choose a space to start the game 
        else: 
            ## Get the square using the minimax Algorithm 
            square = self.minimax(game, self.letter)['position']
            
            if square == None:
                print('Still None !!!')
            
                square = self.minimax(game, self.letter)['position']
        return square




#tic = TicTacToe()
#x_player = bot('X')
#o_player = human('O')
#play(tic,x_player,o_player)