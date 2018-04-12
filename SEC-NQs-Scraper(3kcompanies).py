import pandas as pd
import urllib3
import bs4 as bs
from bs4 import SoupStrainer
import codecs
import pandas as pd


import time
# for python 2 run the following command
#from urllib import FancyURLopener
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


import os
os.chdir('MF')


health1=pd.read_excel("Mutual fund lists.xlsx",sheetname='Finance')
health=health1.drop(health1.index[0])

urls=[]
for i in health['Ticker'].tolist():
    urls.append('https://www.sec.gov/cgi-bin/series?ticker='+i+'&CIK=&sc=companyseries&type=N-PX&Find=Search') 
    
    
CIK=[]
for i in urls: 
    myopener = MyOpener()
    page=myopener.open(i)
    html=bs.BeautifulSoup(page,'lxml')
    ciks=html.find_all('a',href=True)[5].getText()
    if "0" in ciks:
        CIK.append(ciks)
    else:
        CIK.append("NA")
        
NQpage=[]
for i in CIK:
    if 'NA' not in i:
        link='https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK='+i+'&type=N-Q&dateb=&count=40&scd=filings'
    else:
        link='NA'
    NQpage.append(link)
    
    
link17=[]
link16=[]
link15=[]
link14=[]
for i in NQpage:
    if 'NA' not in i:
        myopener = MyOpener()
        page=myopener.open(i)
        inthtml=page.read()
        html=bs.BeautifulSoup(inthtml,'lxml')
        href=html.find_all('a',href=True)[14]
        if href!=-1:
            x=str(href)
            start=x.find('<a')
            end=x.find('</a')
            remaining=x[start+9:end-33]
            link17.append('https://www.sec.gov'+ remaining)
        else:
            link17.append('NA')
        
        html1=str(inthtml)
        
        start=html1.find('2016-')
        if start!=-1:
            remaining1=html1[start-650:start]
            remaining=bs.BeautifulSoup(remaining1,'lxml')
            href=remaining.find_all('a',href=True)[1]
            x=str(href)
            start=x.find('<a')
            end=x.find('</a')
            remaining=x[start+9:end-33]
            link16.append('https://www.sec.gov'+ remaining)
        else:
            link16.append('NA')
        
        start=html1.find('2015-')
        if start!=-1:
            remaining1=html1[start-650:start]
            remaining=bs.BeautifulSoup(remaining1,'lxml')
            href=remaining.find_all('a',href=True)[1]
            x=str(href)
            start=x.find('<a')
            end=x.find('</a')
            remaining=x[start+9:end-33]
            link15.append('https://www.sec.gov'+ remaining)
        else:
            link15.append('NA')
        
        start=html1.find('2014-')
        if start!=-1:
            remaining1=html1[start-700:start]
            remaining=bs.BeautifulSoup(remaining1,'lxml')
            href=remaining.find_all('a',href=True)[1]
            x=str(href)
            start=x.find('<a')
            end=x.find('</a')
            remaining=x[start+9:end-33]
            link14.append('https://www.sec.gov'+ remaining)
        else:
            link14.append('NA')
        
    else:
        link17.append('NA')
        link16.append('NA')
        link15.append('NA')
        link14.append('NA')

NQ14file=[]
NQ15file=[]
NQ16file=[]
NQ17file=[]
for i in link14:
    if 'NA' not in i:
        myopener = MyOpener()
        page=myopener.open(i)
        inthtml=page.read()
        html=bs.BeautifulSoup(inthtml,'lxml')
        href=html.find_all('a',href=True)[8]
        if href!=-1:
            x=str(href)
            start=x.find('<a')
            end=x.find('htm')
            remaining=x[start+9:end+3]
            NQ14file.append('https://www.sec.gov'+ remaining)
        else:
            NQ14file.append('NA')
    else:
        NQ14file.append('NA')
        
for i in link15:
    if 'NA' not in i:
        myopener = MyOpener()
        page=myopener.open(i)
        inthtml=page.read()
        html=bs.BeautifulSoup(inthtml,'lxml')
        href=html.find_all('a',href=True)[8]
        if href!=-1:
            x=str(href)
            start=x.find('<a')
            end=x.find('htm')
            remaining=x[start+9:end+3]
            NQ15file.append('https://www.sec.gov'+ remaining)
        else:
            NQ15file.append('NA')
    else:
        NQ15file.append('NA')
        
for i in link16:
    if 'NA' not in i:
        myopener = MyOpener()
        page=myopener.open(i)
        inthtml=page.read()
        html=bs.BeautifulSoup(inthtml,'lxml')
        href=html.find_all('a',href=True)[8]
        if href!=-1:
            x=str(href)
            start=x.find('<a')
            end=x.find('htm')
            remaining=x[start+9:end+3]
            NQ16file.append('https://www.sec.gov'+ remaining)
        else:
            NQ16file.append('NA')
    else:
        NQ16file.append('NA')
        
for i in link17:
    if 'NA' not in i:
        myopener = MyOpener()
        page=myopener.open(i)
        inthtml=page.read()
        html=bs.BeautifulSoup(inthtml,'lxml')
        href=html.find_all('a',href=True)[8]
        if href!=-1:
            x=str(href)
            start=x.find('<a')
            end=x.find('htm')
            remaining=x[start+9:end+3]
            NQ17file.append('https://www.sec.gov'+ remaining)
        else:
            NQ17file.append('NA')
    else:
        NQ17file.append('NA')

temp = []

for j in NQ17file:
    mylist = []
    myNewlist = []
    myThirdlist=[]    
    d = []
    
    if 'NA' not in j:
        myopener = MyOpener()
        page=myopener.open(j)
        inthtml1=page.read()
        html=bs.BeautifulSoup(inthtml1, 'lxml')

        href=html.find_all('tr')
        for i in range(0,len(href)):
            mylist.append(href[i].getText())

        import unicodedata

        for i in range(0,len(mylist)):
            myNewlist.append(unicodedata.normalize('NFKD', mylist[i]).encode('ascii','ignore').strip())

        for i in range(0,len(myNewlist)):
            myThirdlist.append(myNewlist[i].decode("utf-8"))

        for i in companyname:
            for m in myThirdlist:
                if i[1:14] in m:
                    d.append(i)
                    d = list(set(d))
        
        if d == []:
            temp.append("NA")
        else:
            temp.append(d)
        
    else:
        temp.append("NA")

MF = []
for i in range(0,len(temp)):
    if temp[i] != "NA":
        MF.append([i]*len(temp[i]))
    else:
        MF.append(i)
MF1 = []
temp1 = []
for i in MF:   
    if type(i) != int:
        MF1.extend(i)
    else:
        MF1.append(i)
for i in temp:
    if i == "NA":
        temp1.append("NA")
    else:
        temp1.extend(i)

Healthfinal=pd.DataFrame(MF1)
Healthfinal.rename(columns={0: 'Mutual Funds'}, inplace=True)
Healthfinal["Companynames"] = temp1
Healthfinal.to_csv('Finan17.csv',index=False)
