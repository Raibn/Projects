## ############################################
## written by : Brian Karani                 ##
## Contact : ~                               ##
## Email : brayokara@gmail.com               ##
## Github : https://github.com/Raibn/hangman ##
## ############################################

## Hangman Game

import random as rn
import string
import time
from words import male_names_list as mnlist , words_list as wlist , female_names_list as fnlist


## Just incase you forget ...

# mnlist === male_names_list
# fnlist === male_names_list
# wlist === words_list
try:
    def get_a_word():
        # Randomly chooses a word from the wlist 
        word = rn.choice(wlist).upper()
        #print(word)  ## For the sake of debugging.
        # To avoid geting a wrd with an '-' or a space  >>> 
        while '-' in word or ' ' in word:
            word = rn.choice(wlist).upper()
        return word

    def get_a_boys_name():
        # Randomly chooses boys name from mnlist
        boys_name = rn.choice(mnlist).upper()
        #print(boys_name)  ## For the sake of Debugging.
        return boys_name

    def get_a_girls_name():
        # Randomly selects a girls name from fnlist
        girls_name = rn.choice(fnlist).upper()
        #print(girls_name)   ## For the sake of Debbuging
        return girls_name

## This part still on progress
##     def choose_list(chosen):
##     
##             # prompts the player to choose a list
## 
##         return chosen

    def hangman():
        
        while True:
            word = get_a_word()
            boys_name = get_a_boys_name()
            girls_name = get_a_girls_name()
            # Letters in the word 
            word_letter = set(word)
            alphabets = set(string.ascii_uppercase)
            # what the usser has already guessed
            used_letters = set()


            ## The concept of live // tries 
            life = 10


            while len(word_letter) > 0 and life > 0 :
                
                ## getting User input ...
                user_letters = input("Guess a letter : ").upper()
                #time.sleep(1.5)
                ## Letters used 
                # ''.join(['a','b','cd']) ----> 'a b cd'


                if user_letters in alphabets - used_letters:
                    used_letters.add(user_letters)
                    if user_letters in word_letter:
                        word_letter.remove(user_letters)
                    else:
                        ## print('Current word: ' , ' '.join(word_list))
                        life -= 1

                        ## print('You lost a life..')
                        ## time.sleep(1.5)
                elif user_letters in used_letters :
                    print("You Already Guessed that letter .Please try Again .")
                    ## here we subract lifes if the user already guesed the letter twice 
                    ## print(f"You have {life} lives left  ")
                    life -= 1

                else:
                    print("invalid character. Please Try Again.")
                    ## we also remove alife if the user inputs an Invali Character.
                    ## print(f"You have {life} lives left  ")
                    life -= 1

                ## we need to tell the user Current word is ie (W - -)
                word_list = [letter if letter in used_letters else "_" for letter in word]
                print(f'You have {life} lifes. \nYou Have used these letters: ' , ' '.join(used_letters))
                print('Current word: ' , ' '.join(word_list))



            
            
            ## Gets here when len(word_letter) == 0
            if life == 0 :
                print(f'\n\nOoopsie you died the word was {word}. ')
                exit()
            else: 
                print(f'Yaay !! you guessed the word {word } ')
                time.sleep(1.5)
                


        #print("Hiiii")
    hangman()

except KeyboardInterrupt:
    print('\nOooooopsiee wrong button !!!\nBye Though ...')
    
    exit()