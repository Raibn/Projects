#########################################################
## written by : Brian Karani                           ##
## Contact : ~~                                        ##
## Email : brayokara@gmail.com                         ##
## Github : https://github.com/Raibn/Projects/madlibs  ##
#########################################################


## Madlibs

# Madlibs is a fun game to play with a friend
# so basically we ask for user inpurt as strings place em in a "story" or a paragraph that literaly makes no sense
# Modules used inthis program [random,sys,time,loading]
# Have fun


import random as rn
import sys
import time

try:
    prompt = input(str("Hey you ready to have fun ...? \n")).lower()

    accept = ["y","yes","yeah","si"]
    denial = ["n","naah","nope","no"]


    if prompt in accept:
        time.sleep(1.5)
        sys.stdout.write("\rWoW!! Am glad to hear that <3.")
    
        time.sleep(1.5)
        sys.stdout.write("\rlet\'s play a game it\'s called madlibs.\n")
        time.sleep(1.5)
        ##Promt then sleep for 2 seconds before asking any other feild

        #Celebrity name 
        sys.stdout.write("\rWho is your favourite celeb ?")
        celeb = input(str("\n#: "))
        time.sleep(1.5)

        #A noun 
        sys.stdout.write("\rGive me a random noun ..")
        noun = input(str("\n#:"))
        time.sleep(1.5)

        #A verb
        sys.stdout.write("\rGive me a random verb ..")
        verb = input(str("\n#:"))
        time.sleep(1.5)





        #Favourite place
        sys.stdout.write("\rGive me a random place ..")
        place = input(str("\n#:"))
        time.sleep(1.5)




        #Dream Car
        sys.stdout.write("\rWhat\'s your Dream Car ..?")
        car = input(str("\n#:"))
        time.sleep(1.5)




        #Favourite Meal
        sys.stdout.write("\rWhat\'s your favourite meal ..?")
        meal = input(str("\n#:"))
        time.sleep(1.5)




        #
        sys.stdout.write("\rGive me a random noun ..")
        noun = input(str("\n#:"))
        time.sleep(1.5)
        

        from loading import load
        load()
        time.sleep(10)
        load(True)

        #Final madlibs story
        print(f'Hey am {celeb} !!!')





    elif prompt in denial:

        print("\rSorry lonenly soul I bid you good luck and pregnancy ...!! \nBye !!!")
    else:
        sys.stdout.write("\rOooops!!! ")
        time.sleep(2)
        sys.stdout.write("\rWrong input answer !!!")
        time.sleep(3)
        sys.stdout.write("\rLets try again later ...\n")
        time.sleep(3)
        sys.stdout.write("\rByeeeeeee .....")
        time.sleep(1)
        sys.stdout.write("\rChaoooo ......")
        time.sleep(1)
        sys.stdout.write("\rAdios ........")
        time.sleep(1)
        sys.stdout.write("\r")

except KeyboardInterrupt:
    sys.stdout.write("\rOoops !! Bye Lad .... \
        ")