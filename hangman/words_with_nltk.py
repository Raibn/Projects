## ############################################
## written by : Brian Karani                 ##
## Contact : ~~                              ##
## Email : brayokara@gmail.com               ##
## Github : https://github.com/Raibn/hangman ##
## ############################################

## Resulted to an Error = 'Attempted to load tokenizers/punkt/PY3/english.pickle'
# >>> nltk.download('punkt)

import nltk


with open('/Users/newuser/Home/Desktop/Projects/Randoms/texts/words_webscrape.txt','r') as w:
    wlist = w.read()
with open('/Users/newuser/Home/Desktop/Projects/Randoms/texts/males_webscrape.txt','r') as m:
    mlist = m.read()
with open('/Users/newuser/Home/Desktop/Projects/Randoms/texts/females_webscrape.txt','r') as f:
    flist = f.read()





words_list = [ ] 
male_names = [ ]
female_names= [ ]



words_list = nltk.word_tokenize(wlist)


print(words_list)


