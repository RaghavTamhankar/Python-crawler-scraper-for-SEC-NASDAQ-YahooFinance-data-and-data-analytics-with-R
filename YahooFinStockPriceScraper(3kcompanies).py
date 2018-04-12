#import urllib2 for python 2
import urllib3
import bs4 as bs
from bs4 import SoupStrainer
import codecs
import pandas as pd
companies = pd.read_csv("C:\\Users\\carlvader\\Downloads\\all companies v5.csv", encoding='latin1')
companies.head()
import time
# for python 2 run the following command
# from urllib2 import FancyURLopener
from urllib.request import FancyURLopener  # This is library that helps us create the headless browser
from random import choice #This library helps pick a random item from a list

user_agents = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
]

class MyOpener(FancyURLopener, object):
    version = choice(user_agents)

urls=[]
symbols=companies["Symbol"].tolist()
for i in symbols:
    urls.append('https://finance.yahoo.com/quote/' + i + '/history?period1=1353992400&period2=1511758800&interval=1mo&filter=history&frequency=1mo')       

import datetime
date=[]
closestock=[]
final=[]
dates=['Jan 01, 2015','Jan 01, 2016','Jan 01, 2017']

for i in urls:
    myopener = MyOpener()
    page=myopener.open(i)
    inthtml1 = page.read()
    html1=str(inthtml1)
    for j in dates:
        date.append(j)
        
        ## company name
        start=html1.find('<h1 class')
        if start!=-1:
            remaining=html1[start:]
            start=remaining.find('>')
            remaining2=remaining[start+1:]
            end=remaining2.find('</h1>')
            remaining3=remaining2[:end]
            final.append(remaining3)

            ## closing stock price
            start=html1.find(j)
            if start!=-1:
                remaining1=html1[start-15:]
                end=remaining1.find("</tr>")
                html2=remaining1[:end]
                html=bs.BeautifulSoup(html2, 'lxml')
                x=html.find_all('span')[4].getText()
                closestock.append(x)
            else:
                closestock.append('N/A')
            
        else:
            
            start=html1.find('Symbols similar to')
            remaining=html1[start+25:]
            end=remaining.find('</span>')
            remaining1=remaining[:end-6]
            final.append(remaining1)
            closestock.append('N/A')
          
