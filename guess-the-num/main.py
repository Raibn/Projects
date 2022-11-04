##############################################################
## written by : Brian Karani                                ##
## Contact : ~                                              ##
## Email : brayokara@gmail.com                              ##
## Github : https://github.com/Raibn/Projects/tree/main/guess-the-num ##
##############################################################


## Guess the number (Computer) 
#
## Guess the Number (User)
#
import random as rn
import time



accept = ['y','yes','si','yap','yeah','ok']
cancel = ['n','no','naah','nope','nop']


try:         

    def guess(guess=0):
        try:

            print("Hey give me a range of numbers from \'a\' to \'b\' ")
            a = int(input("From: "))
            b = int(input("To: "))

            random_num = rn.randint(a,b)
            #guess = 0

            while guess != random_num:
                try:
                    guess = int(input(f"Guess a number between {a} and {b} : "))
                    print("\n")
                    if guess < random_num:
                        print("Sorry guess again. Too low \n")
                    elif guess > random_num:
                        print("Sorry. guess again. Too High \n")
                    else:
                        print(f"Whooohoo !!! You guessed {random_num} right ...")


                except ValueError:
                    print("Oooops wrong integer")


        except ValueError:
            print("Oooops wrong integer")


    def comp_guess(a=None,b=None,feedback=''.lower()):
        # a is low 
        # b is high
        try:

            print("Hey. Gime a range of numbers.")
            a = int(input("From: "))
            b =int(input("To: "))
        except ValueError:
            print("Ooops wrong Integer.")

        while feedback != 'c':
            if a != b:
                guess = rn.randint(a,b)
            else:
                guess = a or b
            feedback = input(f"Is {guess} Too High (H), Too loow(L), or Correct (C) ? ").lower()
            if feedback == 'h':
                b = guess-1
            elif feedback == 'l' :
                a = guess+1

        if feedback == 'c' :
            print(f"Whoohooo !! I guessed your number {guess}, correctly")


    def play(prompt=None,play=None):
        while prompt == None:
            print('Hey you !! Let\'s play a Number Guessing game .')
            try:
                prompt = input().lower()

                if prompt in accept :
                    while play == None:
                        play = input("Would you mind, if I started ?").lower()
                        time.sleep(1.5)
                        if play in cancel:
                            print("Thank you.I\'ll be sure to make this fun ..")
                            time.sleep(1.5)
                            comp_guess()
                        elif play in accept:
                            print("Very well then. Go ahead.")
                            time.sleep(1.5)
                            return guess()
                        else:
                            print("Sorry I didn\'t get that. Lest\'s try again")
                elif prompt in cancel:
                    print("Thats ok. but am here if you wanna play a number guessing Game ...")
                    return exit()
                else:
                    print("Sorry.I din\'t get that ..")
                pass
            except ValueError:
                print("Oooooooop!!!!!  TypeError\n")
            except ValueError:
                print("BOOOOOOOO !!!! ValueError\n")


    while True:
        play()
except KeyboardInterrupt:
    
    print('\nOoopsiee Wrong Button. Bye Though .')