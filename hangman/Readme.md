# Hiiiii


## ############################################
## written by : Brian Karani                 ##
## Contact : ~                               ##
## Email : brayokara@gmail.com               ##
## Github : https://github.com/Raibn/hangman ##
## ############################################

## Hangman Game

## About
Similarly to the Real Hangman Game the user ('Player') , Guesses letters in a word or a name genereted randomly from a list of names and words.
I also included the concept of life(s) in the game. Initially the player has 10 life(s) but the following conditions define how he looses a life :
    a)If the player Guesses a letter not present in the word/name,
    b)If the player enters a previously entered letter,
    c)Finally , If a user enters a string

(I'm still working on this hangman game.I'm not satisfied with the efficiency of the game. I don't mind any suggestions to improve the code )

## Functions in the code

# get_a_word()
This function calls a random word from words_list, a list of words from the imported file > words.py
It can also get'em from > words_with_nltk.py but this one is kinda uncomplete so I used the lists from words.py


# get_a_girls_name()
Calls a random girls name similar to get_a_word().


# get_a_boys_name()
Calls a random boys name similar to get_a_girls_name()


# hangman()
Calls the game.


## Note !!
You can also add a word validator While geting word or name ie  without spaces or - .
You can add the following lines in the the functions calling the name/word :
    > while ' ' in word or '-' in word : #can be word/name
    >   word = rando.choice(words)       #randomly chooses another name/word




## Have Fun !!!
