from bs4 import BeautifulSoup as bs
import html5lib

## we import the file to write on 


## We import the html file to do a webscrape on 

with open("/Users/newuser/Home/Desktop/Projects/Randoms/webscrapes/htmls/Male-names.html","r",encoding='mac_roman') as ulr:
    soup = bs(ulr,features='html5lib')
    #print(soup) ## For the sake of Debugging

div = soup.find('div',{'class':'Rand-stage'})

#print(div) ## For the sake of debugging


ol = div.find_all('ol')
#print(ol)  ## For the sake of Debugging

for li in div.find_all('li'):
    tx = li.find('span',{'class':'rand_large'})
    print(tx.text.strip())
