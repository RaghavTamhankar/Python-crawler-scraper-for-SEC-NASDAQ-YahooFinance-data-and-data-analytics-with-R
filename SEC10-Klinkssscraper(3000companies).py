pwd
import os
os.chdir("C:\\Users\\WEILUN\\desktop\\course\\2017FALL\\Web Data Analytics\\Group Projects")

import pandas as pd
import urllib2
import bs4 as bs
from bs4 import SoupStrainer

weblink = []
weblink1 = []
filing_type = []
company_name = []
ticker=[]
date = [] 
df = pd.read_csv('all companies.csv')   #companies list collated from the internet

Symbol=list(df['Symbol'])
Name=list(df['Name'])

from urllib import FancyURLopener  # This is library that helps us create the headless browser
from random import choice #This library helps pick a random item from a list
user_agents = [
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
]
link=[]
for item in range(0,len(Symbol)):
        link ='https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=' + Symbol[item] + '&type=10-K&dateb=&owner=exclude&count=40'
        class MyOpener(FancyURLopener, object):
                version = choice(user_agents)
        
        myopener = MyOpener()
        page=myopener.open(link)
        
        html = page.read()
        soup =bs.BeautifulSoup(html,"lxml")
        infotable = soup.find_all("table",class_ = "tableFile2")
        if html.find('nowrap') != -1:
            if infotable != []:
                rows = infotable[0].find_all('tr')
                for i in rows[1:]:
                    columns = i.find_all('td')
                    filing_type.append(columns[0].getText())
                    templink=columns[1].find("a",href=True)
                    weblink.append("https://www.sec.gov"+templink['href'])
                    date.append(columns[3].getText())
                    ticker.append(Symbol[item])
                    company_name.append(Name[item])
        elif infotable==[]:
            continue

for y in weblink:
            myopener2 = MyOpener()
            page1=myopener2.open(y)
            html3 = page1.read()
            soup2 =bs.BeautifulSoup(html3,"lxml")
            infotable1 = soup2.find_all("table",class_ = "tableFile")
            rows1 = infotable1[0].find_all('tr')
        
            for i in rows1[1:2]:
                columns1 = i.find_all('td')                             
                templink1=columns1[2].find("a",href=True)
                weblink1.append("https://www.sec.gov"+templink1['href'])
                                     

sum_list=[]
sum_list.append(['Symbol','Company Name','Date of Filing','Filing Type','Link of Document'])
for i in range(0,len(weblink1)):
    if filing_type[i]!="10-K":
        continue
    if date[i]<'2013-01-01':
        continue
    sum_list.append([ticker[i],company_name[i],date[i],filing_type[i],weblink1[i]])
import csv
with open('C:\\Users\\WEILUN\\desktop\\course\\2017FALL\\Web Data Analytics\\Group Projects\\10K links(soup).csv','wb') as f:
    writer=csv.writer(f)
    writer.writerows(sum_list)
