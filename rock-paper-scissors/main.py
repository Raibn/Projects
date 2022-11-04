## #################################################################
## written by : Brian Karani                                      ##
## Contact : ~~                                                   ##
## Email : brayokara@gmail.com                                    ##
## Github : https://github.com/Raibn/Projects/tree/main/rock-paper-scissors ##
## #################################################################


## Rock Paper scissors
# 


import random as rn
import sys 
import time



try:

    def play():
    
        print("Let\'s play Rock (R), Paper (P), Scissor (S) ...")
        print("Ready or not ....")
        sys.stdout.write("\rHere we go ... ")
        time.sleep(0.8)
        sys.stdout.write("\rRock (R) ......")
        time.sleep(0.8)
        sys.stdout.write("\rPaper (P) .....")
        time.sleep(0.8)
        sys.stdout.write("\rScissors (S) ..")
        time.sleep(1)
        ## User selection
        user = input("\rYour Pick ....?").lower()

        ## List of options
        # opt = ['r','rock' , 'p' ,'paper' , 's', 'scissors']
        op = ['r', 'p', 's']


        ## Computers choice
        comp = rn.choice(op)

        if comp == user :
            print('Its a Tie ...')



        if is_win(user,comp):
            print('Dzaaamn You won !!!')
            if comp == 's':
                print(f'I chose Scissors (S) ..')
            elif comp == 'r' :
                print(f'I chose Rock (R) ..')
            elif comp == 'p':
                print(f'I chose Paper (P) ..')

        if is_win(comp,user):
            print('Oopsie You Lost !!!')
            if comp == 's':
                print(f'I chose Scissors (S) ..')
            elif comp == 'r' :
                print(f'I chose Rock (R) ..')
            elif comp == 'p':
                print(f'I chose Paper (P) ..')

    def is_win(player,opp):
        ## This will return True if player wins.
        # 
        # paper beats rocks     # p > r
        # scissors beats paper  # s > p
        # rock beats scissors   # r > s
        if (player == 'p' and  opp == 'r' ) or (player == 's' and opp == 'p') \
            or (player == 'r' and opp == 's'):
            return True



        '''if (player == ('p' or 'paper') and  opp == ('r' or 'rock')) or (player == ('s'or'scissors') and opp == ('p' or 'paper')) \
            or (player == ('r'or'rock') and opp == ('s'or'scissors')):
            return True'''





    while True:
        play()

except KeyboardInterrupt:
    
    print('\nOooops Wrong Button ...')