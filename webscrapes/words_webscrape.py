from distutils.file_util import write_file
from fileinput import close
from bs4 import BeautifulSoup as bs
import html5lib

## we import the file to write on 


## We import the html file to do a webscrape on 

with open("/Users/newuser/Home/Desktop/Projects/Randoms/webscrapes/htmls/random-words.html","r",encoding='mac_roman') as ulr:
    soup = bs(ulr,features='html5lib')
    #print(soup) ## For the sake of Debugging

div = soup.find('div',{'class':'Rand-stage'})

#print(div) ## For the sake of debugging


ol = div.find_all('ol')
#print(ol)  ## For the sake of Debugging

for li in div.find_all('li'):
    tx = li.find('span',{'class':'rand_large'})
    '''with open('Users/newuser/Home/Desktop/Projects/Randoms/webscrapes/words_webscrape.txt','r+') as words:
        words.append(tx)'''
    #dy = []
    #dy.append(tx.text.strip())
    
    #'''
    print(tx.text.strip())
    

#write_file('/Users/newuser/Home/Desktop/Projects/Randoms/webscrapes/words_webscrape.txt',tx.text.strip())
