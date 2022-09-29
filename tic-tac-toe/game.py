## ###################################################
## Name    : Brian Karani                           ##
## Contact : ~                                      ##
## Email   : brayokara@gmail.com                    ##
## Github  : https://github.com/Raibn/rtic-tac-toe/ ##
## ################################################### 


## Tic_Tac_Toe command line version 
## The Code the Game it self 
#  The game can be played with two players. It (computer vs computer) , (player vs player) or (player vs computer)



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
        num_board = [[str() for i in range(j*3, (j+1)*3)]\
                            for j in range(3)]
        
        for row in num_board:
            print('| '+' | '.join(row) + ' |')
    
    def available_moves(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ']

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
        return len(self.available_moves())

    def make_move(self, square, letter):
        # if valid_move,then make the move (assign square to letter)
        # then return true, if invalid return false 

        if self.board[square] == ' ' :
            self.board[square] == letter
            return True
        return False



def play(game,x_player ,o_player ,print_game=True):
    if print_game:
        game.print_board_nums()
        
    letter = 'X' #starting letter
    # iterate the game still has empty squares 
    # (we don't have to worry about winner coz we'll return that \
    # which breaks the loop ) #

    while game.empty_squares():
        # Getting move from the right player 
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        
        # Letsdefine a function to make a move 
        

        if game.make_move(square,  letter):
            if print_game:
                print(letter + ' makes a move to square')
        






