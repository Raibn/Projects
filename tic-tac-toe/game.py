## ###########################################################
## Name    : Brian Karani                                   ##
## Contact : ~                                              ##
## Email   : brayokara@gmail.com                            ##
## Github  : https://github.com/Raibn/Projects/tic-tac-toe/ ##
## ###########################################################


## Tic_Tac_Toe command line version 
## The Code the Game it self 
#  The game can be played with two players. It (computer vs computer) , (player vs player) or (player vs computer)

import math
import time
from player import CompPlayer as comp 
from player import HumanPlayer as human 
from player import HumanOp as player_1
from player import bot

try:
    class TicTacToe():
        def __init__(self):
            self.board = [' ' for _ in range(9)] # This list is going to represent a 3x3 board of the Game.
            self.current_winner = None # This variable keeps track of the winner

        def print_board(self):
            for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
                print('| '+' | '.join(row) + ' |')

        @staticmethod
        def print_board_nums():
            # Tell player what nums correspond to what box ie # > 0 | 1 | 2
            num_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]

            for row in num_board:
                print('| '+' | '.join(row) + ' |')
            #return num_board

        def available_moves(self):
            return [i for (i,spot) in enumerate(self.board) if spot == ' ']

            # move = []
            # for (i, spot) in enumerate(self.board):
            #     # ['x','x','o']  --> . [(0,'x'), (1,'x'), (2,'o')]
            #     if spot == ' ':
            #         move.append(i)
            # 
            # return move
        def empty_squares(self):
            return ' ' in self.board

        def num_empty_squares(self):
            # return len(self.available_moves())
            return self.board.count(' ')

        def make_move(self, square, letter):
            # if valid_move,then make the move (assign square to letter)
            # then return true, if invalid return false 
            try:
                if self.board[square] == ' ' :
                    self.board[square] = letter
                    if self.winner(square , letter): 
                        self.current_winner = letter
                    return True
                return False
            except TypeError:
                return True
            ##     pass


        def winner(self, square ,letter):
            # winner present if threee in a row anywhere ..
            # we have to check all directions 

            #first we check the rows
            row_ind = square // 3
            row = self.board[row_ind*3: (row_ind + 1) * 3]
            if all([spot == letter for spot in row]):
                return True

            # checking columns
            col_ind = square % 3
            column = [self.board[col_ind + i * 3] for i in range(3)]
            if all([spot == letter for spot in column]):
                return True

            # to Check for diagonals
            # because all squares are in even number 0,2,4,6,8
            # Those are the only possible moves diagonally to win
            if square % 2 == 0:
                diagonal1 = [self.board[i] for i in [0, 4, 8 ]]
                if all([spot == letter for spot in diagonal1]):
                    return True

                diagonal2 = [self.board[i] for i in [2, 4, 6]]
                if all([spot == letter for spot in diagonal2]):
                    return True

            # If all of fail
            # if TicTacToe.available_moves() == None:
            #     return False



            return False



    def play(game,x_player ,o_player ,print_game=True):
        # returns the winner of the game (or a letter) or a tie if none
        if print_game:
            game.print_board_nums()

        letter = 'X' #starting letter
        # iterate the game still has empty squares 
        # (we don't have to worry about winner coz we'll return that \
        # which breaks the loop ) #'o

        if letter == 'X':
            square = x_player.get_move(game)
            
        else:
            square = o_player.get_move(game)
            

        while game.empty_squares():
            # Getting move from the right player 
            
            # Letsdefine a function to make a move 


            if game.make_move(square,letter):
                if print_game:
                    print(letter + f' makes a move to square {square}')
                    game.print_board()
                    print('') # prints an empty line

                # After we've made our move we need the program to alternate letters
                # so we gonna assign a letter == 'o'

                if game.current_winner:
                    if print_game:
                        print(letter + ' wins!!')
                        game.print_board()
                        return letter

                # letter = 'X' if letter == 'O' else letter='O' # switches player
                if letter == 'O':
                    letter = 'X'
                    square = x_player.get_move(game)
                    
                    
                elif letter == 'X':
                    letter = 'O'
                    square = o_player.get_move(game)


                # if letter == 'O':
                #     square = o_player.get_move(game)
                # else:
                #     square = x_player.get_move(game)
            time.sleep(1)
        # if game.available_moves() == None:
        #     print('It\'s a tie ..')
        #     game.print_board()
        #     exit()
            
            # if print_game:
            #     print('It\' a tie')
            #     game.print_board()
    

except KeyboardInterrupt:
    print('\nOooooopsiee wrong button !!!\nBye Though ...')
    
    # exit()



if __name__ == '__main__':
    tic = TicTacToe()
    x_player = comp('X')
    o_player = human('O')
    play(tic,x_player,o_player)

#print(tic.print_board_nums())